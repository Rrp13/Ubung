#Function defination
def encrypt(text,step):
    result = ""
#Encrypiton
    for i in range(len(text)):
        char=text[i]
        if (char.isupper()):
            result += chr(((ord(char)+step-65)%26)+65)
        else:
            result += chr(((ord(char)+step-97)%26)+97)
    return result

# input text and step
text=input("Enter the Text to be Encripted?")
step=int(input("Enter the step?"))
#Print Encrypted text
print("Encrypted Text is "+ encrypt(text,step))
