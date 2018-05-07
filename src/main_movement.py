from motor import Motor
from sensor import Sensor
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

trigger = 18
echo = 24	
sensor1 = Sensor(trigger, echo)

pwm_pin_1 = 19
motor1_cw = 4
motor1_ccw = 17
motor_left = Motor(pwm_pin_1, motor1_cw, motor1_ccw)

pwm_pin_2 = 19
motor2_cw = 20
motor2_ccw = 26
motor_right = Motor(pwm_pin_2, motor2_cw, motor2_ccw)

power = 30
direction = "cw"

# dist = 0	
dist = sensor1.distance()
# motor_right.turn_on(power, direction)
# motor_left.turn_on(power, direction)
try:
	while dist > 100:
		dist = sensor1.distance()
		if dist > 700:
			power = 90
		elif dist < 500:
			power = 50
		elif dist < 300:
			power = 30
		print("Measured distance: %.1f mm" % dist)
		motor_right.turn_on(power, direction)
		# motor_left.turn_on(power, direction)
		# time.sleep(0.1)
except KeyboardInterrupt:
	print("Measuremend stopped")
	print("Motor stopped")
	GPIO.cleanup()
	# motor_left.turn_off()