import socket
import os
import readline
import threading
import sys

def add(c,file,serverSock):
    print "at Add"
    
    studentID,c = serverSock.recvfrom(1024)
    studentFName,c = serverSock.recvfrom(1024)
    studentLName,c = serverSock.recvfrom(1024)
    studentScore,c = serverSock.recvfrom(1024)

    with open(file, 'a') as f:
        f.write(studentID + "\t"+ studentFName + "\t" +\
        studentLName + "\t" + studentScore)
        f.write("\n")
        
    print "Student record added"
    
def displayID(c,file,serverSock,address):
    print "at ID"
    idNum,c = serverSock.recvfrom(1024)
    print idNum
    with open(file, 'rb') as f:
            s = ' '
            while(s):
                s = f.readline()
                field = s.split("\t")
                if len(s) > 0:
                    if (field[0]) == idNum:
                        
                        with open('tempfile.txt', 'wb') as t:
                            studentID = field[0]
                            t.write(studentID + "\t")
                            print studentID
                            
                            studentFName = field[1]
                            t.write(studentFName + "\t")
                            
                            studentLName = field[2]
                            t.write(studentLName + "\t")
                            
                            studentScore = field[3]
                            t.write(studentScore + "\n")
                       
                            t.close()
            f.close()
            
    with open('tempfile.txt','rb') as t:
            filesize = str(os.path.getsize('tempfile.txt'))
            serverSock.sendto(filesize,address)
                            
            bytesToSend = t.read(1024)
            serverSock.sendto(bytesToSend,address)
            while bytesToSend != "":
                bytesToSend = t.read(1024)
                serverSock.sendto(bytesToSend,address)
            t.close()
            
    if os.path.exists("tempfile.txt"):
        os.remove("tempfile.txt")
    
    else:
          print("The file does not exist")



def displayScore(c,file,serverSock,address):
    print "at Score"
    score,c = serverSock.recvfrom(1024)
    print score
    with open(file, 'rb') as f:
            s = ' '
            while(s):
                s = f.readline()
                field = s.split("\t")
                if len(s) > 0:
                    if (field[3]) > score:
                        
                        with open('tempfile.txt', 'wb') as t:
                            studentID = field[0]
                            t.write(studentID + "\t")
                            print studentID
                            
                            studentFName = field[1]
                            t.write(studentFName + "\t")
                            
                            studentLName = field[2]
                            t.write(studentLName + "\t")
                            
                            studentScore = field[3]
                            t.write(studentScore + "\n")
                       
                            t.close()
            f.close()
            
    with open('tempfile.txt','rb') as t:
            filesize = str(os.path.getsize('tempfile.txt'))
            serverSock.sendto(filesize,address)
                            
            bytesToSend = t.read(1024)
            serverSock.sendto(bytesToSend,address)
            while bytesToSend != "":
                bytesToSend = t.read(1024)
                serverSock.sendto(bytesToSend,address)
            t.close()
            
    if os.path.exists("tempfile.txt"):
        os.remove("tempfile.txt")

    else:
          print("The file does not exist")
    
    
def displayAll(c,file,serverSock,address):
    print "at all"
    with open(file,'rb') as f:
       file_data = f.read(1024)
       f.close()
    serverSock.sendto(file_data,address)
    
def deleteRecord(c,file,serverSock,address):
    print "at delete"
        
    idNum, c = serverSock.recvfrom(1024)
          
    with open(file, 'rt') as f:
        temp = open('tempfile.txt', 'wt')
        s = ' '
        while(s):
            s = f.readline()
            field = s.split("\t")
            if len(s) > 0:
                if (field[0]) != idNum:
                    temp.write(s)
    f.close()
    temp.close()
    
    with open('tempfile.txt','rb') as t:
           filesize = str(os.path.getsize('tempfile.txt'))
           serverSock.sendto(filesize,address)
                           
           bytesToSend = t.read(1024)
           serverSock.sendto(bytesToSend,address)
           while bytesToSend != "":
               bytesToSend = t.read(1024)
               serverSock.sendto(bytesToSend,address)
           t.close()
    
    if os.path.exists(file):
           os.remove(file)
    else:
        print("The file does not exist")
         
    if os.path.exists("tempfile.txt"):
           os.rename("tempfile.txt",file)
    else:
        print("The file does not exist")


def requests(serverSock,file,address):
    print "at reqs"
    
    msg,clientAddr = serverSock.recvfrom(1024)
    print msg
    if msg == 'ADD':
        add(clientAddr,file,serverSock)
    if msg == 'ID':
        displayID(clientAddr,file,serverSock,address)
    if msg == 'SCORE':
        displayScore(clientAddr,file,serverSock,address)
    if msg == 'ALL':
        displayAll(clientAddr,file,serverSock,address)
    if msg == 'RMV':
        deleteRecord(clientAddr,file,serverSock,address)
        
    
def main():
    
    UDP_IP = "127.0.0.1"
    UDP_PORT = 50000
    serverAddressPort = (UDP_IP, UDP_PORT)
    
    serverSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    serverSock.bind((UDP_IP,UDP_PORT))
    
    print "Server socket open:"
    
    while True:
        
        file, address = serverSock.recvfrom(1024)
        print 'Connection from', address
        '''
        t = threading.Thread(target=requests,args=("reqThread",serverSock,file))
        t.start()
        
       '''
        requests(serverSock,file,address)

    
    serverSock.close()

if __name__ == '__main__':
    main()
    
