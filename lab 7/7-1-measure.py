import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt
GPIO.setmode(GPIO.BCM)

def troyka_voltage():    # вычисляем напряжение на тройка-модуле (АЦП)
    v=0
    GPIO.output(dac, decimal2binary(128))
    time.sleep(t)
    if GPIO.input(comp)==0:
        v+=128
    GPIO.output(dac, decimal2binary(64+v))
    time.sleep(t)
    if GPIO.input(comp)==0:
        v+=64
    GPIO.output(dac, decimal2binary(32+v))
    time.sleep(t)
    if GPIO.input(comp)==0:
        v+=32
    GPIO.output(dac, decimal2binary(16+v))
    time.sleep(t)
    if GPIO.input(comp)==0:
        v+=16
    GPIO.output(dac, decimal2binary(8+v))
    time.sleep(t)
    if GPIO.input(comp)==0:
        v+=8
    GPIO.output(dac, decimal2binary(4+v))
    time.sleep(t)
    if GPIO.input(comp)==0:
        v+=4
    GPIO.output(dac, decimal2binary(2+v))
    time.sleep(t)
    if GPIO.input(comp)==0:
        v+=2
    GPIO.output(dac, decimal2binary(1+v))
    time.sleep(t)
    if GPIO.input(comp)==0:
        v+=1
    return v

def decimal2binary(value):   # просто перевод из десятичной в двоичную
    return [int(element) for element in format(value, '08b')]

def leds_out(value):
    GPIO.output(leds, value)

dac=[8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup(dac, GPIO.OUT)
leds=[2, 3, 4, 17, 27, 22, 10, 9]
GPIO.setup(leds, GPIO.OUT)
comp = 14
GPIO.setup(comp, GPIO.IN)
troyka = 13
GPIO.setup(troyka,GPIO.OUT,initial=GPIO.LOW)

measured_data = []   # храним измеренные значения
current_voltage = 0
t=0.001

try:          # основная часть кода, где сначала конденсатор заряжается, а потом разряжается (два соответствующих цикла while)
    start = time.time()
    GPIO.output(troyka, 1)
    while current_voltage < 0.97*255*2.43/3.3:    # странные цифры ввиду ограничений конкретной платы и конкретной RC-цепи
        current_voltage = troyka_voltage()
        measured_data.append(current_voltage)
        leds_out(decimal2binary(current_voltage))
        print(current_voltage)
    GPIO.output(troyka, 0)
    print('phase 2')
    while current_voltage > 0.02*255*2.43/3.3:
        current_voltage = troyka_voltage()
        measured_data.append(current_voltage)
        print(current_voltage)
    finish = time.time()
    duration = finish - start
    plt.plot(measured_data)
    plt.show()
    with open('data.txt', 'w') as d:
        for voltage in measured_data:
            d.write(str(voltage) + '\n')
    with open('settings.txt', 'w') as s:
        s.write('Частота дискретизации: 1000 Гц \n')
        s.write('Шаг квантования: 0.012890625 В')
    print(duration)
    print(t)
    print(1000)
    print(0.012890625)
finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.output(leds, 0)
    GPIO.cleanup()