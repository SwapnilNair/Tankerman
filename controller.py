from fastapi import FastAPI
import subprocess
from os import system
app = FastAPI()
import requests

@app.get("/create/{name}/{port}")
def create(name:str,port:int):
    #valid = subprocess.run(["docker", "run","--name",name,"-i","-p",str(port),":80","server"])
    #valid = system("docker run --name " + name + " -i -p "+str(port)+":80 server") 
    cmd_str = "docker run -d --name " + name + " -i -p "+str(port)+":80 server"
    valid = subprocess.run(cmd_str, shell=True)
    
    if(valid.returncode == 0):
        return ("Created a server named " + name + " serving port " + str(port))
    else:
        return("Server creation failed")

@app.get("/ls")
def ls():
    cmd_str = "docker ps -a --format json"
    valid = subprocess.check_output(cmd_str,shell=True)
    return (valid)

@app.get("/")
@app.get("/lsa")
def lsa():
    cmd_str = "docker ps --format json"
    valid = subprocess.check_output(cmd_str,shell=True)
    return (valid)

@app.get("/stop/{cid}")
def stop(cid:str):
    cmd_str = "docker stop " + cid
    valid = subprocess.run(cmd_str,shell=True)
    if(valid.returncode == 0):
        return ("Stopped server with id : " + cid)
    else:
        return("Could not stop server")

@app.get("/start/{cid}")
def start(cid:str):
    cmd_str = "docker start " + cid
    valid = subprocess.run(cmd_str,shell=True)
    if(valid.returncode == 0):
        return ("Started server with name/id : " + cid)
    else:
        return("Could not start server")

@app.get("/kill/{cid}")
def kill(cid:str):
    cmd_str = "docker rm " + cid
    valid = subprocess.run(cmd_str,shell=True)
    if(valid.returncode == 0):
        return ("Killed server with name/id : " + cid)
    else:
        return("Could not kill server")
@app.get("/killall")
def killall():
    cmd_str = "docker rm $(docker ps -a -q)"
    valid = subprocess.run(cmd_str,shell=True)
    if(valid.returncode == 0):
        return ("Killed all servers")
    else:
        return("Could not kill all servers")

@app.get("/stopall")
def stopall():
    cmd_str = "docker stop $(docker ps -a -q)"
    valid = subprocess.run(cmd_str,shell=True)
    if(valid.returncode == 0):
        return ("Stopped all servers")
    else:
        return("Could not stop all servers")

@app.get("/startall")
def startall():
    cmd_str = "docker start $(docker ps -a -q)"
    valid = subprocess.run(cmd_str,shell=True)
    if(valid.returncode == 0):
        return ("Started all servers")
    else:
        return("Could not start all servers")

@app.get("/rmall")
def rmall():
    cmd_str = "docker rm $(docker ps -a -q)"
    valid = subprocess.run(cmd_str,shell=True)
    if(valid.returncode == 0):
        return ("Removed all servers")
    else:
        return("Could not remove all servers")

@app.get("/rmi")
def rmi():
    cmd_str = "docker rmi $(docker images -q)"
    valid = subprocess.run(cmd_str,shell=True)
    if(valid.returncode == 0):
        return ("Removed all images")
    else:
        return("Could not remove all images")

#Get a specific container's logs
@app.get("/logs/{cid}")
def logs(cid:str):
    cmd_str = "docker logs " + cid
    valid = subprocess.check_output(cmd_str,shell=True)
    return (valid)

#Get all containers' logs
@app.get("/logs")
def logs():
    cmd_str = "docker logs $(docker ps -a -q)"
    valid = subprocess.check_output(cmd_str,shell=True)
    return (valid)

#Get a specific container's stats
@app.get("/stats/{cid}")
def stats(cid:str):
    cmd_str = "docker stats " + cid
    valid = subprocess.check_output(cmd_str,shell=True)
    return (valid)

@app.get("/get/{cid}")
def get(cid:str):
    try:
        cmd_str = "docker port " + cid
        valid = subprocess.check_output(cmd_str,shell=True)
        valid = valid.decode("utf-8")
        valid = valid.split(":")
        valid = valid[4].strip()
        output = requests.get("http://localhost:" + valid)
        return (output.text)
    except:
        return("Could not get port")





