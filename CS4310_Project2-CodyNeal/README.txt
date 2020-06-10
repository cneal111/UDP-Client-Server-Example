This document shall server as the README for the project 2 UDP client-server:

In this project folder are two separate sub folders titled "Client" and "Server":
	-both of these folders contain a single python file.
		a.) the Client folder has UDPClient.py 
		b.) the Server folder has UDP-Server.py and studentrecords.txt

RUNNING THE PROGRAM:


-If using the files for localhost use, the Server file will need to be edited to bind the socket to '127.0.0.1' and an appropriate port number.

-If using the files on the servers:
	- in the UDP-Server.py file, please bind the UDP_IP to the addr of your server and
	  for UDP_PORT please enter a valid port number.
	- in the UDPClient.py file, please enter the same credentials for the UDP_IP and 	  UDP_PORT that you have used for the server as the client will send request 		  there.
	-UDP_IP and UDP_PORT are both located within the main function of both files.


-After reaching the appropriate directories for which you have placed these files

Command for running server file:
python UDP-Server.py

Command for running client file:
python UDPClient.py
	i.) Once prompted for file name enter: studentrecords.txt
	-the file extension must be included.

