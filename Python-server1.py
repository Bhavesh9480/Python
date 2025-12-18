#Python scoket Programming 
#server side 1
#imporitng socket module to makeing the connection
import socket
import sys #to access command line in computer

#create a socket
def create_socket():
    try:
        global host
        global port 
        global s 
        host="0.0.0.0"
        port=9999
        s=socket.socket()
    except socket.error as msg:
        print("Socket creation error :"+str(msg))


 #Binding the socket and listning for connection
def bind_socket():
    try:
        global host
        global port 
        global s 

        print("Binding the port : "+str(port))
        s.bind((host,port))
        s.listen(5)

    except socket.error as msg:
        print("Socket binding error :"+str(msg)+"\n"+"Retrying...")
        bind_socket()

#Establish connection with a clinet (Socket is listning)

def socket_accept():
    while True:
        conn,address=s.accept()
        print("Connection has been established | "+"IP : "+address[0] + " | " + "Port "+str(address[1]))
        send_command(conn)
    conn.close()

#Give defination for "send_command" function
def send_command(conn):
    while True:
        cmd=input()
        if cmd=='quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd))>0:
            conn.send(str.encode(cmd))
            clinet_response=str(conn.recv(1024),"utf-8")
            print(clinet_response, end="")

#Now creating a main function to call the above functions
def main():
    create_socket()
    bind_socket()
    socket_accept()

main()




        