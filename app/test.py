import socket

HOST = 'localhost'  # Replace with your server's hostname or IP address
PORT = 4221  # Replace with your server's port number

def send_request():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b"GET / HTTP/1.1\r\nHost: localhost:4221\r\nUser-Agent: Python/3.9\r\nAccept-Encoding: gzip\r\n\r\n")
        data = s.recv(1024)
    return data

response = send_request()
print(response.decode())