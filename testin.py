import objdata
import jasons
import inputhandler
import security as sec
import os, json
import pickle
import argparse


###############################
#### testing for now:

## load, decrypt, print, encrypt, safe passwordlist
## for testing purpose


def test_restore_basic_datafile(): #and output
    
    testlist1 =["xing", "blubb", "geheim", 
                "xing", "blubb", "geheim", 
                "xincg", "blubb", "geheim", 
                "xineg", "blubb", "geheim", 
                "xinrg", "blubb", "geheim", 
                "xigng", "blubb", "geheim", 
                "xfing", "blubb", "geheim", 
                "x2ing", "blubb", "geheim", 
                "xinsg", "blubb", "gehiem", 
                "xidng", "usena", "pw123"]

    #print(testlist1)
    #reset to testlist
    encryptedd = sec.encrypt_list(testlist1)
    print(encryptedd)
    print("")
    
    #for reset
    with open("data.txt", "wb") as fp:   #Pickling
        pickle.dump(encryptedd, fp)
    fp.close
 
    
    with open("data.txt", "rb") as fp:   # Unpickling
        b = pickle.load(fp)
    fp.close
    print(b)
    print('')
    decrypted = sec.decrypt_list(b)
    print(decrypted)
    print("")
    print("")
    print("")
    #print(testlist1)

def test_show_data():
    b = []
    with open("data.txt", "rb") as fp:   # Unpickling
        b = pickle.load(fp)
    fp.close
    #print("")
    #print(b)
    
    decrypted = sec.decrypt_list(b)
    print(decrypted)
    #print("")
    #print("")
    print("")
    #print(testlist1)

def init_one_value_to_empty():
    testli = ['why111', 'boy111', '1234']
    with open("data.txt", "wb") as fp:
        pickle.dump(testli, fp)
    fp.close   

def debug_input_generated_newdata():
    test = ['test12', 'case12']
    inputhandler.insert_generated_new_data(test)

