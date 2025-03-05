import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
def decimal2binary(value):
    return [int(element) for element in format(value, '08b')]
def adc():
    v=0
    GPIO.output(dac, decimal2binary(128))
    time.sleep(0.001)
    if GPIO.input(comp)==1:
        v+=128
    GPIO.output(dac, decimal2binary(64+v))
    time.sleep(0.001)
    if GPIO.input(comp)==1:
        v+=64
    GPIO.output(dac, decimal2binary(32+v))
    time.sleep(0.001)
    if GPIO.input(comp)==1:
        v+=32
    GPIO.output(dac, decimal2binary(16+v))
    time.sleep(0.001)
    if GPIO.input(comp)==1:
        v+=16
    GPIO.output(dac, decimal2binary(8+v))
    time.sleep(0.001)
    if GPIO.input(comp)==1:
        v+=8
    GPIO.output(dac, decimal2binary(4+v))
    time.sleep(0.001)
    if GPIO.input(comp)==1:
        v+=4
    GPIO.output(dac, decimal2binary(2+v))
    time.sleep(0.001)
    if GPIO.input(comp)==1:
        v+=2
    GPIO.output(dac, decimal2binary(1+v))
    time.sleep(0.001)
    if GPIO.input(comp)==1:
        v+=1
    return v

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
