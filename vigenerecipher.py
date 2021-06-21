#In this encryption we have different cipher combinations basesd on the plaintext and key
import numpy as np

def plain_text():
 plaintext = input("Enter the plain text: ")
 return plaintext
def key_input(plaintext):
 key = input("Enter the key: ")
 repkey = key*(len(plaintext)//len(key))
 for i in range(len(plaintext)%len(key)):
    repkey += key[i]
 print('key1: ',repkey)
 uniqkey = key
 if(len(plaintext)>len(key)):
    print('more')
 for i in range(len(plaintext)-len(key)):
    uniqkey += plaintext[i]
    #print(uniqkey)
    i+=1
 print('key2: ',uniqkey)
 return [repkey,uniqkey];

#encrypting the plaintext with both the ciphertext
def encrypt(plaintext,repkey,uniqkey):
 ciphertext1 = ""
 ciphertext2 = ""
 for i in range(len(plaintext)):
    ciphertext1 += chr((ord(plaintext[i])+ord(repkey[i])-194)%26+97)
    ciphertext2 += chr((ord(plaintext[i]) + ord(uniqkey[i]) - 194)%26+97)
    i+=1
 print('Ciphertext with repetition: ',ciphertext1)
 print('Ciphertext with replacement: ',ciphertext2)

def main():
     print('Welcome to polyalphabetic cipher here are the options you can perform: ')
     option = int(input('choose the option you want to perform: '))
     if (option == 0):
         plaintext = plain_text()
         repkey,uniqkey = key_input(plaintext)
         print(encrypt(plaintext, repkey,uniqkey))


