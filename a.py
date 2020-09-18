import json
import requests
import httplib2
from oauth2client import GOOGLE_REVOKE_URI, GOOGLE_TOKEN_URI, client
def reftok():
 CLIENT_ID = '261435301533-sqbteigq4bbi0c86v9lsg51fcgacqfkk.apps.googleusercontent.com'
 CLIENT_SECRET = 'i9G5pyl7gd8T8cFiK6jpg--v'
 
 REFRESH_TOKEN = '1//04CqM2a2N8_YeCgYIARAAGAQSNwF-L9IrVVdIKDl37oTl6XV8ErW7cpZN28LK2MkrnE66pk9YyK_Ye69PL3ASzip1OcQf5Uk-l_k'
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
    "parents": ['1msGmKqRLBMfkjHF57o1M2EfQJ4zhBzP2']
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
ff="rnddd.txt"
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
  cont=cont+1
  private_key =os.urandom(32)
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
    ff=str(private_key)+"RND.txt"
    file1=open(ff,"w")
    cont=0
