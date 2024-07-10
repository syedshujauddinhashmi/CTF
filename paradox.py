import base64, hashlib, time

def xor_encrypt(data, key):
    key_length = len(key)
    return bytes((data[i] ^ key[i % key_length] for i in range(len(data))))


def level1_encrypt(data):
    key = hashlib.sha256("theycallmeeasy".encode()).digest()
    return xor_encrypt(data, key)


def level2_encrypt(data):
    key = hashlib.sha256("iamthemiddleone".encode()).digest()
    return xor_encrypt(data, key)


def level3_encrypt(data):
    key = hashlib.sha256("thinkofmeastheboss".encode()).digest()
    return xor_encrypt(data, key)


def encrypt(data):
    data = level1_encrypt(data)
    data = level2_encrypt(data)
    data = level3_encrypt(data)
    return base64.b64encode(data).decode()


def decrypt(data):
    print("[+] Getting the key")
    time.sleep(1)
    print("[+] Trying the key")
    time.sleep(2)
    print("[+] Finalizing the payload")
    time.sleep(1)
    print("[+] Producing output")
    time.sleep(2)
    return "You really thought It'll be this easy?\nDecrypt is broken and you can't do anything about that."


def mainParse error at or near `JUMP_LOOP' instruction at offset 210


if __name__ == "__main__":
    main()
