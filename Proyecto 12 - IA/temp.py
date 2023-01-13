# -*- coding: utf-8 -*-
import requests
import pandas as pd

#domain = 'https://testnet.binance.vision/api/v3/'
domain = 'https://api.binance.com/api/v3/'

re = requests.get(domain+"exchangeInfo")
data = re.json()
symbols = data['symbols']

symbol_list = []
status_list = []

for item in symbols:
    symbol_list.append(item['symbol'])
    status_list.append(item['status'])

btc_symbol = filter(lambda x : 'BTCUSDT' == x, symbol_list)
btc_symbol_list = list(btc_symbol)

interval = '6h'

for symbol_str in btc_symbol_list:
    print('----------------------')
    print(f'Descargando {symbol_str}')
    url = domain +'klines'
    headers = {'accept' : 'application/json'}
    doc_columns = ['Open_Time','Open','High','Low',
                   'Close','Volume','Close_Time',
                   'Quote_asset_vol','Number_trades',
                   'Taker_buy_base','Taker_buy_quote','Ignore']
    main_df = pd.DataFrame(columns=doc_columns)
    
    pagination = True
    initial_round = True
    last_end_time = None
    
    while pagination:
        try:
            if initial_round:
                print('Ronda inicial')
                body = {'symbol': symbol_str, 'interval': interval, 'limit':'1000'}
                initial_round = False
            else:
                body = {'symbol': symbol_str, 'interval': interval, 'limit':'1000', 'endTime':end_time}
            
            response = requests.get(url, headers=headers, params=body)
            data = response.json()
            df = pd.DataFrame(data, columns=doc_columns)
            df['Open_Timestamp'] = pd.to_datetime(df['Open_Time'], unit='ms')
            df['Close_Timestamp'] = pd.to_datetime(df['Close_Time'], unit='ms')        
            
            main_df = pd.concat([main_df,df])
            main_df = main_df.sort_values(by='Open_Timestamp', ascending=True)
            end_time = str(main_df['Open_Time'].iloc[0])
        
            if last_end_time == end_time:
                print("Listo")
                break
        
            last_end_time = end_time
        
        except:
            pagination = False
    
    file_name = symbol_str + '_' + interval + '.csv'
    print("Guardando el archivo {symbol_str}.csv")
    main_df.to_csv(file_name,index=False)

    print(main_df.shape)
    
    
    