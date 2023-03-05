#import modules

import socket


#create server socket connection

serverSocket = socket.socket()
port = 2085

#bind the port and ip adresses

serverSocket.bind(("localhost",port))
print("Server ready to connect with the clients")


#set the max number of clients that can connect to the server

serverSocket.listen(10)


while True:
 
	clientSocket, clientAddress = serverSocket.accept()

	#client data

	fromClient = clientSocket.recv(2048).decode()
	fromClientArr = fromClient.split("   $$$$   ")
	fromClientArr.pop()
	
	#create Graph Edges from data received from client

	class Edge:

	   def __init__ (self,src,to,weight):
		   self.src = src
		   self.to = to
		   self.weight = weight

	  
	#LIST to store all edges
	allEdges = []


	for route in fromClientArr:
		routeString = route.split("#")
		
		routeFromAndTo = routeString[0].split(",") 
		source = routeFromAndTo[0]
		destination = routeFromAndTo[1]
		routeWeight = float( routeString[4] )

		routeEdge = Edge(source,destination,routeWeight)
		allEdges.append(routeEdge)



	#create graph from Nodes

	class Graph:
		#Graph constructor
		def __init__ (self,edges,nodes):
			self.edges = edges
			self.nodes = nodes

			


		#Set root node distance to zero and others to infinity = 999
		def setDistance(self,root):
			dist = "" 
			for node in self.nodes:
				if (node != root):
					dist=  999
				else:
					dist = 0

				print(node , dist)


		#Shortest path algorithm  -- takes 2 edges codes as parameters
		def dijkstra(self,source,destination):
			print( source)
			

	#sample graph to work with --- assuming that root is 1
	allNodes = list(range(1,43))
	tricycleGraph = Graph(allEdges,allNodes)

	tricycleGraph.setDistance(10)

	









	 
   






	 


	clientSocket.close()