# How to set development environment ?

### Clone the project
```
git clone https://github.com/hellstein/unix-socket-cs.git
```

### Install dependencies
* `python3`
* `pip3`

### Create python package for testing
```
cd unix-socket-cs
make update
```

### Generate unix socket applcation
```
make test
```
The application `app` is generated according to `testconfig.json`.

### Test the application
* Start server in one terminal
```
cd app
python3 app_server.py
```

* Start client in another terminal
```
cd app
python3 app_client.py
```
