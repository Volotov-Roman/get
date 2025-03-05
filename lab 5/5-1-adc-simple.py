import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
def decimal2binary(value):
    return [int(element) for element in format(value, '08b')]
def adc():
    for i in range(256):
        GPIO.output(dac, decimal2binary(i))
        time.sleep(0.001)
        if GPIO.input(comp)==0:
            return i
    return 255

dac=[26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=0)
GPIO.setup(comp, GPIO.IN)
try:
    while True:
        print(adc()*3.3/256)
finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()
