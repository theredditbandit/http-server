import socket
from .static.fields import *


class Server:
    def __init__(self, host="localhost", port=4221):
        self.host = host
        self.port = port
        print(f"Host :{host} and Port: {port}")
        self.server_socket = socket.create_server((host, port), reuse_port=True)
        print("Server Started!")

    def listen(self) -> bytes:
        """listen for a TCP connection on self.port

        Returns:
            bytes: The data received
        """
        print("Listening for connection on port ", self.port)
        self.conn, self.addr = self.server_socket.accept()
        print("Connected by", self.addr)
        data: bytes = self.conn.recv(1024)
        print("Received data:\n", data.decode(), sep="\n")
        return data

    def request_handler(self, request: bytes):
        """Builds and sends a response to http requests per the request.

        Args:
            data (bytes): Request data
        """
        request = request.split(DELIM)
        _, path, _ = request[
            HTTP_HEADER_MAP["req_line"]
        ].split()  # [b'GET', b'/index.html', b'HTTP/1.1']
        response = b""
        path = path.decode()
        if path == "/":
            response = RESPONSE_MAP["status"][200] + EOF
        elif path == "/echo":
            print("handling echo")
        else:
            response = RESPONSE_MAP["status"][404] + EOF

        response = response.encode()
        self.conn.send(response)

    def response_builder(self):
        ...

    def send_request(self, request):
        """This is for testing the server
        Returns : response from server
        """
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            s.sendall(request)
            data = s.recv(1024)
        return data

    def __del__(self):
        self.conn.close()
