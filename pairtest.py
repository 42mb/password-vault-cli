import objdata
import jasons
import inputhandler
import security as sec
import os, json
import pickle

########## TODO  ||!TODO  ##############

#   first opening json init for first input
#   #handle master pw HASH
#   argv handeling
#   closed console = closed program 
#   planned password change
#   planned delete object
#   planned error handeling 
#   planned list all domains
#   testing

##############################






testlist1 = ["xing", "blubb", "geheim", "blubb", "geheim", "blubb", "geheim", "blubb", "geheim", "blubb", "geheim", "blubb", "geheim", "blubb", "geheim", "blubb", "geheim", "blubb", "dom", "use", "1234567"]


## load, decrypt, print, encrypt, safe passwordlist
## for testing purpose
## TODO, auslagerung in testing.py
def testen3():
    
    #reset
    encryptedd = sec.encrypt_list(testlist1)

    #encryptedd = []


#    with open("test.txt", "wb") as fp:   #Pickling
 #       pickle.dump(encryptedd, fp)
 
   

    with open("test.txt", "rb") as fp:   # Unpickling
        b = pickle.load(fp)
    
    #print(b)
    
    decrypted = sec.decrypt_list(b)
    print(decrypted)
    print("")
    print("")
    print("")
    #print(testlist1)



inputhandler.handle_input()
#testen3()