#!/usr/bin/env python3

# Run me like this:
# $ python3 bleichenbacher.py "eecs388+uniqname+100.00"
# or select "Bleichenbacher" from the VS Code debugger

from roots import *

import hashlib
import sys


def main():
    if len(sys.argv) < 2:
        print(f"usage: {sys.argv[0]} MESSAGE", file=sys.stderr)
        sys.exit(-1)
    message = sys.argv[1]
    
    
    #
    # TODO: Forge a signature
    #

    # sig = 0x0001ff00

    # print("length of first sig:" , len(hex(sig)[2:]))

    # add ASN.1 3031300d060960864801650304020105000420
    sig = hex(0x0001ff003031300d060960864801650304020105000420)

    # print("length of sig", len(sig))

    # print("first sig:", sig)

    # hash the message to sha256
    message_hash = hashlib.sha256(message.encode("latin-1")).hexdigest()
    # print(len(message_hash))
    # print("message hash:", message_hash)
    
    # set the last 201 bytes to 0s
    sig += message_hash + hex(0x00)[2:] * 402

    # print("201:", hex(0x00)[2:] * 201)

    # print("hex sig:", sig)

    #change the sig to a hex number
    # sig = bytes_to_integer(sig)

    # take 3rd root of the sig
    forged_signature, check = integer_nthroot(int(sig, 16), 3)
    if check == True:
        print(bytes_to_base64(integer_to_bytes(forged_signature, 256)))
    else:
         print(bytes_to_base64(integer_to_bytes(forged_signature+1, 256)))

    # print("forged:", integer_nthroot(int(sig, 16), 3))
    # print("forged:", forged_signature)
    # print(bytes_to_base64(integer_to_bytes(forged_signature, 256)))


if __name__ == '__main__':
    main()
