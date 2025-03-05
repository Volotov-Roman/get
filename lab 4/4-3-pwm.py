import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
pwm=GPIO.PWM(24, 1000)
pwm.start(0)
try:
    print('Enter a number between 0 and 100')
    while True:
        pwm.ChangeDutyCycle(float(input()))
finally:
    GPIO.output([27,24], 0)
    GPIO.cleanup()