#!/usr/bin/env python3
#some code from ChatGPT

import sys
import socket

try:
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
except (IndexError, ValueError):
    print(f'Usage: {sys.argv[0]} HOST PORT', file=sys.stderr)
    exit(1)


def main():
    # HOST = sys.argv[1]
    # PORT = int(sys.argv[2])
    # print(f'Connecting to {HOST}:{PORT}...')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        # data = b""
        #receieve bytes 

        while True:
            
            data = b''
            while len(data)<9:
                chunk = sock.recv(9 - len(data))
                print(chunk)
                if not chunk:
                    break
                data += chunk
            
            # if not data:
            #     break
            # data += one
        
        # print("done receiving")
            # print("done receiving, with data: ", data)

            if data[0] == ord('Q'):
                # print("this is a question")
                first = int.from_bytes(data[1:5], byteorder='big')
                second = int.from_bytes(data[5:9], byteorder='big')
                # print("first: ", first)
                # print("second: ", second)
                third = first + second
                sock.sendall(third.to_bytes(4, byteorder='big'))

            elif data[0] == ord('S'):
                # print("this is a secret answer")
                secret = data[1:].decode('utf-8')
                print(secret)
                break
            





if __name__ == '__main__':
    main()
