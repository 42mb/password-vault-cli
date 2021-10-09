import objdata
import json
import security as sec
import pickle


def saveto(class_list):
    plain_list = []

    #transform from object to list
    for obj in class_list:
        plain_list.append(obj.site)
        plain_list.append(obj.account)
        plain_list.append(obj.pw)
   
    encryptedList = sec.encrypt_list(plain_list)
 
    with open("data.txt", "wb") as fp:
        pickle.dump(encryptedList, fp)
       

def loadfrom():

      
    with open("data.txt", "rb") as fp:
        cryptedlist = pickle.load(fp)
        

    decrypted_parsed_list = []
    decrypted_parsed_list = sec.decrypt_list(cryptedlist) 
   
    #transform list into class objects
    parsed_list = []
    for obj in range(int(len(decrypted_parsed_list)/3.0)):
        site = decrypted_parsed_list[obj]
        account = decrypted_parsed_list[obj+1]
        pw = decrypted_parsed_list[obj+2]
        parsed_list.append( objdata.logindata(site, account, pw))#sure
         
    return parsed_list


def searchfrom(parsed_list, domainToBeFound):
    for obj in parsed_list:
        if(obj.site==domainToBeFound):
            resultlist = []
            resultlist.append(obj.account)
            resultlist.append(obj.pw)
            return resultlist
        else:
            print("not found")

