import socket

def main():

    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    print("Server created!")
    print("Listening for a connection!")
    conn , addr = server_socket.accept()
    print("Connected by",addr)
    with conn:
        data = conn.recv(1024)
        print("Received data:\n", data.decode())
        response = b"HTTP/1.1 200 OK\r\n\r\n"
        conn.send(response)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nShutting down server")
        
