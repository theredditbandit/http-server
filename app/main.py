from .libs.server import Server


def main():
    server = Server()
    data = server.listen()
    server.request_handler(data)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nShutting Down server")
