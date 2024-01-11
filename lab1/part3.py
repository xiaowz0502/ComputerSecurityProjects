#!/usr/bin/env python3

from Crypto.Cipher import AES


class secret:
    def __repr__(self) -> str:
        encrypted = 'd0326fb8d0bfb1c5394991e7dcdf59b37889f2256772b8daad85dbeaff4483ed64cbb2b933d797bd530c8c92f57466d1c861c9f4931bc6631c38f375c64c40c4'
        return AES.new(b'\x00'*16, AES.MODE_ECB).decrypt(bytes.fromhex(encrypted)).decode()

    def __str__(self) -> str:
        return 'secret'


s = secret()


# Put the secret string you found in the debugger here!
secret_string = "388 rocks!"
