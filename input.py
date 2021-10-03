import getpass
import sys

input_domain = ""
input_username = ""
intpu_pw = ""

print(len(sys.argv))
print(sys.argv)


pswd = getpass.getpass(' ')
print(pswd)

def confirmed_pw():
    passwd = getpass.getpass('')
    #hash pw
    #cmpare hashes
    return True


def handle_input():
    #input new pass
    if(argv.lower() == "-n"):
        #argv1 ,argv2, argv3 in abspeichern, pw extern abfragen        
    else:
        #exit
        print("exit")

    #output existing pass
    if(argv.lower() == "-g"):
        #argv1 aus liste suchen und name ausgeben und pw in clipboard
        if(confirmed_pw()):            
    else:
        #exit  
        print("exit") 


