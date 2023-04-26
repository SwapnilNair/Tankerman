# Tankerman
A FastAPI controller for orchestrating docker containers remotely.

## Setting up
```
pip install -r requirements.txt
```


## Running
```
python3 tankerman <flags>
```

>flags
  - ```-H : Host ip```
  - ```-P : Host port```
  - ```-R : Reload watch```

Go to ```http://<host>:<port>/docs``` to access the controller interface.
