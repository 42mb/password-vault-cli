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
input_domain = sec.gen_password(10) 
input_username = sec.gen_password(13)
input_pw = sec.gen_password(16)

majorpw = "1234"
firstload = True
#-n -l
argv1 = "-newpw"
argv2 = "xing"
#################################################

#print(len(sys.argv))
#print(sys.argv)


def confirmed_pw():
    userinputPassword = getpass.getpass('enter password:')
    #normal mode: one line up
    #debug mode one line down
    #userinputPassword = majorpw
    #debug mode end
    #return sec.correct_hash(userinputPassword)
    if(sec.correct_hash(userinputPassword)):
        return True
    else:
        print("wrong password")
        return False
    
    #return bcrypt.checkpw(password.encode(), hashAndSalt)
    #hash pw
    #cmpare hashes
    #return True


def abort(): 
    exit()

def handle_input():
    print("Welcome to pwfault, flags: -n or -l or -newpw")
    #input new password
    if (argv1 == "-n"): #input -NEW domain/name/password
        #argv1 ,argv2, argv3 
        #generel wanted input : argv1, argv2, argv3
        #                        -n    domain  name
        if(confirmed_pw()): #hidden pw input WIP
            #plan loadin from clipboard
            class_list = [] 
            #later argv2,3 becoming input_domain, input_username
            domain_password = getpass.getpass('enter password')
            class_list = jasons.loadfrom()
            class_list.append( objdata.logindata(input_domain, input_username, input_pw))
            jasons.saveto(class_list)   
            #output existing password
    if(argv1 == "-l"): #load, maybe with lower(argv1) ?
        #argv2 compare to domain in list, output of loginname, 
        #copy password to clipboard
        if(confirmed_pw()):
            data = jasons.loadfrom()
            result = jasons.searchfrom(data, argv2)#argv2 = domainToFind
            print(result[0])
            print(result[1]) #WIP planned copy to clipboard/no visable output
            #import pandas as pd
            #df=pd.DataFrame(['Text to copy'])
            #df.to_clipboard(index=False,header=False)        
    if(argv1 == "-newpw"):
        if(confirmed_pw): #TODO refractor!
            newpw = getpass.getpass("enter new password: ")
            newpwRepeat = getpass.getpass("enter new password again: ")
            if(newpw == newpwRepeat):
                sec.new_password(newpw)
            else:
                print("passwords are not the same")
                abort()       
    if(argv1 == "-ng"):
        if(confirmed_pw):
            #plan loadin from clipboard
            class_list = [] 
            #later argv2,3 becoming input_domain, input_username
            domain_password = sec.gen_password()
            class_list = jasons.loadfrom()
            class_list.append( objdata.logindata(input_domain, input_username, input_pw))
            jasons.saveto(class_list)
            print(domain_password)

def copy2clipboard(pw):
    #pw = sec.gen_password()  
    p = Popen(['xsel','-bi'], stdin=PIPE)
    p.communicate(input=pw.encode())

def insert_new_data():
    print("new data input with costum password")
    #argv1 ,argv2, argv3 
        #generel wanted input : argv1, argv2, argv3
        #                        -n    domain  name
    if(confirmed_pw()): #hidden pw input WIP
        #plan loadin from clipboard
        class_list = [] 
            #later argv2,3 becoming input_domain, input_username
        input_pw = getpass.getpass('enter password')
        class_list = jasons.loadfrom()
        class_list.append( objdata.logindata(input_domain, input_username, input_pw))
        jasons.saveto(class_list)   

            #output existing password

def load_data():
    print("load data")
#argv2 compare to domain in list, output of loginname, 
        #copy password to clipboard
    if(confirmed_pw()):
        data = jasons.loadfrom()
        result = jasons.searchfrom(data, argv2)#argv2 = domainToFind
        print(result[0])
        #print(result[1]) #WIP planned copy to clipboard/no visable output
        copy2clipboard(result[1])

def change_masterpassword():
    if(confirmed_pw()): 
        newpw = getpass.getpass("enter new masterpassword: ")
        controllInput = getpass.getpass("enter new masterpassword again: ")
        if(newpw == controllInput):
            sec.new_masterpassword(newpw)
        else:
            print("passwords are not the same")
            abort()   


#def change_password(): TODO


#def delete_datapoint(): TODO


def insert_generated_new_data():
    print("import new data with generated pw copied to clipboard")
    if(confirmed_pw()):
        #plan loadin from clipboard
        class_list = [] 
        #later argv2,3 becoming input_domain, input_username
        input_pw = sec.gen_password()
        class_list = jasons.loadfrom()
        class_list.append( objdata.logindata(input_domain, input_username, input_pw))
        jasons.saveto(class_list)
        copy2clipboard(input_pw)


