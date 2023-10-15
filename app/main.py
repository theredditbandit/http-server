from .libs.server.basicServer import Server
import asyncio


def main():
    # while True:
    #     server = Server()
    #     data = server.listen()
    #     server.request_handler(data)
    server = Server()
    asyncio.run(server.start_server())


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nShutting Down server")
