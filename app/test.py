from app.libs.server.basicServer import Server

HOST = "localhost"  # Replace with your server's hostname or IP address
PORT = 4221  # Replace with your server's port number


server = Server()
request = b"GET / HTTP/1.1\r\nHost: localhost:4221\r\nUser-Agent: Python/3.9\r\nAccept-Encoding: gzip\r\n\r\n"
response = server.send_request(request)

print(response.decode())
