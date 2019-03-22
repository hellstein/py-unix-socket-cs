[back to github](https://github.com/hellstein/unix-socket-cs)

# Usage scenarios
As a developer, you always account to create unix socket. The socket server implements some specified system features, which is running as a deamon process. You also need a socket client to request server to perform some tasks. You have already seen this pattern a lot, such as most database systems, e.g, `MySQL`, `MongoDB`, and most system deamons, e.g, `systemd`, `Docker`. 

It is a little bit boring to create such system from scratch, since plenty of work is spent on socket communication. It is the same idea that you would not create http server without any frameworks.

That is this project for, it is a framework written in python to create unix socket, as well as a code generator to create socket server and client code according to configuration.

# Architecture

