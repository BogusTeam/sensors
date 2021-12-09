import datetime
import random
import time

from paho.mqtt import publish

hostname = "demo.thingsboard.io"   ##hostname = "klasi.keenetic.pro"
default_temp = 20
default_volt = 200
def motion(number: int): # datchik dvigeniya
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

if __name__ == "__main__":
    motion(10)