import socket
from libs.responses import RESPONSE
def main() -> None:
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    print("Server created!")
    print("Listening for a connection!")
    conn , addr = server_socket.accept()
    print("Connected by",addr)
    with conn:
        data:bytes = conn.recv(1024)
        print("Received data:\n", data.decode(),sep='\n')
        response = response_handler(data)
        conn.send(response)

def response_handler(data: bytes) -> bytes:
    return RESPONSE[200]

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nShutting down server")
        
