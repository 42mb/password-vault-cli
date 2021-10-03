from os import close
import rsa
# Use at least 2048 bit keys nowadays, see e.g. https://www.keylength.com/en/4/
(publicKey, privateKey) = rsa.newkeys(2048) 


 
d = open('privateKey.pem', 'wb')
d.write(privateKey.save_pkcs1(format = "PEM"))
d.close()
 
 
f = open('publicKey.pem', 'wb') 
f.write(publicKey.save_pkcs1(format = "PEM"))
f.close()




