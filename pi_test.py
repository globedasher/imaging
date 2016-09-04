import RPi.GPIO as GPIO
import paho.mqtt.client as cmqtt
import time

#I want this section of code to be placed in a function, but I don't know
# why I cannot get two functions to share the data

#use the BCM I/O numbering scheme
GPIO.setmode(GPIO.BCM)
#set pin 2 to be an input
GPIO.setup(4,GPIO.IN)
#set pin 18 to be the output
GPIO.setup(18, GPIO.OUT)
#set pin 23 to be an output
GPIO.setup(23, GPIO.OUT)

topic = "rico/pub/button"
client = cmqtt.Client()
client.connect("iot.eclipse.org", 1883, 60)

while True:
    GPIO.output(23, GPIO.LOW)
    GPIO.output(18, GPIO.HIGH)
    time.sleep(.5)
    GPIO.output(18, GPIO.LOW)
    time.sleep(.5)

    if GPIO.input(4) == GPIO.LOW:
        client.publish(topic, "test!", retain=True)
        print("Shutting down in...")
        count = 5
        GPIO.output(18, GPIO.LOW)
        GPIO.output(23, GPIO.HIGH)
        for char in "shutd":
            print(count)
            count = count - 1
            time.sleep(1)
        GPIO.cleanup()

    # The callback for when the client recieves a CONNACK response from the 
    # server.
    def on_connect(client, userdata, flags, rc):
        print("Connected with result code " +str(rc))

        # Subscribing in on_connect means subscriptions will be renewed if 
        # we lose the connection and reconnect.
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

client.loop_forever()
