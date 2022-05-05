import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

home1 = 15  #GPIO determine
home2 = 13 #GPIO determine
GPIO.setup(15,GPIO.IN)
GPIO.setup(13,GPIO.IN)

delay = 0.008 #2 millisecond
step_pin = 38   #GPIO 20
direction_pin = 40  #GPIO 21
step_pin2 = 8 #GPIO 14
direction_pin2 = 10 #GPIO 15
GPIO.setup(step_pin2, GPIO.OUT)
GPIO.setup(direction_pin2, GPIO.OUT)
GPIO.setup(step_pin, GPIO.OUT)
GPIO.setup(direction_pin, GPIO.OUT)

def steps (n):
    count = 0
    while count < n:
        GPIO.output(step_pin, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(step_pin, GPIO.LOW)
        time.sleep(delay)
        count += 1

def steps2 (n):
    count = 0
    for n in count:
        GPIO.output(step_pin2, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(step_pin2, GPIO.LOW)
        time.sleep(delay)
        count += 1
        
GPIO.input(15) == 0

GPIO.output(direction_pin, GPIO.HIGH)
while GPIO.input(15) == GPIO.HIGH:
    steps(10)
    
time.sleep(5)

while home2 == GPIO.LOW:
    GPIO.output(direction_pin2, GPIO.HIGH)
    steps2(100)
        