#!/usr/bin/python3
# coding: latin-1
blob = """
                LxV �/ۼ�/������Oc]5YvA�����ϳ��.�l���;B>���.@vXF!�T��&k_�����Y���P&�\�ɷ)�D^�!� ��_H��5X蟈m���z���ڶONv�q��L�J
"""
from hashlib import sha256
print(sha256(blob.encode("latin-1")).hexdigest())
