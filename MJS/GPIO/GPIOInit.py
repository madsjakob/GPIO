import RPi.GPIO as GPIO

class MGP:
	def __init__(self):
		print("Hello world!")
		GPIO.setmode(GPIO.BCM)
	def __del__(self):
		GPIO.cleanup()
		print("Goodbye cruel world!")


print("including")

x = MGP()

print("ifsddsf")
