# Using the library

There is a sample [here](https://github.com/grodansparadis/pyvscphelper/tree/main/tests) that uses most of the methods available in the library. 

**pyvscphelp** is the official Python helper library for VSCP & friends. It builds on the C helper library that has been available from the beginning of VSCP development. The library is normally used together with 

* [pyvscp](https://github.com/grodansparadis/pyvscp). The vscp library contains constants and VSCP event and filter structures and templates.
* [pyvscpclasses](https://github.com/grodansparadis/pyvscpclasses). The vscp_class library contains VSCP class definitions. 
* [pyvscptypes](https://github.com/grodansparadis/pyvscptypes). The vscp_type library contains VSCP type definitions. 

There are also other Python related VSCP libraries and you find a list [here](https://github.com/search?q=user%3Agrodansparadis+pyvscp)


Example
```python
# Constants from the vscp library
vscpclass = vscp.CLASS1_SECURITY
vscptype = vscp.VSCP_TYPE_PROTOCOL_GENERAL
errcode = VSCP_ERROR_SUCCESS

# Helper
h1 = vhlp.newsession()
if (0 == h1 ):
    vhlp.closesession(h1)
    raise ValueError('Unable to open vscphelp library session')
```

## Prerequisites

To use the vscphelper library you first need to install the binary vscp helper library. This library is available for Linux and Windows. You find install and build instructions in the documentation for the library [here](https://docs.vscp.org/#vscphelper).

## Install on Linux

The pyvscphelper module is available on PyPi. Install it from PyPi is the easiest way to obtain the module. To install it on your machine use

```bash
pip3 install pyvscphelper
```
To install in a virtual environment in your current project:

mkdir project-name && cd project-name
python3 -m venv .env
source .env/bin/activate
pip3 install pyvscphelper

In both cases pyvscp, pyvscpclasses and pyvscptypes will also be installed.


Upgrade with

```bash
pip3 install --upgrade pyvscphelper
```

## Install on Windows

On windows run 

```bash
cmd
```

as administrator and use

```bash
python -m pip install pyvscphelper
```

to install the library.

On GitHub you can find the code at (https://github.com/grodansparadis/pyvscphelper)

pyvscp, pyvscpclasses and pyvscptypes libraries will also be installed.

## To use in a (new) project

```python
import vscphelper 
```

is the standard way to im,port the library. This measn that you have to prefix every function in the library with "vscphelper". It may be better to use

```python
import vscphelper as vhlp
```

to get a shorter prefix "vhlp". You can use any combination you like of course. 

Normally you also need the vscp library as well so the full import is

```python
import vscp
import vscphelper as vhlp
```

or if you want symbolic VSCP classes and types

```python
import vscp
import vscp_class as vc
import vscp_type as vt
import vscphelper as vhlp
```

## Initializing the project

You must initialize a new session before you can use the vscphelper library. This session also must be ended when you are finished with your use of the library.

* [newsession]() starts a new session
* [closesession]() ends a session

[filename](./bottom_copyright.md ':include')