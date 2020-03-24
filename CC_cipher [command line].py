import string
import sys

def cipher(offset,text):
    mapping=generate_mapping(offset)
    return("".join(mapping.get(i,i)for i in text))
def generate_mapping(offset):
    return{**generate_partialmapping(offset,string.ascii_lowercase),
      **generate_partialmapping(offset,string.ascii_uppercase)}
def generate_partialmapping(offset,alphabet_string):
    if (sys.argv[1]=="encrypt"):
        return{
        char : alphabet_string[((offset+i)%26)]for i, char in enumerate(alphabet_string)
        }

    if (sys.argv[1]=="decrypt"):
        return{
        char : alphabet_string[((i-offset)%26)]for i, char in enumerate(alphabet_string)
        }
    

text=input("Enter Text ")
offset=int(input("Enter Offset "))
print(str(sys.argv[1])+"ed Text "+ cipher(offset,text))

