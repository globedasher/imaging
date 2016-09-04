""" This applicaiton sends an MQTT message when the I/O of the 
Raspberry Pi is triggered.
"""
import RPi.GPIO as GPIO

import paho.mqtt.client as cmqtt

import time
import threading

trigger = 0

#I want to move this I/O configuration to a function at some point
#use the BCM I/O numbering scheme
GPIO.setmode(GPIO.BCM)
#set pin 2 to be an input
GPIO.setup(4,GPIO.IN)
#set pin 18 to be the output
GPIO.setup(18, GPIO.OUT)
#set pin 23 to be an output
GPIO.setup(23, GPIO.OUT)

def run_app():
    """This function runs the I/O of the Raspberry Pi.
    """
    while True:
        GPIO.output(23, 0)
        GPIO.output(18, 1)
        time.sleep(.5)
        GPIO.output(18, 0)
        time.sleep(.5)

        if GPIO.input(4) == 0:
            trigger = 1
            print("Shutting down in...")
            count = 5
            GPIO.output(18, 0)
            GPIO.output(23, 1)
            for char in "shutd":
                print(count)
                count = count - 1
                time.sleep(1)
            GPIO.cleanup()
            return trigger

def mqtt_msg():
    topic = "rico/pub/button"
    client = cmqtt.Client()
    client.connect("iot.eclipse.org", 1883, 60)
    
    # The callback for when the client recieves a CONNACK response from the server.
    def on_connect(client, userdata, flags, rc):
        print("Connected with result code " +str(rc))

        # Subscribing in on_connect means subscriptions will be renewed if we lose
        # the connection and reconnect.
        client.subscribe(topic)

    # the callback for when a publish message is recieved from the server
    def on_message(client, userdata, msg):
        print(msg.topic + " " + str(msg.payload))

    def on_publish(client, userdata, mid):
        #client.disconnect()
        return

    client.on_connect = on_connect
    client.on_message = on_message
    client.on_publish = on_publish

    if trigger == 1:
        print("teeth")
        client.publish(topic, "trip", qos=0, retain=True)
    client.loop_forever()


mq = threading.Thread(target=mqtt_msg)
io = threading.Thread(target=run_app)

io.start()
mq.start()
