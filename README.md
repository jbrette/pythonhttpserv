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

Stop the server
~~~
fg
CTRL C
~~~

## Packaging

Get into the simplistic application directory
~~~
cd app1
~~~

Package using setup.py. For interest time use sudo instead of --prefix
~~~
sudo python3 ./setup.py install

running install
Checking .pth file support in /usr/local/lib/python3.5/dist-packages/
/usr/bin/python3 -E -c pass
TEST PASSED: /usr/local/lib/python3.5/dist-packages/ appears to support .pth files
running bdist_egg
running egg_info
writing simplistic.egg-info/PKG-INFO
writing top-level names to simplistic.egg-info/top_level.txt
writing dependency_links to simplistic.egg-info/dependency_links.txt
writing entry points to simplistic.egg-info/entry_points.txt
reading manifest file 'simplistic.egg-info/SOURCES.txt'
writing manifest file 'simplistic.egg-info/SOURCES.txt'
installing library code to build/bdist.linux-x86_64/egg
running install_lib
running build_py
creating build/bdist.linux-x86_64/egg
creating build/bdist.linux-x86_64/egg/simplistic
copying build/lib/simplistic/simplisticHTTPServer.py -> build/bdist.linux-x86_64/egg/simplistic
copying build/lib/simplistic/__init__.py -> build/bdist.linux-x86_64/egg/simplistic
byte-compiling build/bdist.linux-x86_64/egg/simplistic/simplisticHTTPServer.py to simplisticHTTPServer.cpython-35.pyc
byte-compiling build/bdist.linux-x86_64/egg/simplistic/__init__.py to __init__.cpython-35.pyc
creating build/bdist.linux-x86_64/egg/EGG-INFO
copying simplistic.egg-info/PKG-INFO -> build/bdist.linux-x86_64/egg/EGG-INFO
copying simplistic.egg-info/SOURCES.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
copying simplistic.egg-info/dependency_links.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
copying simplistic.egg-info/entry_points.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
copying simplistic.egg-info/top_level.txt -> build/bdist.linux-x86_64/egg/EGG-INFO
zip_safe flag not set; analyzing archive contents...
creating 'dist/simplistic-0.1.0-py3.5.egg' and adding 'build/bdist.linux-x86_64/egg' to it
removing 'build/bdist.linux-x86_64/egg' (and everything under it)
Processing simplistic-0.1.0-py3.5.egg
Removing /usr/local/lib/python3.5/dist-packages/simplistic-0.1.0-py3.5.egg
Copying simplistic-0.1.0-py3.5.egg to /usr/local/lib/python3.5/dist-packages
simplistic 0.1.0 is already the active version in easy-install.pth
Installing simplistic script to /usr/local/bin

Installed /usr/local/lib/python3.5/dist-packages/simplistic-0.1.0-py3.5.egg
Processing dependencies for simplistic==0.1.0
Finished processing dependencies for simplistic==0.1.0
~~~

~~~
which simplistic

/usr/local/bin/simplistic
~~~

Run the service
~~~
simplistic &

starting server on port 9000
running server...
~~~

Test the server packaged using setup.py
~~~
curl -i http://localhost:9000

127.0.0.1 - - [02/Jul/2018 10:22:25] "GET / HTTP/1.1" 200 -
HTTP/1.0 200 OK
Server: BaseHTTP/0.6 Python/3.5.2
Date: Mon, 02 Jul 2018 15:22:25 GMT
Content-type: text/html

Hello world!
~~~

Stop the server
~~~
fg
CTRL C
~~~

## Links

[Link1](https://daanlenaerts.com/blog/2015/06/03/create-a-simple-http-server-with-python-3/)
