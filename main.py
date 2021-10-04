import objdata
import jasons
import inputhandler
import security as sec
import os, json
import pickle

########## TODO  ||!TODO  ##############

#   first opening routine
#   argv handeling
#   output into Clipboard
#   closed console = closed program 
#   planned password change/
#   planned delete object
#   planned error handeling 
#   planned list all domains
#   encrypt obj /w class fnc?
#   cleanup/garbage handeling in a secured way
#   testing

##############################

inputhandler.handle_input()

#sec.new_password("123")
#test = sec.correct_hash("1234")







###############################
#### testing for now:

testlist1 = ["xing", "blubb", "geheim", "blubb", "geheim", "blubb", "geheim", "blubb", "geheim", "blubb", "geheim", "blubb", "geheim", "blubb", "geheim", "blubb", "geheim", "blubb", "dom", "use", "1234567"]


## load, decrypt, print, encrypt, safe passwordlist
## for testing purpose
## TODO, auslagerung in testing.py


def test_restore_basic_datafile():
    
    #reset
    encryptedd = sec.encrypt_list(testlist1)

    #for reset
    #encryptedd = []

    #for reset
    with open("data.txt", "wb") as fp:   #Pickling
        pickle.dump(encryptedd, fp)
 
   
    with open("data.txt", "rb") as fp:   # Unpickling
        b = pickle.load(fp)
  
    
    decrypted = sec.decrypt_list(b)
    print(decrypted)
    print("")
    print("")
    print("")
    #print(testlist1)

def test_show_data():
  
    with open("data.txt", "rb") as fp:   # Unpickling
        b = pickle.load(fp)
    
    #print(b)
    
    decrypted = sec.decrypt_list(b)
    print(decrypted)
    print("")
    print("")
    print("")
    #print(testlist1)

#####################################################
#test_restore_basic_datafile()
#test_show_data()
#####################################################