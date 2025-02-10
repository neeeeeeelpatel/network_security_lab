#Playfair Cipher

def playfair_mat(key):
    alpha= "ABCDEFGHIKLMNOPQRSTUVWXYZ"  
    matrix=[]
    key="".join(dict.fromkeys(key.upper().replace("J","I")+alpha))  
    for i in range(0, 25, 5):
        matrix.append(list(key[i:i+5]))
    return matrix

def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
            
            
def playfair_encrypt(plaintext, key):
    matrix = playfair_mat(key)
    plaintext = plaintext.upper().replace("J", "I").replace(" ", "")
    if len(plaintext) % 2 != 0:
        plaintext += "X"
        
    ciphertext = ""
    for i in range(0, len(plaintext), 2):
            a, b = plaintext[i], plaintext[i + 1]
            row1, col1 = find_position(matrix, a)
            row2, col2 = find_position(matrix, b)
            if row1 == row2:
                ciphertext += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:
                ciphertext += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
            else:
                ciphertext += matrix[row1][col2] + matrix[row2][col1]
    return ciphertext

def playfair_decrypt(ciphertext, key):
    matrix = playfair_mat(key)
    plaintext = ""
    
    for i in range(0, len(ciphertext), 2):
        a, b = ciphertext[i], ciphertext[i + 1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)
        if row1 == row2:
            plaintext += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            plaintext += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else:
            plaintext += matrix[row1][col2] + matrix[row2][col1]
    return plaintext



plaintext = input("Enter a plain text: ")
key = input("Enter a key: ")


encrypted_text = playfair_encrypt(plaintext, key)
print("Encrypted:", encrypted_text)

decrypted_text = playfair_decrypt(encrypted_text, key)
print("Decrypted:", decrypted_text)