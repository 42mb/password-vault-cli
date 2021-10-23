import getpass
from pickle import TRUE
import sys
import objdata
import jasons
import security as sec
import clipboard
import pyperclip
import os
from subprocess import Popen, PIPE
from tkinter import Tk
import pandas as pd
import random


#################################################
#testing purpose RN
#input_domain = sec.gen_password(10) 
#input_username = sec.gen_password(13)
#input_pw = sec.gen_password(16)

#majorpw = "1234"
#firstload = True
#-n -l
#argv1 = "-newpw"
#argv2 = "xing"
#################################################

#print(len(sys.argv))
#print(sys.argv)


def confirmed_pw():
    userinputPassword = getpass.getpass('enter masterpassword: ')
    #normal mode: one line up
    #debug mode:  one line down
    #userinputPassword = majorpw

    if(sec.correct_hash(userinputPassword)):
        return True
    else:
        print("wrong password")
        return False
    

def copy2clipboard(pw):
    #pw = sec.gen_password()  
    p = Popen(['xsel','-bi'], stdin=PIPE)
    p.communicate(input=pw.encode())

def insert_new_data(argv_domain):
    #print("new data input with costum password")
    #argv1 ,argv2, argv3 
        #generel wanted input : argv1, argv2, argv3
        #                        -i    domain  name
    if(confirmed_pw()): 
        class_list = [] 
        
        input_domain = argv_domain[0]
        input_username = argv_domain[1]
        input_pw = getpass.getpass('enter password: ')
        class_list = jasons.loadfrom()
        class_list.append( objdata.logindata(input_domain, input_username, input_pw))
        jasons.saveto(class_list)   

            

def load_data(argv_domain):#output existing password
    #print("load data")
        #argv2 compare to domain in list, output of loginname, 
        #copy password to clipboard
    if(confirmed_pw()):
        data = jasons.loadfrom()
        print(argv_domain[0])
        domain = argv_domain[0]
        result = jasons.searchfrom(data, domain)#1 datalist, #searched obj
        if result:
            print(result[0])  #username
            #print(result[1]) #print pw
            copy2clipboard(result[1]) #pw to clipboard, output via strg+v
        else:
            print("not found")


def change_masterpassword():
    if(confirmed_pw()): 
        newpw = getpass.getpass("enter new masterpassword: ")
        controllInput = getpass.getpass("enter new masterpassword again: ")
        if(newpw == controllInput):
            sec.new_masterpassword(newpw)
        else:
            print("passwords are not the same")


#def change_password(): TODO


#def delete_datapoint(): TODO


def insert_generated_new_data(parsed_args):
    #print("import new data with generated pw copied to clipboard")
    if(confirmed_pw()):
        class_list = [] 
        input_domain = parsed_args[0]
        input_username = parsed_args[1]
        input_pw = sec.gen_password()
        class_list = jasons.loadfrom()
        class_list.append( objdata.logindata(input_domain, input_username, input_pw))
        jasons.saveto(class_list)
        copy2clipboard(input_pw)


