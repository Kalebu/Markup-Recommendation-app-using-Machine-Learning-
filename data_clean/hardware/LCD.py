""" 

Installation of the following library is required 

->Adafruit_Python_CharLCD

follow the following instructions to install the above library on pi

1.    git clone https://github.com/adafruit/Adafruit_Python_CharLCD.git

2.    cd ./Adafruit_Python_CharLCD

3.    sudo python setup.py install


after installation of the above library 
connect the lcd pins to raspberry pi 
indicated in below code 

"""
     



#______________________________code_______________________________________

from Adafruit_CharLCD import Adafruit_CharLCD 
from time import sleep


#=============== specify lcd========================
lcd = Adafruit_CharLCD(rs=26, en=19, d4=13, d5=6, d6=5, d7=21, cols=16, lines=2)  
lcd.clear()


def show_results(makeup_type):	
	#_______________showing the makeup result_________________
	try:
		makeup_message = 'You Need\nMakeup type '+makeup_type
		print(makeup_message)
		lcd.message(makeup_message)
		sleep(1)
		print('displayed on the lcd screen')
	except Exception as ex:
		print(ex)
		print("The above error have occured")
		
#____________________________end code___________________________________________



