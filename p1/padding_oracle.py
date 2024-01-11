#!/usr/bin/env python3

# Run me like this:
# $ python3 padding_oracle.py "https://project1.eecs388.org/uniqname/paddingoracle/verify" "5a7793d3..."
# or select "Padding Oracle" from the VS Code debugger

import copy
import json
import sys
import time
from typing import Dict, List
from Crypto.Cipher import AES

import requests



# Create one session for each oracle request to share. This allows the
# underlying connection to be re-used, which speeds up subsequent requests!
s = requests.session()


def oracle(url: str, messages: List[bytes]) -> List[Dict[str, str]]:
    while True:
        try:
            r = s.post(url, data={"message": [m.hex() for m in messages]})
            r.raise_for_status()
            return r.json()
        # Under heavy server load, your request might time out. If this happens,
        # the function will automatically retry in 10 seconds for you.
        except requests.exceptions.RequestException as e:
            sys.stderr.write(str(e))
            sys.stderr.write("\nRetrying in 10 seconds...\n")
            time.sleep(10)
            continue
        except json.JSONDecodeError as e:
            sys.stderr.write("It's possible that the oracle server is overloaded right now, or that provided URL is wrong.\n")
            sys.stderr.write("If this keeps happening, check the URL. Perhaps your uniqname is not set.\n")
            sys.stderr.write("Retrying in 10 seconds...\n\n")
            time.sleep(10)
            continue


