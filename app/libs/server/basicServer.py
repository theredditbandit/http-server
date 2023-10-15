import asyncio
import socket
from asyncio.streams import StreamReader, StreamWriter

from ..static.fields import *


class Server:
    def __init__(self, host="localhost", port=4221):
        self.host = host
        self.port = port
        
    async def response_handler(self, request: bytes, writer: StreamWriter) -> bytes:
        """Builds and sends a response to http requests per the request.

        Args:
            data (bytes): Request data
        """
        request = request.split(DELIM.encode())
        _, resource, _ = request[
            HTTP_HEADER_MAP["req_line"]
        ].split()  # [b'GET', b'/index.html', b'HTTP/1.1']

        resource: str = resource.decode()
        if resource == "/":
            response = f"{RESPONSE_MAP['status'][200]}{EOF}"
        elif resource.startswith("/echo"):
            content = resource.split("/", maxsplit=2)[-1]
            response = f"{RESPONSE_MAP['status'][200]}{DELIM}Content-Type: text/plain{DELIM}\
                Content-Length: \{len(content)}{EOF}{content}"
        elif resource.startswith("/user-agent"):
            user_agent = request[HTTP_HEADER_MAP["User-Agent"]]
            _, content = user_agent.decode().split(":")
            content = content.strip()
            response = f"{RESPONSE_MAP['status'][200]}{DELIM}Content-Type: text/plain{DELIM}\
                Content-Length: {len(content)}{EOF}{content}"
        else:
            response = f"{RESPONSE_MAP['status'][404]}{EOF}"

        print(f"Response \n{response}")
        response = response.encode()
        writer.write(response)
        await writer.drain()
        writer.close()

    async def request_handler(self, reader: StreamReader, writer: StreamWriter):
        data: bytes = await reader.readuntil(EOF.encode())
        await self.response_handler(data, writer)

    async def start_server(self):
        server = await asyncio.start_server(
            self.request_handler, host=self.host, port=self.port
        )
        addr = server.sockets[0].getsockname()
        print(f"Serving on {addr}")
        async with server:
            await server.serve_forever()

    def send_request(self, request):
        """This is for testing the server
        Returns : response from server
        """
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            s.sendall(request)
            data = s.recv(1024)
        return data
