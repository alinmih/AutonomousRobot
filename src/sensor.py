import RPi.GPIO as GPIO
import time

class Sensor:
	def __init__(self, trig, echo):
		self.trig = trig
		self.echo = echo
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(trig, GPIO.OUT)
		GPIO.setup(echo, GPIO.IN)
	#setup GPIO board config
	# trigger = 18
	# eccho = 24


	def distance(self):
		#set trigger to high
		GPIO.output(self.trig, True)
		
		#set trigger after 0,01ms to low
		time.sleep(0.00001)
		GPIO.output(self.trig, False)
		
		start_time = time.time()
		stop_time = time.time()
		
		#save start time
		while GPIO.input(self.echo) == 0:
			start_time = time.time()
		
		#save stop time
		while GPIO.input(self.echo) ==1:
			stop_time = time.time()

		#calculate time needed
		time_elapsed = stop_time - start_time
		#calculate the distance with sonic speed 343000 mm/s
		distance = (time_elapsed * 343000) / 2
		
		return distance


# trigger = 18
# echo = 24	
# sensor1 = Senzor(trigger, echo)
# try:
# 	while True:
# 		dist = sensor1.distance()
# 		print("Measured distance: %.1f mm" % dist)
# 		time.sleep(0.2)
# except KeyboardInterrupt:
# 	print("Measuremend stopped")
# 	GPIO.cleanup()
