import base64
import hashlib

def xor_dec(data, key):
    key_length = len(key)
    return bytes((data[i] ^ key[i % key_length] for i in range(len(data))))

def lvl1_dec(data):
    key = hashlib.sha256("theycallmeeasy".encode()).digest()
    return xor_dec(data, key)

def lvl2_dec(data):
    key = hashlib.sha256("iamthemiddleone".encode()).digest()
    return xor_dec(data, key)

def lvl3_dec(data):
    key = hashlib.sha256("thinkofmeastheboss".encode()).digest()
    return xor_dec(data, key)

def decrypt(data):
    data = base64.b64decode(data)
    data = lvl3_dec(data)
    data = lvl2_dec(data)
    data = lvl1_dec(data)
    return data

enc_data = "zJA8n3b1UraRcadADYaDybH6IjQ6QbPzuUjCfzzuC8fMn2/OPbE="

dec_data = decrypt(enc_data)
print(dec_data.decode())
