import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# GPIO.cleanup()
class Motor:
	def __init__(self, pwm_pin, motor_cw, motor_ccw):
		#pin init
		self.pwm_pin = pwm_pin
		self.motor_cw = motor_cw
		self.motor_ccw = motor_ccw
		GPIO.setup(self.motor_cw, GPIO.OUT)
		GPIO.setup(self.motor_ccw, GPIO.OUT)
		GPIO.setup(self.pwm_pin, GPIO.OUT)
		GPIO.output(self.pwm_pin, True)

	#set direction to cw	
	def cw(self):
		GPIO.output(self.motor_cw, False)
		GPIO.output(self.motor_ccw, True)
	
	#set direction to ccw
	def ccw(self):
		GPIO.output(self.motor_cw, True)
		GPIO.output(self.motor_ccw, False)
		
	#turn on motor
	def turn_on(self, pow, dir):
		if dir == "cw":
			self.cw()
		else:
			self.ccw()
		try:
			pwm = GPIO.PWM(self.pwm_pin,100)
			pwm.start(pow)
			sleep(0.3)
			pwm.stop()
			GPIO.output(self.pwm_pin, False)
		except:
			print("Excepption")


		
	#turn off motor	
	def turn_off(self):
		pwm = GPIO.PWM(self.pwm_pin,100)
		GPIO.output(self.motor_cw, False)
		GPIO.output(self.motor_ccw, False)
		GPIO.output(self.pwm_pin, False)
		pwm.stop()
		GPIO.cleanup()

# pwm_pin_1 = 19
# motor1_cw = 4
# motor1_ccw = 17
# motor_left = Motor(pwm_pin_1, motor1_cw, motor1_ccw)

# pwm_pin_2 = 19
# motor2_cw = 20
# motor2_ccw = 26
# motor_right = Motor(pwm_pin_2, motor2_cw, motor2_ccw)


# power = 50
# direction = "cw"
# # time = 0.1

# # motor_right.turn_on(power, direction, time)
# # motor_left.turn_on(power, direction, time)
# # sleep(2)

# # direction = "ccw"
# # motor_right.turn_on(power, direction)
# # motor_left.turn_on(power, direction)

# # motor_right.turn_off()
# # motor_left.turn_off()



# # # recla 300827796
# try:
# 	while True:
# 		motor_right.turn_on(power, direction)
# 		motor_left.turn_on(power, direction)
		
# except KeyboardInterrupt:
# 	print("Motor stopped")
# 	GPIO.cleanup()
