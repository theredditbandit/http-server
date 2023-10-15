import argparse
import asyncio

from .libs.server.basicServer import Server


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--directory", help="Path to directory")
    args = parser.parse_args()
    server = Server(directory=args.directory)
    asyncio.run(server.start_server())


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nShutting Down server")
