#!/usr/bin/python3
# coding: latin-1
blob = """
                LxV �/ۼ�/�������c]5YvA�����ϳ��.�l���;B����.@vXF!�T�&k_�����Y���P&�\�ɷ)D^�!� ��_H��5X蟈m���z���ڶONv�q�IL�J
"""
from hashlib import sha256
hex_value = (sha256(blob.encode("latin-1")).hexdigest())
if hex_value == "5f4d74f2027053340a210a5fe4e207ad89045961d51626c1ea8cc19a043ac9a0":
    print("MD5 is perfectly secure!")
else:
    print("Use SHA-256 instead!")