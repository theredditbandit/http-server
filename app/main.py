import socket


def main() -> None:
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)
    print("Server created!")
    print("Listening for a connection!")
    conn, addr = server_socket.accept()
    print("Connected by", addr)
    with conn:
        data: bytes = conn.recv(1024)
        print("Received data:\n", data.decode(), sep="\n")
        response = response_handler(data)
        conn.send(response)


def response_handler(data: bytes) -> bytes:
    """Handles responses to TCP connections

    Args:
        data (bytes): data in bytes

    Returns:
        bytes: HTTP response
    """
    RESPONSE_MAP = {200: b"HTTP/1.1 200 OK\r\n\r\n", 404: b"HTTP/1.1 404 Not Found\r\n\r\n"}

    httpm, path, httpv= data.strip().split()  # ['GET', '/index.html', 'HTTP/1.1']
    response = ""
    if path == "/":
        response = RESPONSE_MAP[200]
    else:
        response = RESPONSE_MAP[404]

    print("Responded with ", response)
    return response


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nShutting down server")
