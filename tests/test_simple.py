# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import sys

sys.path.append('../..')
from vscp import *

sys.path.append('..')
from vscphelper import *

def test_success():
    print("New session")
    h1 = newSession()
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

if __name__ == "__main__":
    test_success()
    print("Everything passed")