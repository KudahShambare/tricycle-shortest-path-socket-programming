#import modules

import socket


#create server socket connection

serverSocket = socket.socket()
port = 2030

#bind the port and ip adresses

serverSocket.bind(("localhost",port))
print("Server ready to connect with the clients")


#set the max number of clients that can connect to the server

serverSocket.listen(10)


while True:
 
	clientSocket, clientAddress = serverSocket.accept()



	#create graph from Nodes

	class Graph:
		#Graph constructor
		def __init__ (self,nodesList,rootNode):
			self.nodesList = nodesList
			self.rootNode = rootNode








	 
   






	 


	clientSocket.close()