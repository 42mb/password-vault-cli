import getpass
import sys
import objdata
import jasons



#################################################
#testing purpose RN
input_domain = "domaainaa" 
input_username = "namua"
input_pw = "1234567"

majorpw = "1234"
firstload = True
#-n -l
argv1 = "-n"
argv2 = "xing"
#################################################

#print(len(sys.argv))
#print(sys.argv)


def confirmed_pw():
    passwd = getpass.getpass('enter password')
    #hash pw
    #cmpare hashes
    return True


def abort():
    exit()

def handle_input():
    print("-n or -l")
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
        else:
            abort()
            
            
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
        else:
            abort()
            
   
