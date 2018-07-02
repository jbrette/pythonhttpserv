# Python HTTP Server
Simple Python Based HTTP Server

- Main goal is to create a simple Python3 based HTTP Server
- Second goal is to package the code in a way that will ease the installation in a container image

## Check python3 version

~~~
python3 --version

Python 3.5.2
~~~


## Simplistic HelloWorld project using Classical mode

First step is to create a simple code

Get into the simplistic application directory
~~~
cd app1
~~~

Verify the presence of the source code
~~~
ls simplistic/

__init__.py  simplisticHTTPServer.py
~~~

Let's run the simplistic application using the classical way
~~~
./simplistic/simplisticHTTPServer.py 9000 &
[1] 9198

starting server on port 9000
running server...
~~~

Test
~~~
curl -i http://localhost:9000

127.0.0.1 - - [02/Jul/2018 10:11:11] "GET / HTTP/1.1" 200 -
HTTP/1.0 200 OK
Server: BaseHTTP/0.6 Python/3.5.2
Date: Mon, 02 Jul 2018 15:11:11 GMT
Content-type: text/html

Hello world!
~~~

## Links

[Link1](https://daanlenaerts.com/blog/2015/06/03/create-a-simple-http-server-with-python-3/)
