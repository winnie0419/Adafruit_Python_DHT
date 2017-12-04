#!/usr/bin/python
import time, RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
count=0
while (count<10):
	GPIO.output(17,1)
	time.sleep(1)
	GPIO.output(17,0)
	time.sleep(1)
	count=count+1
