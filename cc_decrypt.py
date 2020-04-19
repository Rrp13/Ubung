#Function defination
def decrypt(cipher,step):
    result = ""
#Decrypiton
    for i in range(len(cipher)):
        char=cipher[i]
        if (char.isupper()):
            result += chr(((ord(char)-step-65)%26)+65)
        else:
            result += chr(((ord(char)-step-97)%26)+97)
    return result

# input text and step
cipher=input("Enter the Cipher to be Decripted?")

#Print decrypted text
for step in range (1,26):
    print("Step="+str(step))
    print("Encrypted Text is "+ decrypt(cipher,step))
    
Wub axgibwa vuks npxgwb