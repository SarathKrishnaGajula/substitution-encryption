import CaesarCipher
import monoalphabeticcipher
import playfaircipher
import hillcipher
import vigenerecipher

def main():
    while(1):
     print('Choose from the following options:\n'
           'Press 0 for Caesar cipher\n'
           'Press 1 for Monoalphabetic cipher\n'
           'Press 2 for Playfair cipher\n'
           'Press 3 for Hill cipher\n'
           'Press 4 for polyalphavetic cipher\n'
           'Press any other number to exit!')
     option = int(input('Option: '))
     if(option>4):
         print('Thanks for using this module,if you find any bugs report them')
         break
     if(option==0):
      #print('here')
      CaesarCipher.main()
     elif(option==1):
      monoalphabeticcipher.main()
     elif(option==2):
      playfaircipher.main()
     elif(option==3):
      hillcipher.main()
     elif(option==4):
      vigenerecipher.main()


if __name__ == "__main__":
    main()