import pandas as pd
import requests
import pandas as pd
import pymysql
import sqlalchemy as sql
import time
from datetime import datetime,timedelta


class KlinesClient:
            
    @classmethod
    def new(self, ticker, interval, override = False):
        db = KlinesDB.instantiate(ticker, interval)
        c = KlinesClient(db, ticker, interval, override)
        return c
    
    @classmethod
    def new2(self, ticker, interval, user, passw, ip, db, override=False):
        db = KlinesDB(user, passw, ip, db, ticker, interval)
        c = KlinesClient(db, ticker, interval, override)
        return c
    
    def __init__(self, db, ticker, interval, override = False):
        self._ticker = ticker
        self._interval = interval
        self._db = db
        self._start(override)
    
    def _start(self, override = False):
       #system('cls')
        if override:
            self._db.dropTable()
        self._db.createTable()
        minBD = self._db.oldest()
        while True:
            df = self._reqKlines(first=minBD)
            minDf = df.oldest()
            if minBD == None or minBD  > minDf:
                minBD = minDf
                self._db.insert(df)
                print(f'{df.size()} lineas escritas')
            else:
                delay = self._reqKlines(1).closeTime()
                for i in range(delay):
                    time.sleep(1)
                    hs = pd.to_timedelta(delay - i, unit='s')
                    print(f'Esperando {hs} segundos')
                delay = 60
        
    def _reqKlines(self, n=1000, first=None):
        url = 'https://api.binance.com/api/v3/klines'
        headers = {'accept' : 'application/json'}
        cols = ['Open_Time','Open','High','Low','Close','Volume','Close_Time',  
                'Quote_asset_vol','Number_trades', 'Taker_buy_base','Taker_buy_quote',
                '_Ignore']
        body = {
                'symbol': self._ticker,
                'interval': self._interval,
                'limit':str(n)
                }
        if first != None:
            body['endTime'] = int(first.timestamp() * 1000)
        data = requests.get(url, headers=headers, params=body).json()
        df = pd.DataFrame(data, columns=cols)
        if len(df)>1: # Para sleep(delay) se pide uno solo
            df = df[0:-1]
        return KlineDF(df)


class KlineDF:
    
    def __init__(self, df):
        df['Open_Timestamp'] = df['Open_Time'].copy()
        df['Close_Timestamp'] = df['Close_Time'].copy()
        self._df = df
        self._toDatetime('Open_Time')
        self._toDatetime('Close_Time')
        self._delCol('Quote_asset_vol')
        self._delCol('Number_trades')
        self._delCol('Taker_buy_base')
        self._delCol('Taker_buy_quote')
        self._delCol('_Ignore')
        
    def _toDatetime(self, key):
        self._df[key] = pd.to_datetime(self._df[key], unit='ms')
        
    def _delCol(self, name):
        self._df.drop(name, inplace=True, axis=1)
    
    def oldest(self):
        self._df = self._df.sort_values(by='Open_Time', ascending=True)
        return self._df['Open_Time'].iloc[0]
    
    def size(self):
        return len(self._df)
    
    def dataFrame(self):
        return self._df
    
    def closeTime(self):
        if self.size() == 0:
            raise Exception('No hay datos en la tabla con que calcular el\
                            cierre de la proxima vela')
        candle = self._df['Close_Time'].iloc[0] 
        candle = candle - self._df['Open_Time'].iloc[0]
        now = datetime.now() + timedelta(hours=6)
        self._df = self._df.sort_values(by='Close_Time', ascending=True)
        elapsed = now - self._df['Close_Time'].iloc[-1]
        delay = candle - elapsed
        return int(delay.total_seconds())+1


class KlinesDB:
    
    @classmethod
    def instantiate(self, ticker, interval):
        return KlinesDB('root','1234','localhost','crypto', ticker, interval)
    
    def __init__(self, user, passw, ip, db, ticker, interval):
        self._name = ticker + interval
        self._sql = sql.create_engine(f'mysql+pymysql://{user}:{passw}@{ip}/{db}')
    
    def createTable(self):
        with self._sql.connect() as connection:
            connection.execute(f'                               \
                CREATE TABLE IF NOT EXISTS {self._name} (       \
                    Open_Time datetime primary key,             \
                    Close_Time datetime,                        \
                    Open varchar(20),                           \
                    High varchar(20),                           \
                    Low varchar(20),                            \
                    Close varchar(20),                          \
                    Volume varchar(20),                         \
                    Open_Timestamp bigint,                      \
                    Close_Timestamp bigint                      \
                );                                              \
            ')
            
    def oldest(self):
        return self._select('min(Open_Time) as o')['o'].iloc[0] 
            
    def recent(self):
        return self._select('max(Open_Time) as o')['o'].iloc[0] 
        
    def _select(self, fields):
        return pd.read_sql(f'select {fields} from {self._name}', self._sql)
            
    def dropTable(self):
        with self._sql.connect() as connection:
            connection.execute(f'drop table {self._table};')
        
    def insert(self, kdf):
        kdf.dataFrame().to_sql(
            name=self._name.lower(), 
            con=self._sql, 
            if_exists='append', 
            index=False 
        )
        
    def read(self):
        q = 'select * from ' + self._name
        return pd.read_sql(q,self._sql)

"""
   
   TABLA COMPLETA
   
   connection.execute(f'                               \
       CREATE TABLE IF NOT EXISTS {self._table} (      \
           Open_Time bigint primary key,               \
           Open varchar(20),                           \
           High varchar(20),                           \
           Low varchar(20),                            \
           Close varchar(20),                          \
           Volume varchar(20),                         \
           Close_Time bigint,                          \
           Quote_asset_vol varchar(20),                \
           Number_trades int,                          \
           Taker_buy_base varchar(20),                 \
           Taker_buy_quote varchar(20),                \
           _Ignore varchar(20),                        \
           Open_Timestamp datetime,                    \
           Close_Timestamp datetime                    \
       );                                              \
   ')
   
"""

def test():    
    KlinesClient.new('BTCUSDT', '4h')

#test()