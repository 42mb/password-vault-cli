from tkinter.constants import TRUE
import objdata
import jasons
import inputhandler
import security as sec
import os, json
import testin
import pickle
import argparse


########## TODO || !TODO  ##############

#   first opening routine
#   argv ERROR handeling ARGV2 ARGV3

    #BUG list only expendable by one 
    #planned fix bei opening routine
    #load erkennt auch nicht neu hinzugefügte elemente (über safe)

#   handle empty data.txt
#   closed console = closed program 
#   planned domainpassword change
#   planned delete object
#   planned error handeling 
#   planned list all domains
#   planned testing
#   maybe encrypt obj /w class fnc?
#   maybe cleanup/garbage handeling in a secured way
#   maybe data cleanup? (memory überschreiben)
#   check duplicate

##############################

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--InsertNewInput", help = "Insert Dataset. Input: -i Domain Accountname", action = "store_true" )
parser.add_argument("-ig", "--InsertNewData_GeneratedPassword", help = "Insert Dataset. Password automatically generated. Input: -ig Domain Accountname", action = "store_true")
parser.add_argument("-l", "--loadData", help = "Load specific data. Input: -l Domain", action = "store_true")
parser.add_argument("-mp", "--newMasterPassword", help = "Change the Master Password of the program.", action = "store_true")
#parser.add_argument("-p", "--newPassword", help = "Change the Password of a Domain. (automaticly generated) Input: -p Domain", action = "store_true")
#parser.add_argument("-d", "--deleteDatapoint", help = "Deletes Domain/password/username. Input: -d Domain", action = "store_true")
parser.add_argument('parsed_args', nargs= "*", default = "", action = "store")
#parser.add_argument('parsed_domain', nargs ="*", action="store")
#parser.add_argument('parsed_username',nargs ="*", default = "", action="store") #TODO#errorhandeling here with argparse or with if statement within error_handle:
args = parser.parse_args()

def handle_input():
    print("Well met")
    if(args.InsertNewInput): 
        #input -NEW domain/name/password
        #argv1 ,argv2, argv3 
        #generel wanted input : argv1, argv2, argv3
        #                        -n    domain  name
        inputhandler.insert_new_data(args.parsed_args) 
        
    if(args.loadData): #load, maybe with lower(argv1) ?
        #argv2 compare to domain in list, output of loginname, 
        #copy password to clipboard
        inputhandler.load_data(args.parsed_args)
            
    if(args.newMasterPassword):
        inputhandler.change_masterpassword()
        
    if(args.InsertNewData_GeneratedPassword):
        inputhandler.insert_generated_new_data(args.parsed_args)
    
    #if(args.newPassword):
    #    inputhandler.change_password()

    #if(args.deleteDatapoint):
    #    inputhandler.delete_datapoint()
    #    usedJustOnce = False
   

#################
##init & run:
#################

    
handle_input()

#####################################################
### testing: 

#test_restore_basic_datafile()
#init_one_value_to_empty()
testin.test_show_data()

#sec.new_password("123")
#test = sec.correct_hash("1234")

#####################################################