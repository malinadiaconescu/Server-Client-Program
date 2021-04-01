import socket
import threading

HEADER = 64
PORT = 8080
SERVER = socket.gethostbyname(socket.gethostname()) #iau ipv4 address
print(SERVER)
ADDR = (SERVER,PORT) #facem un tupple care contine serverul si portul
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "EXIT"


server = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #generez socket
server.bind(ADDR) #le leg


print("[STARTING]...Server is starting!")
def handle_client(conn,addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length: #tells the length of the message from the server that comes next
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}") #print address and the message sent

    conn.close()

def start():
    server.listen() #listening for new connections
    print(f"[LISTENING] Server is listenting on {SERVER}")
    while True:
        conn,addr = server.accept() #accept new connections,
        thread = threading.Thread(target=handle_client, args= (conn,addr))
        #pass info to handle client
        thread.start()
        print(f"[ACTIVE CONNECTIONS] { threading.activeCount()-1 } ")

print("[STARTING] Server is starting ... ")
start()