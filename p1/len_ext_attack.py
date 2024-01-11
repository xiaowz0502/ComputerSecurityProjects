#!/usr/bin/env python3

# Run me like this:
# $ python3 len_ext_attack.py "https://project1.eecs388.org/uniqname/lengthextension/api?token=...."
# or select "Length Extension" from the VS Code debugger

import sys
from urllib.parse import quote
from pysha256 import sha256, padding


class URL:
    def __init__(self, url: str):
        # prefix is the slice of the URL from "https://" to "token=", inclusive.
        self.prefix = url[:url.find('=') + 1]
        self.token = url[url.find('=') + 1:url.find('&')]
        # suffix starts at the first "command=" and goes to the end of the URL
        self.suffix = url[url.find('&') + 10:]

    def __str__(self) -> str:
        return f'{self.prefix}{self.token}&{self.suffix}'

    def __repr__(self) -> str:
        return f'{type(self).__name__}({str(self).__repr__()})'




def main():
    if len(sys.argv) < 2:
        print(f"usage: {sys.argv[0]} URL_TO_EXTEND", file=sys.stderr)
        sys.exit(-1)

    url = URL(sys.argv[1])
    print("url.prefix: ", url.prefix)
    print("url.tokken: ", url.token)
    print("url.surfix: ", url.suffix)

    #
    # TODO: Modify the URL
    #
    #url.suffix += '&command=UnlockSafes'
    
    extend = '~email=xiaowz@umich.edu79'.encode()  # .encode() converts str to bytes
    

    #8f36ee4a3885bcc8a8446b09e9498808c97667f0266e3641c5d2abca457f9187

    length = 8 + len(url.suffix.encode('ascii')) + 2
    padded_message_len = length + len(padding(length))


    h2 = sha256(
        state=bytes.fromhex(url.token),
        count=padded_message_len,
    )
    # x = extend.encode()  # .encode() converts str to bytes
    h2.update(extend)

    url.token = h2.hexdigest()


    url.suffix += ("13"+quote(padding(length)) +'~email=xiaowz@umich.edu')


    print(str(url))

    


if __name__ == '__main__':
    main()