import socket

sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

host = "192.168.0.30"
port = 443

#Checks the value that is returned for the port
#result = sock.connect_ex((host, port))
#print(result)

def portScanner(port):
    if sock.connect_ex((host, port)):
        print("Port", port, "is closed")
    else:
        print("Port", port, "is open")

portScanner(port)

