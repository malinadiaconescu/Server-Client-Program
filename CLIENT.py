import socket

HEADER = 64
PORT = 8080
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "EXIT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR) #instead of BIND, we CONNECT
print("Connected to server ip:"+SERVER)
print("Port:"+str(PORT))
def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length) #send length of message
    client.send(message) #send message

ok=True
while(ok==True):
    mess=input()
    if(mess==DISCONNECT_MESSAGE):
        ok=False
        send(DISCONNECT_MESSAGE)
        print("Disconnecting from the server...")
    else:
        send(mess)
        print("Message sent:" + mess)



