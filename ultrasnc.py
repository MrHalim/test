
    
#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

TRIG = 11
ECHO = 12
BUZZ = 13

def setup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(TRIG, GPIO.OUT)
	GPIO.setup(ECHO, GPIO.IN)
	GPIO.setup(BUZZ, GPIO.OUT)
	
def on():
        GPIO.output(BUZZ, GPIO.LOW)
	

def off():
        GPIO.output(BUZZ, GPIO.HIGH)



def distance():
	GPIO.output(TRIG, 0)
	time.sleep(0.002)

	GPIO.output(TRIG, 1)
	time.sleep(0.001)
	GPIO.output(TRIG, 0)

	
	while GPIO.input(ECHO) == 0:
		a = 0
	time1 = time.time()
	while GPIO.input(ECHO) == 1:
		a = 1
	time2 = time.time()

	during = time2 - time1
	return during * 340 / 2 * 100

def loop():
	while True:
		dis = distance()
		if dis >= 0 and dis <= 30:
                    print dis, 'cm'
                    on()
                   
                   
                else:
                    print dis, 'cm'
                    off()
                    print '' 
               
		time.sleep(0.5)
def destroy():
	GPIO.cleanup()

if __name__ == "__main__":
	setup()
	try:
		loop()
	except KeyboardInterrupt:
		destroy()
