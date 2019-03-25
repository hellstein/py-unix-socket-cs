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
Refer to [Quick Start](../qs/deployment.md)
