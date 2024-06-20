import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BOARD)
gpio.setup(11,gpio.OUT)
gpio.setup(12,gpio.OUT)
gpio.setup(13,gpio.OUT)
gpio.setup(15,gpio.OUT)
gpio.setup(16,gpio.OUT)
a=0
for i in range(0,31):

	s = format(a,'05b')
	gpio.output(11,int(s[0]))
	gpio.output(12,int(s[1]))
	gpio.output(13,int(s[2]))
	gpio.output(15,int(s[3]))
	gpio.output(16,int(s[4]))
	a += 1
	time.sleep(1.5)
gpio.cleanup()




