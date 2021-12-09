from multiprocessing import Process

import paho.mqtt.client as paho
import paho.mqtt.subscribe as sub
import paho.mqtt.publish as publish
import time
import random
from datetime import datetime
#pr(10)
hostname = "demo.thingsboard.io"   #
default_temp = 20
default_volt = 200
def motion(number: int): # datchik dvigeniya
    #hostname = "demo.thingsboard.io"
    #hostname = "klasi.keenetic.pro"
    auth = {'username': 'lEtZ0LvBAkGaYIXz2PCK', 'password': ''}  # token TBpKZY4qm5xqLNNNwGT8   lEtZ0LvBAkGaYIXz2PCK


    if (random.randint(0, 1) == 1):
        a = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        ss = '"motion": "' + str(1) + '", "datetime": "' + a + '", "id": "' + str(number) + '"'
    else:
        a = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        ss = '"motion": "' + str(0) + '", "datetime": "' + a + '", "id": "' + str(number) + '"'
    ss = "{" + ss + "}"
    print(ss)
    publish.single("v1/devices/me/telemetry",
                   ss,
                   qos=0,
                   hostname=hostname,
                   auth=auth
                   )
    time.sleep(1)


def temperature(number: int):  # datchik temperaturi
    global default_temp
    auth = {'username': 'fatN7gC2NttXx9CqZFo0', 'password': ''}  #token for pr 9: or6HOVTHuM6WcEIQDQMH

    if (random.randint(0, 1) == 1):
        default_temp -= 5
        a = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        ss = '"temperature": "' + str(default_temp) + '", "datetime": "' + a + '", "id": "' + str(number) + '"'
    else:
        default_temp += 5
        a = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        ss = '"temperature": "' + str(default_temp) + '", "datetime": "' + a + '", "id": "' + str(number) + '"'
    ss = "{" + ss + "}"
    print(ss)

    #client = paho.Client(
    #    "Public")  # create client object client1.on_publish = on_publish #assign function to callback client1.connect(broker,port) #establish connection client1.publish("house/bulb1","on")
    ######Bind function to callback
    #client.on_message = on_message
    #####


    """sub.simple("v1/devices/me/rpc/request/+",
               hostname=hostname,
               auth=auth,
               retained=True
               )
    time.sleep(1)"""
    """client.connect(hostname)

    client.subscribe("v1/devices/me/rpc/request/+")
    client.loop_forever()
    time.sleep(1)"""

    publish.single("v1/devices/me/telemetry",
                   ss,
                   qos=0,
                   hostname=hostname,
                   auth=auth
                   )
    time.sleep(1)

    publish.single("v1/devices/me/rpc/response/3",
                   '{"status: 1"}',
                   qos=1,
                   hostname=hostname,
                   auth=auth
                   )
    time.sleep(1)



def voltage(number: int):  # datchik napryagenia
    global default_volt
    auth = {'username': 'reXKyNioBkbKhB57xZTc', 'password': ''}  #token
    #default_volt = 200


    if (random.randint(0, 1) == 1):
        default_volt -= 10
        a = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        ss = '"voltage": "' + str(default_volt) + '", "datetime": "' + a + '", "id": "' + str(number) + '"'
    else:
        default_volt += 10
        a = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        ss = '"voltage": "' + str(default_volt) + '", "datetime": "' + a + '", "id": "' + str(number) + '"'
    ss = "{" + ss + "}"
    print(ss)
    publish.single("v1/devices/me/telemetry",
                   ss,
                   qos=0,
                   hostname=hostname,
                   auth=auth
                   )
    time.sleep(1)


if __name__ == "__main__":

    #motion(10)
    while True:
        #motion(10)
        temperature(11)
        #voltage(12)


    print("All's done")