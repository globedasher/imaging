import RPi.GPIO as gpio

gpio.setmode(gpio.BCM_)
gpio.setup(4, gpio.IN)
gpio.setup(18, gpio.OUT)
gpio.setup(23, gpio.OUT)

def closeGPIO():
    gpio.cleanup()
