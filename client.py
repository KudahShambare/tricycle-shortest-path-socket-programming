import socket
import pandas
import json
#create client connection

clientSocket = socket.socket()

clientSocket.connect(("localhost",2085))

# import data from excel files
surbubsCodes = pandas.read_excel("Surbubs.xlsx").to_json(orient='records')
routes =  pandas.read_excel("Routes.xlsx").to_json(orient='records')

#convert the json data to python list 
surbubsCodes =json.loads(surbubsCodes)
routes =json.loads(routes)

#create a file to store routes
routesFile = open("routes.txt","w")

#create graph vertices 
toSendToServer = ""
for route in routes:

	#add weight to the routes
	if(route["Route Reports"]>=1):
		
		route["Weight"] = abs((route["Distance"]/route["Time (Minutes)"])*2*route["Route Reports"])
	else:

		route["Weight"] = abs(route["Distance"]/route["Time (Minutes)"])


	#convert every route object into a string and add it to a txt file
	#   $$$   is the delimiter used to split lines in the txt file

	routeString = route["Links"]+"#"+str(route["Distance"])+"#"+str(route["Route Reports"])+"#"+str(route["Time (Minutes)"])+"#"+str(route["Weight"] )+"   $$$$   "
	routesFile.write(routeString)
	toSendToServer+=routeString

#clse file after writing has been completed
routesFile.close()	



#send allLinks to the server

clientSocket.send(bytes(toSendToServer,"utf-8"))
















# get user source and destination






	



	

