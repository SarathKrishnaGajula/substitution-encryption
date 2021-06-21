#In this encryption Key is a nxn matrix where n is the block size for given plaintext
import numpy as np

def plain_text():
 plaintext = input("Enter the plain text: ").replace(" ","").lower()
 return plaintext
def key_input(plaintext):
 while(1):
  block_size = int(input('Enter the key dimension: '))
  if(len(plaintext)%block_size!=0):
     print("Please make sure the key dimension is a divisor of ",len(plaintext))
  else: break
 key = np.zeros((block_size,block_size))
 print(key)
 for i in range(block_size):
    for j in range(block_size):
        key[i][j] = ord(input("Enter the value for index ["+str(i)+']['+str(j)+']:'))-97

 print("Heres the key:\n",key)
 return key

#Encrypting using the key
def encrypt(plaintext,key):
 ciphertext = ""
 for i in range(len(plaintext)-len(key)+1):
    block = np.zeros((len(key),1))
    for j in range(len(key)):
        print(plaintext[i])
        block[j][0] = ord(plaintext[i])-97
        i+=1
    cross = np.dot(key,block)
    print(cross)
    for col in cross:
        ciphertext+=chr(((((col%26)+ 26)%97) % 26)+97)
 print("Cipher text is: ",ciphertext)
 return ciphertext

def main():
    print('Welcome to hill cipher here are the options you can perform: ')
    option = int(input('choose the option you want to perform: '))
    if (option == 0):
        plaintext = plain_text()
        key = key_input(plaintext)
        print(encrypt(plaintext, key))