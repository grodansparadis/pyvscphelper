# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import sys

sys.path.append('../..')
from vscp import *

sys.path.append('..')
from vscphelper import *

def test_connect():
    print("New session")
    h1 = newSession()
    assert h1 != 0
    print(h1)
    if (0 == h1 ):
        print("Failed to open new session")
    rv = open(h1,"192.168.1.7:9598","admin","secret")
    print("connected rv=",rv)
    close(h1)
    print("closed")
    assert True
    print("Close session")
    closeSession(h1)

def test_conversions():
    value = 3.14
    ba = float2ByteArray(value)
    print([ "0x%02x" % b for b in ba ])
    ba = double2ByteArray(value)
    print([ "0x%02x" % b for b in ba ])

if __name__ == "__main__":
    test_connect()
    test_conversions()
    print("Everything passed")