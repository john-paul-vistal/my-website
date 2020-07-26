import paho.mqtt.client as mqtt
import time

print("This is the Third Publisher client")
topic = input("Published Topic: ")
payload = input('Published Payload: ')

def on_connect(client, userdata, flags, rc):
    print("")
    print("Connected with result code "+str(rc))
    print("")

client = mqtt.Client()
client.on_connect = on_connect

client.connect("mqtt.eclipse.org", 1883, 60)

time.sleep(1)
while True:
    client.loop()
    client.publish(topic, payload)
    time.sleep(1)
