from coincurve import PublicKey
from sha3 import keccak_256
import os
f = open("addr.txt", "r")
s=f.read()
while True:
    private_key=keccak_256(os.urandom(128)).digest()
    public_key = PublicKey.from_valid_secret(private_key).format(compressed=False)[1:]
    addr = keccak_256(public_key).digest()[-20:]
    addr=addr.hex()
    private_key=private_key.hex()
    if addr in s:
     f=open("foooond.txt","a")
     f.write(" add: "+str(addr)+" pk "+str(private_key)+"\n")
     f.close()
     print (" add: "+str(addr)+" pk "+str(private_key)+"\n")
