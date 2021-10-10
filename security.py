import rsa
import os
import bcrypt
import pickle
import string
import secrets
import random


def getPrivateKey():    
    with open('privateKK.pem', mode='rb') as privatefile:
        keydata = privatefile.read()
        privkey = rsa.PrivateKey.load_pkcs1(keydata)
       
    privatefile.close()
    return privkey


def getPublicKey():
    with open('publicKK.pem', mode='rb') as publicfile:
        keydata = publicfile.read()
        pubkey = rsa.PublicKey.load_pkcs1(keydata)
       
    publicfile.close()
    return pubkey


def encrypt_list(listToEncrypt):
    pubKey = getPublicKey()
    listEncrypted = []
    for elem in listToEncrypt:
        listEncrypted.append(rsa.encrypt(elem.encode(), pubKey))  
        
    return listEncrypted
    

def decrypt_list(listToDecrypt):
    privKey = getPrivateKey()
    listDecrypted = []
    for elem in listToDecrypt:
        listDecrypted.append(rsa.decrypt(elem, privKey).decode())
    privKey = 0

    return listDecrypted
    

def correct_hash(password):
    with open("hash.txt", "rb") as fp:   # Unpickling
        hashAndSalt = pickle.load(fp)
    #print(hashAndSalt)
    fp.close
    return bcrypt.checkpw(password.encode(), hashAndSalt)


def new_masterpassword(password):
    #print(password)
    hashAndSalt = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    #print(hashAndSalt)
    with open("hash.txt", "wb") as fp:   #Pickling
        pickle.dump(hashAndSalt, fp)
    fp.close


# to be sure to have at least 2(amount) of each (lower/uper/digit/punctuations)
# remaining spots will be filled randomly. Afterwards shuffeled.
def gen_password(length = 15):
    if (length<10):
        print('minimum length is set to 10')
        length = 10

    amount = 2;    
    password1 = "".join(secrets.choice(string.ascii_lowercase)for i in range(amount))
    password2 = "".join(secrets.choice(string.ascii_uppercase)for i in range(amount))
    password3 = "".join(secrets.choice(string.digits)for i in range(amount))
    password4 = "".join(secrets.choice(string.punctuation)for i in range(amount))
    password5 = "".join(secrets.choice(secrets.choice(string.ascii_letters + string.digits + string.punctuation))for i in range(length-4*amount))
    password = password1 + password2 + password3 + password4 + password5
    passwordlist = list(password)
    random.SystemRandom().shuffle(passwordlist)
    password = "".join(passwordlist)
    return password
