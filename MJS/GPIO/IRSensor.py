import RPi.GPIO as GPIO
import GPIOInit

class IRSensor:
	_pin1 = 0
	def __init__(self, pin1):
		self._pin1 = pin1
		GPIO.setup(_pin1, GPIO.IN)
		GPIO.add_event_detect(_pin, GPIO.RISING, callback=self.SensorBlocked)
	def SensorBlocked(self, channel):
		print("Sensor blocked")



if __name__ == "__main__":
	print("Testing IRSensor")
else:
	print("Including " + __name__)
