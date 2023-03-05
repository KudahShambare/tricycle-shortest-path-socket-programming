import socket
import pandas
import json
#create client connection

clientSocket = socket.socket()

clientSocket.connect(("localhost",2030))

# import data from excel files
surbubsCodes = pandas.read_excel("Surbubs.xlsx").to_json(orient='records')
routes =  pandas.read_excel("Routes.xlsx").to_json(orient='records')

#convert the json data to python list 
surbubsCodes =json.loads(surbubsCodes)
routes =json.loads(routes)


#create graph vertices 
allLinks = []
for route in routes:

	#add weight to the routes
	if(route["Route Reports"]>=1):
		
		route["Weight"] = abs((route["Distance"]/route["Time (Minutes)"])*2*route["Route Reports"])
	else:

		route["Weight"] = abs(route["Distance"]/route["Time (Minutes)"])



	links = route["Links"].split(",")
	allLinks.append(links)


class Node:

	def __init__ (self,code,name,neighbors):
		self.code = code
		self.name = name
		self.neighbors = neighbors

#create nodes for all surbubs and store them in list

allNodes=[]

for surbub in surbubsCodes:
	myNeighbors =[]
	for pair in allLinks:
		code = str(surbub["Code"])
		if(pair[0] == code):
			myNeighbors.append(pair[1])
	node = Node(surbub["Code"],surbub["Name"],myNeighbors)
	allNodes.append(node)

	
#rint(surbubsCodes)

for node in allNodes:
	joined = node.neighbors
	#msp neigbor code to node objects
	neighborsObjects = []
	for joiny in joined:
		obj = allNodes[int(joiny)-1]
		#obj["weight"]
		neighborsObjects.append(obj)
		#print(neighborsObjects)
	node.neighbors=neighborsObjects
		
		
			

	
	#print(node.name,node.code,node.neighbors)



# get user source and destination






	



	

