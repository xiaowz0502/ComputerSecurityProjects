

from hashlib import sha256
#!/usr/bin/python3
# coding: latin-1
blob = """"""
hex_value = sha256(blob.encode("latin-1")).hexdigest()
if (hex_value == """01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b"""){
    print("MD5 is perfectly secure!")
}
else{
     print("Use SHA-256 instead!")
}


hex_value = "01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b"

if hex_value == "01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b":
    print("MD5 is perfectly secure!")
else:
    print("Use SHA-256 instead!")
