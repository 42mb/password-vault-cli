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
    #encryptedList = plain_list
    #print("save")
    #print(plain_list)
    with open("data/data.txt", "wb") as fp:
        pickle.dump(encryptedList, fp)
    fp.close   

def loadfrom():
      
    with open("data/data.txt", "rb") as fp:
        cryptedlist = pickle.load(fp)        
    fp.close

    decrypted_parsed_list = []
    decrypted_parsed_list = sec.decrypt_list(cryptedlist) 
    #decrypted_parsed_list = cryptedlist
    #transform list into class objects
    parsed_list = []
    
    for obj in range(0,(int(len(decrypted_parsed_list)/1.0)),3):###### OBJ PRO LOOP +3
        site = decrypted_parsed_list[obj]
        account = decrypted_parsed_list[obj+1]
        pw = decrypted_parsed_list[obj+2]
        parsed_list.append( objdata.logindata(site, account, pw))
    return parsed_list


def searchfrom(parsed_list, domainToBeFound):
    resultlist = []
    for obj in parsed_list:
        if(obj.site == domainToBeFound):
            #resultlist = []
            resultlist.append(obj.account)
            resultlist.append(obj.pw)
            #print(obj.account)
    return resultlist
    #print("not found")

