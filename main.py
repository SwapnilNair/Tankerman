from typing import Union
from fastapi import FastAPI
import socket
import platform
from uuid import uuid4

rand_token = uuid4()
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)


no_open = 1
no_close = 0

machine = platform.machine()
version = platform.version()
plat = platform.platform()
uname = platform.uname()
system = platform.system()
proc = platform.processor()


app = FastAPI()

@app.get("/")
def home():
    return {"ip" : IPAddr,
            "hostname":hostname,
            "number_open_conns":no_open,
            "number_closed_conns":no_close,
            "token":rand_token,
            "machine" : machine,
            "version" : version,
            "platform" : plat,
            "uname" : uname,
            "system" : system,
            "processor" : proc
            }


@app.get("/item/{id}")
def get_item(id:int,q: Union[str,None] = None):
    return{"The ID is " : id,"q":q}

@app.get("/ping")
def ping():
    return {"ping successful"}



 
