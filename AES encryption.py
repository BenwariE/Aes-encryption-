import random
import string
from Cryptodome.Cipher import AES
from crypto.Cipher import AES
from crypto.Util.Padding import pad, unpad

def encrypt_data(plaintext, key, iv):
    cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv.encode('utf-8'))
    padded_plaintext = pad(plaintext.encode('utf-8'), AES.block_size)
    ciphertext = cipher.encrypt(padded_plaintext)
    return print_output(ciphertext)

def decrypt_data(ciphertext, key, iv):
    decipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv.encode('utf-8'))
    decrypted_plaintext = decipher.decrypt(ciphertext)
    unpadded_plaintext = unpad(decrypted_plaintext, AES.block_size)
    return print(f'plain text is {unpadded_plaintext.decode('utf-8')}')
def input_string():
    print('do you have cyper text')
    ans = input('type y for cyphertext and n for plaintext: ')
    if ans == 'y':
        ciphertext = input('enter your text')
        key = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(32))
        iv = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(16))
        return decrypt_data(ciphertext, key, iv)
    elif ans == 'n':
        plaintext = input('enter your text')
        key = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(32))
        iv = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(16))
        return encrypt_data(plaintext, key, iv)
    else: 
        print('wrong letter')
def print_output(ciphertext):
    print(f'cipher text is{ciphertext}')


input_string()