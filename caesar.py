import cs50
import sys

def main(argv):
   if ((len(sys.argv))!=2):
         print("Wrong!", end="")
         sys.exit

   else:
     key = int(sys.argv[1])
     print("plaintext: ")
     plainText = cs50.get_string()
     print("ciphertext: ")

     for letter in plainText: 
       if(letter.isalpha()):
           if(letter.isupper()):
               #ord gives the integer of a char and chr gives the string value of an integer
               text = (ord(letter) - ord('A'))
               ascii = (text + key)% 26;
               newText = chr(ascii + ord('A'))
               print(newText, end="")
           elif (letter.islower()):
               text = (ord(letter) - ord('a'))
               ascii = (text + key)% 26;
               newText = chr(ascii + ord('a'))
               print(newText, end="")
       else:
           print(letter, end= "")
   print("")
           

if __name__ == "__main__":
    main(argv ="2")             