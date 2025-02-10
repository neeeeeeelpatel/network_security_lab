#MonoAlphabetic Cipher
import string
import random

def genrate_key():
    alphabet = list(string.ascii_uppercase)
    shuff=alphabet.copy()
    random.shuffle(shuff)
    return dict(zip(alphabet,shuff))

def inv(keys):
    return {v:k for k,v in keys.items()}

def encry(text,key):
    cipher=[]
    for ch in text:
        if ch.upper() in key:
            cipher.append(key[ch.upper()])
        else:
            cipher.append(ch)
    return "".join(cipher)

def dencry(text,key):
    cipher=[]
    invertedkey= inv(key)
    for ch in text:
        if ch.upper() in invertedkey:
            cipher.append(key[ch.upper()])
        else:
            cipher.append(ch)
    return "".join(cipher)

generate=genrate_key()
print("Generated key = ",generate)
print("Encryption")
t=input("Enter Plain text")
e=encry(t,generate)
print("\nEncrypted text = ",e)
d=dencry(e,generate)
print("\nDecrypted tex = ",d)
