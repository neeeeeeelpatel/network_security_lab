#Vigenere Cipher:

def generate_key(msg,key):
    key=list(key)
    if len(msg)==len(key):
         return"".join(key)
    else:
        for i in range(len(msg)-len(key)):
            key.append(key[i%len(key)])
        return"".join(key)

def encrypt_vigenere(msg,key):
    encrypted_text=[]
    key=generate_key(msg,key)
    for i in range(len(msg)):
        char=msg[i]
        if char.isupper():
            encrypted_char=chr((ord(char)+ord(key[i])-2*ord('A'))%26+ord('A'))
        elif char.islower():
            encrypted_char=chr((ord(char)+ord(key[i])-2*ord('a'))%26+ord('a'))
        else:
            encrypted_char=char
        encrypted_text.append(encrypted_char)
    return"".join(encrypted_text)

def decrypt_vigenere(msg,key):
    decrypted_text=[]
    key=generate_key(msg,key)
    for i in range(len(msg)):
        char=msg[i]
        if char.isupper():
            decrypted_char=chr((ord(char)-ord(key[i])+26)%26+ord('A'))
        elif char.islower():
            decrypted_char=chr((ord(char)-ord(key[i])+26)%26+ord('a'))
        else:
            decrypted_char=char
        decrypted_text.append(decrypted_char)
    return"".join(decrypted_text)

text_to_encrypt = input("enter the text to encrypt:")
key = input("enter the encryption key:")
encrypted_text=encrypt_vigenere(text_to_encrypt,key)
print(f"encrypted text: {encrypted_text}")
decrypted_text=decrypt_vigenere(encrypted_text,key)
print(f"decrypted text: {decrypted_text}")
