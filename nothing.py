

#   

#   
#   first opening json init for first input
#   #handle master pw HASH
#   argv handeling
#   closed console = closed program 
#   planned password change
#   planned delete object
#   planned error handeling 
##############################




def testen():
    print('')
    print("")
    list = ['fjslkdfjklsdf', 'fkjslfjsdlkjfieow', 'KDFJSEI', '3%!@KJDFIdkjf']
    testlist = ["xing", "blubb", "geheim", "blubb", "geheim", "blubb", "geheim", "blubb", "geheim", "blubb", "geheim", "blubb", "geheim", "blubb", "geheim", "blubb", "geheim", "blubb", "dom", "use", "1234567"]
    newlist = sec.encrypt_list(testlist);
    print(testlist)
    print('')
    print(newlist)
    new2list = sec.decrypt_list(newlist)
    print('')
    print(new2list)

#testen()
testlist1 = ["xing", "blubb", "geheim", "blubb", "geheim", "blubb", "geheim", "blubb", "geheim", "blubb", "geheim", "blubb", "geheim", "blubb", "geheim", "blubb", "geheim", "blubb", "dom", "use", "1234567"]


def testen2():
   # with open("app2.txt") as txtfile:
    #    txtfile.write(str(testlist1))
     #   txtfile.close()


###################################
    #loop to list elme, encrypt it, put it into newline of txt file
    #get lines out of txt file, decrypt, sav to list
###################################



    encryptedList = sec.encrypt_list(testlist1)
    encryptedString = "".join(str(encryptedList))
        #?del class_list
        #?del plain_list
    #print(encryptedList) 
    print('')
    print('')



    with open('app1.json', 'w') as f:
        #json.dump(plain_list, f)
        json.dump(encryptedList, f)
        #f.write(encryptedString)
        f.close()

    plain_list = []
    with open("app1.json") as jsonFile:
        plain_list = jsonFile.read()
        jsonFile.close()

    test_list = []
    test_list = sec.decrypt_list(plain_list)
    print(test_list)
    #print(plain_list)    
    #decrypted_parsed_list = []
    #decrypted_parsed_list = sec.decrypt_list(plain_list) 
    #print(plain_list)
    testss = []
    testss= plain_list
    print(testss)
    #nejrke = sec.decrypt_list(plain_list)
    #print(nejrke)

def testen3():
    
    encryptedd = sec.encrypt_list(testlist1)

    for i in encryptedd:
        #print(i)
        print("")


    with open("test.txt", "wb") as fp:   #Pickling
        pickle.dump(encryptedd, fp)
 
    with open("test.txt", "rb") as fp:   # Unpickling
        b = pickle.load(fp)
    
    #print(b)
    
    decrypted = sec.decrypt_list(b)
    print(decrypted)
    print("")
    print("")
    print("")
    print(testlist1)
testen3()