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

    #three parts 
    middle = hashlib.sha256(message.encode()).hexdigest()
    head = "0001"+"FF"+"00"+"3031300d060960864801650304020105000420"
    end = "0"*201*2

    # integer_value = 255  # Replace this with your integer value
    # hex_string = hex(integer_value)

    # print(hex_string)

    
    result = head + middle + end
    # print(result)

    # turn hex to 
    integer_value = int(result, 16)
    pkcs, check = integer_nthroot(integer_value, 3)
    # print(pkcs)

    if check == True:
        hex_string = hex(pkcs)
        print(hex_string)
    else:
        ceiling 
        print("unable to check")
        
    
    
    





    #
    # TODO: Forge a signature
    #

    forged_signature = 0
    # print(bytes_to_base64(integer_to_bytes(forged_signature, 256)))


if __name__ == '__main__':
    main()
