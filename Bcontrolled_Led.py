import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BOARD)
gpio.setup(12,gpio.OUT)
gpio.setup(11,gpio.IN,pull_up_down=gpio.PUD_UP)
gpio.setup(13,gpio.IN,pull_up_down=gpio.PUD_UP)
incState=1
oldincState=1
dcState=1
olddcState=1
pwm=gpio.PWM(12,100)
dcy=10
pwm.start(dcy)
try:
	while True:
		incState=gpio.input(11)
		dcState=gpio.input(13)
		if oldincState == 0 and dcy < 100 and incState == 1:
			dcy += 5
		if olddcState == 0 and dcy > 0 and dcState == 1:
			dcy -= 5
		if dcy >= 100:
			print('Max Brightness')
		if dcy <= 0:
			print('Min Brightness')
		print(dcy)
		pwm.ChangeDutyCycle(dcy)
		oldincState = incState
		olddcState = dcState
		time.sleep(.1)
except KeyboardInterrupt:
	pwm.stop()
	gpio.cleanup()

