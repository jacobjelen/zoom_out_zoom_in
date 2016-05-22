#!/usr/bin/env python

MS_key1 = "647e1b31bc4e4c0281ff9276bd135a13" # MicroSoft API key 1
MS_key2 = "3e99f41bc1f3429cb40b4f32233bc40b" # MicroSoft API key 2

from projectoxford.speech import SpeechClient 	# Project Oxford Library (MS APIs wrapper) 

import sys	# used to stop the program
gen = ""
track = 0

# === Speech Function =============================

def speech(gen):
	import requests

	en = SpeechClient(MS_key1 , gender=gen, locale='en-GB')	# speech client for input - english
	jp = SpeechClient(MS_key1 , gender=gen, locale='ja-JP')	# speech client for output - japanese

	order = en.input("Say something in English...") # transcribes what you say into text and stores it in order variable
	print(order)
	jp.print(order)	# reads back the text with japanese accent

	requests.get('localhost:5000')

	global track	# enables editing the 'track' variable inside this function
	jp.say_to_wav(order, filename="rec/" + str(track) + "-" + gen + ".wav")		# saves recording of the repetition and numbers it
	track = track + 1
# === Map Function ================================

# === Main Loop ===================================

while gen !="q":		# 
	gen = input("Select gender M / F : ")

	if gen == "m" or gen == "M":
		
		print("male")
		speech("Male")

	elif gen == "f" or gen == "F":
	
		print("Female")
		speech("Female")
	
	elif gen == "q" or gen == "Q":
		sys.exit()		#stops the entire program
	
	else: 
		print("Must be: M - Male // F - Female // Q - Quit : ")	






