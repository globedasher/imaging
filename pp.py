import RPi.GPIO as GPIO
import paho.mqtt.client as cmqtt

def on_publish(client, userdata, mid):
    #client.disconnect()
    return

topic = "rico/pub/button"
client = cmqtt.Client()
try:
    #I don't know what "try" does!! :( 
    client.connect("iot.eclipse.org", 1883, 60)
client.on_publish = on_publish

while True:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4,GPIO.IN)
    if GPIO.input(4) == GPIO.LOW:
        client.publish(topic, "test!", retain=True)
        GPIO.cleanup()
        break

client.loop_forever()
