# flask_srv_ui_webpage
backend Python server with flask and webpage for user interface

## Activation
The server is set to run on localhost port 4567
type `localhost:4567`in your browser to access the user interface
if you want to run he server elsewhere, replace `localhost` with ip adress

# To be able to run `flask_server.py`you should install pip and virtualenv
```
sudo apt-get install python-pip
sudo pip install virtualenv
```
then create a directory called `virtual` and activate the virtualenvironment:
```
mkdir virtual
virtualenv virtual
source virtual/bin/activate
```

Once you are running into to virtualenv you can install needed packages and run the server:
```
pip install flask

python flask_server.py
```

