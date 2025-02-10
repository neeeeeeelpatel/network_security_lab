def ceaserCipher(st,k):
    cipher=''
    for char in st:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            cipher = cipher + chr((ord(char)+k -shift) %26+shift)
        else:
            cipher+=char
    return cipher

def dceaserCipher(st,k):
    dcipher=''
    for char in st:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            dcipher = dcipher + chr((ord(char)-k -shift) %26+shift)
        else:
            dcipher+=char
    return dcipher

st=str(input("Enter a plain text :"))
k=int(input("Enter the key value: "))
ciph=ceaserCipher(st,k)
dciph=dceaserCipher(ciph,k)
print(f'encyripted text is: {ciph}')
print(f'decripted text is: {dciph}')
