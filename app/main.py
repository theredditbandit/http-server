import argparse
import asyncio

from .libs.server.basicServer import Server


def main():
    server = Server()
    asyncio.run(server.start_server())


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nShutting Down server")
