import time
import paho.mqtt.client as mqtt
import random

from getpass import getpass
# pip3 install mysql-connector-python
# OJO, NO usar pip install mysql.connector
from mysql.connector import connect, Error

sqlIP = "192.168.0.15";
emqxIP = sqlIP;
sql = None
sqlCursor = None;
try:
    sql = connect(
        host=sqlIP,
        user="root",
        password="1234",
        database="iot"
    )
    sqlCursor = sql.cursor();
except Error as e:
    print(e)
  
def on_connect(client, userdata, flags, rc):
    print('Conectado. Codigo: '+str(rc))
    client.connected_flag = rc == 0
    if not client.connected_flag :
        print("Error de conexion: " + str(rc))
        
def on_message(client, userdata, msg):
    msg.payload = msg.payload.decode("utf-8")
    print("Subscripci.: Topico = " + msg.topic + ", Payload = " + str(msg.payload))
    sqlCursor.execute("insert into ldr values(" + str(msg.timestamp) + "," + str(msg.payload) + ")" )
    sql.commit()

def on_disconnect(client, userdata,rc=0):
    if rc != 0:
        print("Codigo: "+str(rc)+" Reconectando...")
        client.connected_flag = False        
        client.reconnect()
        while not client.connected_flag: #wait in loop
            time.sleep(1)

def initClient(name):
    client = mqtt.Client(name)
    client.connected_flag = False
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_message = on_message
    client.connect(emqxIP, 1883, 60)
    client.loop_start()
    while not client.connected_flag: #wait in loop
        time.sleep(1)
    return client

observer = initClient("observer")
observer.subscribe('ldr')

observable = initClient("observable")
for i in range(50):
    observable.publish('ldr', random.random() * 100) 
    print("Publicacio.: Topico = ldr")
    time.sleep(0.1)
    observable.loop()

observable.loop_stop()
observer.disconnect()

print("SELECT val, time FROM ldr; : ");

sqlCursor.execute("SELECT val, timestamp FROM ldr ")

for (val, timestamp) in sqlCursor:
    print(f'( {timestamp}, {val} )')
        
sqlCursor.close()
sql.close()  

print("Fin del programa")
