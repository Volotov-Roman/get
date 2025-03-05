import RPi.GPIO as GPIO

def decimal2binary(value):
    return list(map(int, bin(value)[2:].zfill(8)))

class Exit(Exception):
    pass
GPIO.setmode(GPIO.BCM)

dac=[8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup(dac, GPIO.OUT)
try:
    print('Enter numbers between 0 and 255 one by one')
    while True:
        a=input()
        if a=='q':
            raise Exit
        try:
            c=int(a)
        except Exception:
            print("please enter an integer")
            continue
        finally:
            pass
        a=int(a)
        if a<0 or a>255:
            print("out of range")
        else:
            b=decimal2binary(a)
            GPIO.output(dac, b)
            print(f'{3.3*a/128} V')
except Exit:
    print('manually exited')
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
    print('here')
