import sys
#import RPi.GPIO as GPIO
import time
from math import ceil, floor
import os



#===============initilization=========================
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)#

#================setting pin mode===================
GPIO.setup(11, GPIO.IN)         #Read output from PIR motion sensor
GPIO.setup(3, GPIO.OUT)         #LED output pin


#==============file for interupption management===================
def initialize():
	
	try:
		with open('time_data.time', 'w') as initial:
			initial.write(str(time.time()))
	except Exception as ex:
		print(ex)
		print('The above error have occured')
		sys.exit() 


#=========creating the file ===================
initialize()


#======================function for reducing interuption===============
def file():
	def read():
		try:
	
			with open('time_data.time', 'r') as time_info:
#===============================specifying conditional based on time differences ==================
				time_elapsed = floor(time.time()) - floor(float(time_info.read()))
				print('elapsed time ', time_elapsed)
				if time_elapsed>=4:
					return True
			return False

		except Exception as ex:
			print(ex)
			print('above error occured .......')
			sys.exit()
	if read():
#====================================writing the current time to the file =======================
		initialize()
		return True
	return False
			


#===================return a signal for an arduino to activate the camera========    
def PIR():
	try:
		if file():
			signal = GPIO.input(11)
			#signal = 0
			return signal
		else:
			return 0
	except:
		return 0