def main():
    if len(sys.argv) != 3:
        print(f"usage: {sys.argv[0]} ORACLE_URL CIPHERTEXT_HEX", file=sys.stderr)
        sys.exit(-1)
    oracle_url, message = sys.argv[1], bytes.fromhex(sys.argv[2])

    if oracle(oracle_url, [message])[0]["status"] != "valid":
        print("Message invalid", file=sys.stderr)

    d_list = [0] * AES.block_size
    ciphertext = bytearray(message)
    pad_len = 0
    decrypted = ""

    # if len(ciphertext) % AES.block_size:
    #     raise Exception('invalid_length')
    # if len(ciphertext) < 2 * AES.block_size:
    #     raise Exception('invalid_iv')

    round  = int(len(ciphertext) / AES.block_size)
    
    temp = copy.deepcopy(ciphertext)
    
    iv = ciphertext[0:AES.block_size].hex()

    # decipher the first byte in the first block
    last_byte_list = []
    for i in range(256):
        n = round - 2
        byte = AES.block_size - 1
        temp[n * AES.block_size + byte] = i
        status = oracle(oracle_url, [temp])[0]["status"]

        if status == "invalid_mac" or status == "valid":
            p_mod = AES.block_size - byte
            c_mod = i
            c = ciphertext[n * AES.block_size + byte]
            last_byte_list.append({
                'status': status,
                'p_mod': p_mod,
                'c_mod': c_mod,
                'c': c,
                'p': p_mod ^ c ^ c_mod,
            })
            # p_mod = AES.block_size - byte
            # c_mod = i
            # c = ciphertext[n * AES.block_size + byte]
            # p = p_mod ^ c ^ c_mod

            # #check special case
            # if status == "valid" and p != 1:
            #     continue

            
            # print("cur plaintext:", decrypted)

            # print("pad_len:", pad_len)
            # break

    if len(last_byte_list) == 2:
        if last_byte_list[0]['status'] == "invalid_mac":
            p = last_byte_list[0]['p']
        else:
            p = last_byte_list[1]['p']
        decrypted = (p.to_bytes((p.bit_length() + 7) // 8, 'big')).hex() + decrypted
        pad_len = p
        d = p ^ c
        d_list[byte] = d
        pad_len = p
    elif len(last_byte_list) == 1:
        p = last_byte_list[0]['p']
        decrypted = (p.to_bytes((p.bit_length() + 7) // 8, 'big')).hex() + decrypted
        pad_len = p
        d = p ^ c
        d_list[byte] = d
        pad_len = p
    
    print("cur plaintext:", decrypted)
    print("pad_len:", pad_len)

    temp = copy.deepcopy(ciphertext)

    # decipher the rest of first block
    for byte in range(AES.block_size-2, -1, -1):
        n = round - 2
        for i in range(AES.block_size - 1, byte, -1):
            target = AES.block_size - byte
            temp[n * AES.block_size + i] = target ^ d_list[i]

        for i in range(256):
            temp[n * AES.block_size + byte] = i
                
            # send to server
            status = oracle(oracle_url, [temp])[0]["status"]
            
            if status == "invalid_mac"or status == "valid":
                if status == "valid" and byte > AES.block_size - pad_len:
                    continue
                if status == "invalid_mac" and byte == AES.block_size - pad_len:
                    continue
                p_mod = AES.block_size - byte
                c_mod = i
                c = ciphertext[n * AES.block_size + byte]
                p = p_mod ^ c ^ c_mod
                #(p.to_bytes((p.bit_length() + 7) // 8, 'big')).hex()
                decrypted = (p.to_bytes((p.bit_length() + 7) // 8, 'big')).hex() + decrypted
                d = p ^ c
                d_list[byte] = d
                print("in_mac:", "round:", n, ", byte:", byte, ", i:", i)
                print("cur plaintext:", decrypted)
                break
        temp = copy.deepcopy(ciphertext)

    ciphertext = ciphertext[0 : AES.block_size * (round - 1)]
    temp = copy.deepcopy(ciphertext)

    # decipher the rest of the blocks
    for n in range(round-3, -1, -1):
        # if round = 4, n -> 2, 1, 0
        # print("round: ", n)

        for byte in range(AES.block_size-1, -1, -1):
            # print("byte: ", byte)

            for i in range(AES.block_size - 1, byte, -1):
                target = AES.block_size - byte
                temp[n * AES.block_size + i] = target ^ d_list[i]

            for i in range(256):
                # modify the hex string
                # byte_value = bytes([i])
                temp[n * AES.block_size + byte] = i
                
                # send to server
                status = oracle(oracle_url, [temp])[0]["status"]
                
                if status == "invalid_mac"or status == "valid":
                    p_mod = AES.block_size - byte
                    c_mod = i
                    c = ciphertext[n * AES.block_size + byte]
                    p = p_mod ^ c ^ c_mod
                    decrypted = (p.to_bytes((p.bit_length() + 7) // 8, 'big')).hex() + decrypted
                    d = p ^ c
                    d_list[byte] = d
                    print("in_mac:", "round:", n, ", byte:", byte, ", i:", i)
                    print("cur plaintext:", decrypted)
                    break
                
            #recover temp to ciphertext
            #cipher text will lost block
            temp = copy.deepcopy(ciphertext)
        
        ciphertext = ciphertext[0 : AES.block_size * (n + 1)]
        temp = copy.deepcopy(ciphertext)  
       
    
    # decrypted = iv + decrypted
    # pad_len = 14
    # decrypted = "636172736f6e20736179732068656c6c6f2e206c6f6f6b20617420796f7520676f2120796f7527726520617765736f6d6521c519e8084b3e0318d53d05bed77b1041eaeb44de345c90a28df3ab6d6fa9c4ad0e0e0e0e0e0e0e0e0e0e0e0e0e0e"
    # print(decrypted[:len(decrypted) - pad_len * 2])
    
    # decrypted = copy.deepcopy(decrypted[0:len(decrypted) - (pad_len+32) * 2])
    # # print(decrypted)
    # decoded_text = bytes.fromhex(decrypted).decode('ascii', errors='ignore')

    # decrypted = iv + decrypted
    # hex_string = "58c7b1c356554755592df3e6c2a1619b636172736f6e20736179732068656c6c6f2e206c6f6f6b20617420796f7520676f2120796f7527726520617765736f6d6521c519e8084b3e0318d53d05bed77b1041eaeb44de345c90a28df3ab6d6fa9c4ad0e0e0e0e0e0e0e0e0e0e0e0e0e0e"
    byte_array = bytes.fromhex(decrypted)
    byte_array = byte_array[:len(byte_array) - (pad_len + 32 )]
    # decrypted = copy.deepcopy(decrypted[:len(decrypted) - pad_len * 2])
    # print(decrypted[:len(decrypted) - (pad_len + 32 )* 2])

    decoded_text = byte_array.decode('ascii', errors='ignore')
    print(decoded_text)



if __name__ == '__main__':
    main()