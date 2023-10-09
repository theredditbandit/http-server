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


def byte_parser(data: bytes):
    """
    Parse binary data

    Returns:
        str: decoded string
    """
    return data.decode()

def response_builder(code:int,body:str):
    ...

def response_handler(data: bytes) -> bytes:
    """Handles responses to TCP connections

    Args:
        data (bytes): data in bytes

    Returns:
        bytes: HTTP response
    """
    RESPONSE_MAP = {
        "status": {
            200: "HTTP/1.1 200 OK",
            404: "HTTP/1.1 404 Not Found",
        },
        "eof": "\r\n\r\n",
    }

    HTTP_HEADER_MAP = {"req_line": 0}
    data = data.split(b"\r\n")
    _, path, _ = data[
        HTTP_HEADER_MAP["req_line"]
    ].split()  # ['GET', '/index.html', 'HTTP/1.1']

    response:bytes = b""
    if byte_parser(path) == "/":
        response = RESPONSE_MAP["status"][200] + RESPONSE_MAP["eof"]
        response = response.encode()
    elif byte_parser(path) == "/echo":
        print("got echo")
    else:
        response = RESPONSE_MAP["status"][404] + RESPONSE_MAP["eof"] 
        response = response.encode()

    print("Responded with ", response)
    return response


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nShutting down server")
