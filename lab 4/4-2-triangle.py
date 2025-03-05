import time
import RPi.GPIO as GPIO
def decimal2binary(value):
    return list(map(int, bin(value)[2:].zfill(8)))
GPIO.setmode(GPIO.BCM)
dac=[8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup(dac, GPIO.OUT)
values=[i for i in range(255)] + [i for i in range(255,-1,-1)]
bin_values=[decimal2binary(value) for value in values]
period=1
try:
    while True:
        for bin_value in bin_values:
            GPIO.output(dac,bin_value)
            time.sleep(0.005)
        time.sleep(period)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()