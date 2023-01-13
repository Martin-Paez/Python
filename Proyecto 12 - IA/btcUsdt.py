# -*- coding: utf-8 -*-
import requests
import pandas as pd
import pymysql
import sqlalchemy as sql
import time
from datetime import datetime,timedelta


ticker = 'BTCUSDT'
interval = '4h'
user = 'root'
password = '1234'
ip = 'localhost'
db = 'crypto'


engine = sql.create_engine(f'mysql+pymysql://{user}:{password}@{ip}/{db}')

table = ticker + interval
  
with engine.connect() as connection:
    connection.execute(
        f'CREATE TABLE IF NOT EXISTS {table} (  \
            Open_Time bigint primary key,       \
            Open varchar(20),                   \
            High varchar(20),                   \
            Low varchar(20),                    \
            Close varchar(20),                  \
            Volume varchar(20),                 \
            Close_Time bigint,                  \
            Quote_asset_vol varchar(20),        \
            Number_trades int,                  \
            Taker_buy_base varchar(20),         \
            Taker_buy_quote varchar(20),        \
            _Ignore varchar(20),                \
            Open_Timestamp datetime,            \
            Close_Timestamp datetime            \
        );'
    )
    
q = 'select * from ' + table
df = pd.read_sql(q,engine)

last = None
if len(df) > 0:
    df = df.sort_values(by='Open_Time', ascending=True)
    last = df['Open_Time'].iloc[0]


url = 'https://api.binance.com/api/v3/klines'
headers = {'accept' : 'application/json'}
cols = ['Open_Time','Open','High','Low','Close','Volume','Close_Time',  
        'Quote_asset_vol','Number_trades', 'Taker_buy_base','Taker_buy_quote',
        '_Ignore']

body = {'symbol': ticker, 'interval': interval, 'limit':'1000'}

delay = None

try:
    while True:

        data = requests.get(url, headers=headers, params=body).json()
        df = pd.DataFrame(data, columns=cols)    

        df = df.sort_values(by='Open_Time', ascending=True)
        body['endTime'] = str(df['Open_Time'].iloc[0])

        if last == None or last > int(body['endTime']):
            last = int(body['endTime'])
            df['Open_Timestamp'] = pd.to_datetime(df['Open_Time'], unit='ms')
            df['Close_Timestamp'] = pd.to_datetime(df['Close_Time'], unit='ms')  
            
            df.to_sql(name=table, con=engine, if_exists='ignore', index=False)
            print(f'{len(df)} lineas escritas')
        
        else:
            body['limit'] = 1;
            data = requests.get(url, headers=headers, params=body).json()
            body['limit'] = 1000;
            df = pd.DataFrame(data, columns=cols)    
            df['Open_Timestamp'] = pd.to_datetime(df['Open_Time'], unit='ms')
            df['Close_Timestamp'] = pd.to_datetime(df['Close_Time'], unit='ms')  

            candle = df['Close_Timestamp'].iloc[0] - df['Open_Timestamp'].iloc[0]
            now = datetime.now() + timedelta(hours=6)
            elapsed = now - df['Close_Timestamp'].iloc[-1]
            candle - elapsed
            print(f'Esperar {delay} segundos')
            time.sleep(delay)
            delay = 60
            
except Exception as e:
    print(e)
finally:
    engine.dispose()
    print("Fin del programa")
    
    
    
"""
 CREATE TABLE IF NOT EXISTS btcusdt(Open_Time bigint primary key, Open varchar(20), High varchar(20), Low varchar(20), Close varchar(20), Volume varchar(20), Close_Time bigint, Quote_asset_vol varchar(20), Number_trades int, Taker_buy_base varchar(20), Taker_buy_quote varchar(20), _Ignore varchar(20), Open_Timestamp date, Close_Timestamp date);
"""
"""
import pymysql
user = 'root'
passw = '1234'
host =  'localhost'
port = 3306
database = 'crypto'


conn = pymysql.connect(host=host,
                       port=port,
                       user=user, 
                       passwd=passw,  
                       db=database,
                       charset='utf8')

klines.to_sql(name=database, con=conn, if_exists = 'append', index=False)

conn = pymysql.connect(host=host, port=port, user=user, passwd=passw)

conn.cursor().execute("CREATE DATABASE IF NOT EXISTS {0} ".format(database))
conn = pymysql.connect(host=host,
                       port=port,
                       user=user, 
                       passwd=passw,  
                       db=database,
                       charset='utf8')

data.to_sql(name=database, con=conn, if_exists = 'replace', index=False, flavor = 'mysql')

import sqlalchemy as sql

engine = sql.create_engine('mysql+mysql.connector://root:1234@localhost/crypto')

df.to_sql(con=engine, name='btcusdt', if_exists='append', index=False)


insert =  insert into btcusdt(Open_Time, Open, High, Low, Close, Volume,
            Close_Time, Quote_asset_vol, Number_trades, Taker_buy_base,
            Taker_buy_quote, _Ignore, Open_Timestamp, Close_Timestamp) values 
values = ",".join([ ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}',
                       '{}','{}','{}',).format(
                   row.Open_Time,
                   row.Open,
                   row.High
                   row.Low,
                   row.Close,
                   row.Volume,
                   row.Close_Time,
                   row.Quote_asset_vol,
                   row.Number_trades,
                   row.Taker_buy_base,
                   row.Taker_buy_quote,
                   row._Ignore,
                   row.Open_Timestamp,
                   row.Close_Timestamp,
                   ) for i,row in klines.iterrows()])

engine.excetute
                   
cur = sql.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS btcusdt(Open_Time int, Open varchar(20), High varchar(20), Low varchar(20), Close varchar(20), Volume varchar(20), Close_Time int, Quote_asset_vol varchar(20), Number_trades int, Taker_buy_base varchar(20), Taker_buy_quote varchar(20), _Ignore varchar(20), Open_Timestamp int, Close_Timestamp int);')
sql.commit()
df.to_sql(con=sql, name='btcusdt', if_exists='append', index=False)

cur.execute("insert into ldr values(" + str(msg.payload) + "," + str(msg.timestamp) + ")" )
sql.commit()
"""