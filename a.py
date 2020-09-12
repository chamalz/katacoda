from coincurve import PublicKey
from sha3 import keccak_256
import sys
import time
cnt=5456454654546
i=0
start_time = time.time()
while i<1000000:
    private_key =cnt.to_bytes(32, byteorder='big')
    public_key = PublicKey.from_valid_secret(private_key).format(compressed=False)[1:]
    addr = keccak_256(public_key).digest()[-20:]
    addr=addr.hex()
    private_key=private_key.hex()
    cnt=cnt+1
    i=i+1
    if addr==str("hgjhgjhghjg"):
     s=private_key+" : "+addr
f=open("a.txt","a")
f.write(str((time.time() - start_time))+" add: "+addr)
f.close()
