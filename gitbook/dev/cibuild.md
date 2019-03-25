# How to build with CI ?

### Clone the project
```
git clone https://github.com/hellstein/unix-socket-cs.git
```

### Make changes and doing development build
```
cd unix-socket-cs
```
* Make feature changes
* Doing development build and test

### Push and travis build
```
git tag [tag num]
git push origin [tag num]
```
The travis will build the package and upload it to [pypi](https://pypi.org/project/usocketgen/#history)

### Test the application
* Create test environment
```
pip3 install uscoketgen
mkdir testapp
```
* Create configuration
```
cd testapp
vim conf.json
```
where `conf.json` has the format as
```json
{
    "features": ["start", "stop", "install", "uninstall", "version", "status"]
}
```

* Create application
```
cd testapp
python3 -m usocketgen.genapp --conf conf.json --app app
```

* Start server in one terminal
```
cd testapp/app
python3 app_server.py
```

* Start client in another terminal
```
cd testapp/app
python3 app_client.py [cmd] 
```
* `cmd` is the cli command defined in `config.json`.
* You also can check by `python3 app_client.py -h`.




