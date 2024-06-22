import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BOARD)
gpio.setup(11, gpio.IN,pull_up_down=gpio.PUD_UP)
gpio.setup(12, gpio.OUT)
LedState = 0
buttonState = 1
oldbuttonState = 1
try:
	while True:
		buttonState=gpio.input(11)
		if buttonState==1 and oldbuttonState==0:
			LedState = not LedState
			gpio.output(12,LedState)
		oldbuttonState=buttonState
		time.sleep(.1)
except KeyboardInterrupt:
	gpio.cleanup()
