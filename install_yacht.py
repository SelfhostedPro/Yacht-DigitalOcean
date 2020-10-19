#!/usr/bin/env
import docker
from email_validator import validate_email, EmailNotValidError
import os
import secrets
import pyufw as ufw

# Snippets
clear = lambda: os.system('clear')

def get_username():
	while True:
		clear()
		print('Please input the email you would like to use for Yacht: ')
		_email = input("Email: ")

		try:
			valid = validate_email(_email, check_deliverability=False)
			email = valid.email

		except EmailNotValidError as e:
			_email = None
			clear()
			print(str(e))
			input("Press Enter to try again.")
			continue
		return email

def get_port():
	while True:
		try:
			clear()
			print('Select the port you would like Yacht to run on (Default is 8000)')
			port = int(input("(8000) Port: ") or "8000")
			
			if 1<= port <= 65535:
				return port
			else:
				raise ValueError
		except ValueError:
			clear()
			print("Port number"+ port + "is invalid\n")
			input("Press Enter to try again. (1-65535 are valid options)")
			continue
def deploy(email, port):
	clear()
	input("Press enter to deploy Yacht... (This also allows incoming traffic on the port you have specified)")
	ufw.add('allow' + port)
	ufw.reload()
	dclient = docker.from_env()
	try:
		dclient.containers.run(
			image="selfhostedpro/yacht:latest",
			remove=False,
			detach=True,
			ports = {'8000/tcp': port},
			volumes = {
				'/var/run/docker.sock': 
					{'bind': '/var/run/docker.sock', 'mode': 'rw'},
				'/root/.yacht/config':
					{'bind': '/config', 'mode': 'rw'}
			},
			environment = ["ADMIN_EMAIL="+email, "SECRET_KEY="+secrets.token_hex(16)]
		)
	except Exception as e:
		clear()
		print(e)
		input("Press enter to change your port.")
		main_loop(email)
	clear()
	print("\nEmail is set to: " + email)
	print("\nDefault password is: pass")
	print("\nYacht is available on: " + str(port) + '\n')
	print("If you need to run this script again you can use the following command:")
	print("/opt/SelfhostedPro/install_yacht.sh")

def main_loop(email=None):
	if email == None:
		email = get_username()
	port = get_port()
	deploy(email, port)
	exit(0)

main_loop()