import socket
import os


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    UDP_IP = 'localhost'
    UDP_PORT = port
    #sock.connect((UDP_IP, UDP_PORT))
    serverAddressPort = (UDP_IP, UDP_PORT)
    BUFFER_SIZE = 1024

    '''
    sock.sendto(MESSAGE,(UDP_IP, UDP_PORT))#data transfer example
    print MESSAGE
    '''
    filename = raw_input("Enter name of file or 'q' to quit: ")
    if filename == 'q':
        sock.close()
        
    else:
        bytesForSend = filename
        sock.sendto(bytesForSend,serverAddressPort)
        print bytesForSend
        
        print "Would you like to:"
        print "1) Add a new record "
        print "2) Show student info by ID"
        print "3) Find students by score"
        print "4) Show all information for students"
        print "5) Delete a student's record by ID"
        print "6) Exit."
         
        message = raw_input("Enter: ")
    
    if message == "1":
       sock.sendto('ADD',serverAddressPort)
       
       ID = raw_input("ID: ")
       sock.sendto(ID,serverAddressPort)
       fname = raw_input("First name: ")
       sock.sendto(fname,serverAddressPort)
       lname = raw_input("Last name: ")
       sock.sendto(lname,serverAddressPort)
       score = raw_input("Score: ")
       sock.sendto(score,serverAddressPort)
        
    if message == "2":
        sock.sendto('ID',serverAddressPort)
        idNum = raw_input("Enter the student's ID: ")
        sock.sendto(idNum,serverAddressPort)
  
        data, server = sock.recvfrom(BUFFER_SIZE)
        filesize = long(data)
        
                     
        fileData,server = sock.recvfrom(BUFFER_SIZE)
        totalRecv = len(fileData)
        print fileData
         
        while totalRecv < filesize:
            fileData,server = sock.recvfrom(BUFFER_SIZE)
            totalRecv += len(fileData)
            print fileData
           
        print "End of student's info."
        
        
    if message == "3":
       sock.sendto('SCORE',serverAddressPort)
       score = raw_input("Enter a score for displaying students' info: ")
       sock.sendto(score,serverAddressPort)
 
       data, server = sock.recvfrom(BUFFER_SIZE)
       filesize = long(data)
       
                    
       fileData,server = sock.recvfrom(BUFFER_SIZE)
       totalRecv = len(fileData)
       print fileData
        
       while totalRecv < filesize:
           fileData,server = sock.recvfrom(BUFFER_SIZE)
           totalRecv += len(fileData)
           print fileData
          
       print "EOF"
    
    if message == "4":
               sock.sendto('ALL',serverAddressPort)
               printFile,server = sock.recvfrom(BUFFER_SIZE)
               print "Printing on client side: "
               print printFile
    
    if message == "5":
        sock.sendto('RMV',serverAddressPort)
            
        idNum = raw_input("Enter the student's ID you wish to delete: ")
        sock.sendto(idNum,serverAddressPort)
            
        data = sock.recvfrom(BUFFER_SIZE)
        filesize = data
                                  
        fileData,server = sock.recvfrom(BUFFER_SIZE)
        totalRecv = len(fileData)
        print fileData
                                  
        while totalRecv < filesize:
            fileData,server = sock.recvfrom(BUFFER_SIZE)
            totalRecv += len(fileData)
            print fileData
        print "Deletion Completed."
    
    if message == "6":
        sock.close()
               
               
               
               
if __name__ == '__main__':
    main()
