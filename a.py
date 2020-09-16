import json
import requests
import httplib2
from oauth2client import GOOGLE_REVOKE_URI, GOOGLE_TOKEN_URI, client
def reftok():
 CLIENT_ID = '1085699941843-nohpi0r2p1bs5if9sbmga4qp6gctl97u.apps.googleusercontent.com'
 CLIENT_SECRET = 'ymFlH6ZLp4L_2kyHX9FAL-fo'
 #1//04HkYrrQZm7d4CgYIARAAGAQSNwF-L9Ir_cHx4VQTFqG77D8gjW7-i94VjmCWR-nYStRL9EClLb6_2MQeYEVcrMTJ4FQ9X-T9mwI
 REFRESH_TOKEN = '1//04GTenNhyJONyCgYIARAAGAQSNwF-L9Iri5UMI9xMHfvfhXXkrBynD0B3319F6dynV_yYB178NxoU0N2vkS8pVhOb_zatIuhkvgQ'
 credentials = client.OAuth2Credentials(
 access_token=None,  # set access_token to None since we use a refresh token
 client_id=CLIENT_ID,
 client_secret=CLIENT_SECRET,
 refresh_token=REFRESH_TOKEN,
 token_expiry=None,
 token_uri=GOOGLE_TOKEN_URI,
 user_agent=None,
 revoke_uri=GOOGLE_REVOKE_URI)
 credentials.refresh(httplib2.Http())  # refresh the access token (optional)
 tok=credentials.to_json()
 http = credentials.authorize(httplib2.Http())  # apply the credentials
 idx=tok.index(', "client_id":')
 tok[18:idx-1]
 return tok[18:idx-1]
def up(fname,fdata,tokk):

 metadata = {
    "name": fname,
    "parents": ['1DP8YZZGBNnv5mIbHj8jgllGetWrYuK5a']
 }
 files = {
    'data': ('metadata', json.dumps(metadata), 'application/json'),
    'file': open(fdata, "rb").read()  # or  open(filedirectory, "rb")
 }
 r = requests.post(
 "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart&&supportsAllDrives=true",
 headers={"Authorization": "Bearer " + tokk},
 files=files
 )
 return r.text

from coincurve import PublicKey
from sha3 import keccak_256
import os
import time
start_time = time.time()
x=0
ff=str(x)+".txt"
file1=open(ff,"w")
mytok=reftok()
cont=0
okk=0
while True:
  a=(time.time() - start_time)
  a=int(a)
  if a>3500:
    mytok=reftok()
    start_time = time.time()
  x=x+1
  cont=cont+1
  private_key =x.to_bytes(32, byteorder='big')
  public_key = PublicKey.from_valid_secret(private_key).format(compressed=False)[1:]
  addr = keccak_256(public_key).digest()[-20:]
  addr=addr.hex()
  private_key=private_key.hex()
  s=str(addr)+" "+str(private_key)+" "
  file1.write(s)
  if cont>9891:
    file1.close()
    up(ff,ff,mytok)
    os.remove(ff)
    ff=str(x)+".txt"
    file1=open(ff,"w")
    cont=0
