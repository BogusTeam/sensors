from paho.mqtt import client as mqtt_client, publish
from time import sleep
from random import randint
from datetime import datetime

hostname = "demo.thingsboard.io"
client_id = f"python-mqtt-{randint(0, 100)}"
topic = "v1/devices/me/rpc/request/+"
username = "H7WXTcZedIlpopjLhLhJ"
password = ""

default_motion = {
    "motion_enable": 0,
    "force_motion": False
}
default_temp = 20
default_volt = 200


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(hostname)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        global default_motion, default_volt

        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

        try:
            d = eval(msg.payload.decode())
            if d.get("device", None) == "motion":
                default_motion["force_motion"] = True
                default_motion["motion_enable"] = int(not bool(default_motion["motion_enable"]))
            elif d.get("device", None) == "voltage":
                default_volt = int(d.get("value", 0))
        except BaseException:
            pass

    client.subscribe(topic)
    client.on_message = on_message


def motion(number: int):  # Motion sensor
    global default_motion

    if not default_motion["force_motion"]:
        default_motion["motion_enable"] = randint(0, 1)
    default_motion["force_motion"] = False
    if default_motion["motion_enable"]:
        a = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        ss = '"motion": "' + str(1) + '", "datetime": "' + a + '", "id": "' + str(number) + '"'
    else:
        a = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        ss = '"motion": "' + str(0) + '", "datetime": "' + a + '", "id": "' + str(number) + '"'
    ss = "{" + ss + "}"
    print(ss)
    publish.single("v1/devices/me/telemetry", ss, qos=0, hostname=hostname,
                   auth={'username': 'lEtZ0LvBAkGaYIXz2PCK', 'password': ''})
    sleep(1)


def temperature(number: int):  # Temperature sensor
    global default_temp

    if randint(0, 1) == 1:
        default_temp -= 5
        a = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        ss = '"temperature": "' + str(default_temp) + '", "datetime": "' + a + '", "id": "' + str(number) + '"'
    else:
        default_temp += 5
        a = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        ss = '"temperature": "' + str(default_temp) + '", "datetime": "' + a + '", "id": "' + str(number) + '"'
    ss = "{" + ss + "}"
    print(ss)
    publish.single("v1/devices/me/telemetry", ss, qos=0, hostname=hostname,
                   auth={'username': 'or6HOVTHuM6WcEIQDQMH', 'password': ''})
    sleep(1)


def voltage(number: int):  # Voltage sensor
    global default_volt

    if randint(0, 1) == 1:
        default_volt -= 10
        a = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        ss = '"voltage": "' + str(default_volt) + '", "datetime": "' + a + '", "id": "' + str(number) + '"'
    else:
        default_volt += 10
        a = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        ss = '"voltage": "' + str(default_volt) + '", "datetime": "' + a + '", "id": "' + str(number) + '"'
    ss = "{" + ss + "}"
    print(ss)
    publish.single("v1/devices/me/telemetry", ss, qos=0, hostname=hostname,
                   auth={'username': 'reXKyNioBkbKhB57xZTc', 'password': ''})
    sleep(1)


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_start()
    while True:
        motion(10)
        temperature(11)
        voltage(12)


if __name__ == "__main__":
    run()
