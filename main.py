from tkinter.constants import TRUE
import objdata
import jasons
import inputhandler
import security as sec
import os, json
import pickle
import argparse


########## TODO || !TODO  ##############

#   first opening routine
#   argv handeling ARGV2 ARGV3 ARGV4

#   closed console = closed program 
#   planned domainpassword change
#   planned delete object
#   planned error handeling 
#   planned list all domains
#   planned testing
#   maybe encrypt obj /w class fnc?
#   maybe cleanup/garbage handeling in a secured way
#   maybe data cleanup? (memory überschreiben)

##############################

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--InsertNewInput", help = "Insert Dataset. Input: -i Domain Accountname", action = "store_true" )
parser.add_argument("-ig", "--InsertNewData_GeneratedPassword", help = "Insert Dataset. Password automaticle generated. Input: -ig Domain Accountname", action = "store_true")
parser.add_argument("-l", "--loadData", help = "Load specific data. Input: -l Domain", action = "store_true")
parser.add_argument("-mp", "--newMasterPassword", help = "Change the Master Password of the program.", action = "store_true")
#parser.add_argument("-p", "--newPassword", help = "Change the Password of a Domain. (automaticly generated) Input: -p Domain", action = "store_true")
#parser.add_argument("-d", "--deleteDatapoint", help = "Deletes Domain/password/username. Input: -d Domain", action = "store_true")
args = parser.parse_args()


def handle_input():
    print("Well met")
    if(args.InsertNewInput): #input -NEW domain/name/password
        #argv1 ,argv2, argv3 
        #generel wanted input : argv1, argv2, argv3
        #                        -n    domain  name
        inputhandler.insert_new_data() 
        
    if(args.loadData): #load, maybe with lower(argv1) ?
        #argv2 compare to domain in list, output of loginname, 
        #copy password to clipboard
        inputhandler.load_data()
            
    if(args.newMasterPassword):
        inputhandler.change_masterpassword()
        
    if(args.InsertNewData_GeneratedPassword):
        inputhandler.insert_generated_new_data()
    
    #if(args.newPassword):
    #    inputhandler.change_password()

    #if(args.deleteDatapoint):
    #    inputhandler.delete_datapoint()
    #    usedJustOnce = False
    else:
        print("get lost")
        print("u forgot argv? -h")

#################
##init & run:
#################     
handle_input()


#################




###############################
#### testing for now:

## load, decrypt, print, encrypt, safe passwordlist
## for testing purpose
## TODO, auslagerung in testing.py


def test_restore_basic_datafile(): #and output
    
    testlist1 = ["xing", "blubb", "geheim", 
                "acc1", "blubb", "geheim", 
                "acc2", "blubb", "geheim", 
                "acc3", "blubb", "geheim", 
                "acc4", "blubb", "geheim", 
                "acc5", "blubb", "geheim", 
                "acc6", "blubb", "geheim", 
                "acc7", "blubb", "geheim", 
                "acc8", "blubb", "gehiem", 
                "dom", "use", "1234567"]


    #reset to testlist
    encryptedd = sec.encrypt_list(testlist1)

    #for complete reset:
    #encryptedd = []

    #for reset
    with open("data.txt", "wb") as fp:   #Pickling
        pickle.dump(encryptedd, fp)
    fp.close
 
   
    with open("data.txt", "rb") as fp:   # Unpickling
        b = pickle.load(fp)
    fp.close

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
### uncommand if needed:
#test_restore_basic_datafile()
#test_show_data()


#sec.new_password("123")
#test = sec.correct_hash("1234")

#####################################################