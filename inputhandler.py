import getpass
import sys
import objdata
import jasons
import security as sec


#################################################
#testing purpose RN
input_domain = "domaainaa" 
input_username = "namua"
input_pw = "1234567"

majorpw = "1234"
firstload = True
#-n -l
argv1 = "-newpw"
argv2 = "xing"
#################################################

#print(len(sys.argv))
#print(sys.argv)


def confirmed_pw():
    #userinputPassword = getpass.getpass('enter password')

    #debug mode: TODO reinstate getpass one line up
    userinputPassword = majorpw
    #debug mode end

    #return sec.correct_hash(userinputPassword)
    return sec.correct_hash(userinputPassword)
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
    if(argv1 == "-newpw"):
        if(confirmed_pw): #TODO refractor!
            newpw = getpass.getpass("enter new password: ")
            newpwRepeat = getpass.getpass("enter new password again: ")
            if(newpw == newpwRepeat):
                sec.new_password(newpw)
            else:
                print("passwords are not the same")
                abort()
        else:
            print("wrong password")

