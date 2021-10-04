import rsa
import os
import bcrypt
import pickle


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
    return bcrypt.checkpw(password.encode(), hashAndSalt)


def new_password(password):
    #print(password)
    hashAndSalt = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    #print(hashAndSalt)
    with open("hash.txt", "wb") as fp:   #Pickling
        pickle.dump(hashAndSalt, fp)
