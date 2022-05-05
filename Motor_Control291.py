import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BOARD)
delay = 0.009 #2 millisecond
step_pin = 38   #GPIO 20
direction_pin = 37  #GPIO 21
step_pin2 = 8 #GPIO 14
direction_pin2 = 11 #GPIO 15
GPIO.setup(step_pin2, GPIO.OUT)
GPIO.setup(direction_pin2, GPIO.OUT)
GPIO.setup(step_pin, GPIO.OUT)
GPIO.setup(direction_pin, GPIO.OUT)
home1 = 15  #GPIO determine
home2 = 13 #GPIO determine
GPIO.setup(15,GPIO.IN)
GPIO.setup(13,GPIO.IN)

def steps (n):
    count = 0
    while count < n:
        GPIO.output(step_pin, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(step_pin, GPIO.LOW)
        time.sleep(delay)
        count += 1
    return count
        
def steps2 (n):
    count = 0
    while count < n:
        GPIO.output(step_pin2, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(step_pin2, GPIO.LOW)
        time.sleep(delay)
        count += 1
    return count
        
def Motor1(twist_steps,direction):  #Tilt Motor
    
    if direction == 1:  #Clockwise
        GPIO.output(direction_pin, GPIO.LOW)
        steps(twist_steps)
            
    if direction == 2:  #Counterclockwise
        GPIO.output(direction_pin, GPIO.HIGH)
        steps(twist_steps)
                 
    
def Motor2(move_twist,direction): #Twist Motor
        
    if (direction == 1):  #Clockwise
        GPIO.output(direction_pin2, GPIO.HIGH)
        steps2(move_twist)
            
    if (direction == 2):  #Counterclockwise
        GPIO.output(direction_pin2, GPIO.LOW)
        steps2(move_twist)
    
def home():
    while GPIO.input(15) == GPIO.LOW:
        while GPIO.input(15) == GPIO.LOW:
            GPIO.output(direction_pin, GPIO.HIGH)
            steps(1)
    
    time.sleep(1)

    while GPIO.input (13) == GPIO.LOW:
        while GPIO.input(13) == GPIO.LOW:
            GPIO.output(direction_pin2, GPIO.LOW)
            steps2(1)
    
    time.sleep(1)
