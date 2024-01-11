#!/usr/bin/env python3

eecs388 = bytes([0x03, 0x08, 0x08])


def str_to_bytes(s: str) -> bytes:
    return s.encode(encoding="ascii")


def hex_to_bytes(s: str) -> bytes:
    return bytes.fromhex(s)


def int_to_bytes(n: int) -> bytes:
    length = 4
    return n.to_bytes(length, 'big')


def set_end_to_zero(b):
    if len(b) > 0:
        b[-1] = 0x00
    return


# Feel free to edit the main function however you like to help you debug, it won't be graded
#
# Run this script with the command: python3 part1.py
# or select "Part 1" from the VS Code debugger
def main():
    print(eecs388)

    bytes1 = str_to_bytes('Hello, world!')
    print(bytes1)

    bytes2 = hex_to_bytes('a2f295ac')
    print(bytes2)

    bytes3 = int_to_bytes(100599730)
    print(bytes3)

    b = bytearray(b'\x01\x02\x03\x04\x05')
    set_end_to_zero(b)
    print(b)


if __name__ == '__main__':
    main()
