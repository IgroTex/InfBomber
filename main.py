import requests
from threading import Thread
import random
from termcolor import colored


print(colored( '''

█ █▄░█ █▀▀ █ █▄░█ █ ▀█▀ █▄█
█ █░▀█ █▀░ █ █░▀█ █ ░█░ ░█░
		  developer IgroTex
''','red'))

phone = input(colored('Enter your phone number>>: ','cyan'))

		requests.post('https://youla.ru/web-api/auth/request_code', 
				json=({"phone":phone})
			print(a.text)
			input
