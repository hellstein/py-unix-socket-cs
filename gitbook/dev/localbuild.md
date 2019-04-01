# How to build locally ?

### Clone the project
```
git clone https://github.com/hellstein/py-unix-socket-cs.git
```

### Install dependencies
* `python3`
* `pip3`

### Create python package for testing
```
cd py-unix-socket-cs
make update
```
* We use the PyPI repo for development, you can check `Makefile` to see the build and test process.
* If you need knowledge how the python package works, please do read [Packaging Python Projects](https://packaging.python.org/tutorials/packaging-projects/).
* The python package has been built and uploaded into [pypi.org](https://pypi.org/project/unixsocketcs/).

### Install package
```
make test
```

### Test the application
* Start server in one terminal
```
cd example
python3 app_server.py
```

* Start client in another terminal
```
cd example
python3 app_client.py [cmd] 
```
* `cmd` is the cli command defined in `testconfig.json`.
* You also can check by `python3 app_client.py -h`.
