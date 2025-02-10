#Hill Cipher

import numpy as np

def hill_cipher_encrypt(plaintext, key_matrix):
    n = len(key_matrix)
    plaintext = plaintext.upper().replace(" ", "")
    
    original_length=len(plaintext)
    
    if len(plaintext) % n != 0:
        plaintext += "X" * (n - len(plaintext) % n)

    plaintext_vector = [ord(char) - ord('A') for char in plaintext]
    ciphertext = ""
    for i in range(0, len(plaintext_vector), n):
        block = plaintext_vector[i:i + n]
        result = np.dot(key_matrix, block) % 26
        ciphertext += "".join(chr(num + ord('A')) for num in result)
    return ciphertext,original_length

def hill_cipher_decrypt(ciphertext,key_matrix,original_length):
    n=len(key_matrix)
    key_matrix_inv=mod_inverse_matrix(key_matrix,26)
        
    ciphertext_vector=[ord(char)-ord('A') for char in ciphertext]
    plaintext=""
        
    for i in range(0,len(ciphertext_vector),n):
        block=ciphertext_vector[i:i+n]
        result=np.dot(key_matrix_inv,block)%26
        plaintext+="".join(chr(num+ord('A')) for num in result)
            
    return plaintext[:original_length]
        
def mod_inverse_matrix(matrix,mod):
    determinant=int(round(np.linalg.det(matrix)))
    determinant_inv=pow(determinant,-1,mod)
    adjugate_matrix=np.round(determinant*np.linalg.inv(matrix)).astype(int)%mod
    inverse_matrix=(determinant_inv*adjugate_matrix)%mod
    
    return inverse_matrix

plaintext = input("Enter the text to be encrypted : ")
key_matrix = np.array([[6, 24, 1], [13, 16, 10], [20, 17, 15]])  

ciphertext,original_length=hill_cipher_encrypt(plaintext, key_matrix)
print("Encrypted:",ciphertext)

decryptedtext=hill_cipher_decrypt(ciphertext,key_matrix,original_length)
print("Decrypted:",decryptedtext)
