# FILE: vscphelper.py
#
# VSCP UDP functionality
#
# This file is part of the VSCP (http://www.vscp.org)
#
# The MIT License (MIT)
#
# Copyright (c) 2000-2020 Ake Hedman, Grodans Paradis AB <info@grodansparadis.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
from ctypes import *
import _ctypes
import vscp 


if os.name == "nt":
    lib = cdll.LoadLibrary('libvscphelper.dll')
else:
    lib = cdll.LoadLibrary('libvscphelper.so')    

###############################################################################
# newSession
#

def newSession():
    lib.vscphlp_newSession.restype = c_long
    handle = lib.vscphlp_newSession()
    return handle

###############################################################################
# closeSession
#

def closeSession( handle ):
    print("A")
    lib.vscphlp_closeSession( c_long(handle) )
    print("B")
    _ctypes.dlclose(lib._handle) 
    print("C")
    # Is this needed?
    # if os.name == "nt":
    #     _ctypes.FreeLibrary(lib1._handle)
    # else:    
    #     _ctypes.dlclose(lib._handle)      

###############################################################################
# setResponseTimeout
#

def setResponseTimeout(handle, timeout):
    rv = lib.vscphlp_setResponseTimeout( c_long(handle), c_ulong(timeout) )
    return rv

###############################################################################
# setAfterCommandSleep
#

def setAfterCommandSleep(handle, timeout):
    rv = lib.vscphlp_setAfterCommandSleep( c_long(handle), c_ushort(timeout) )
    return rv

###############################################################################
# open
#

def open(handle,host,user,password):
    rv = lib.vscphlp_open( c_long(handle),
                            c_char_p(host.encode('utf-8')),
                            c_char_p(user.encode('utf-8')),
                            c_char_p(password.encode('utf-8')))
    return rv        

###############################################################################
# openInterface
#

def openInterface(handle,interface,flags):
    rv = lib.vscphlp_openInterface( c_long(handle),
                                        c_char_p(interface.encode('utf-8')),
                                        c_ulong(flags) )
    return rv 

###############################################################################
# close
#

def close(handle):
    rv = lib.vscphlp_close( c_long(handle) )
    return rv    

###############################################################################
# isConnected
#

def isConnected(handle):
    rv = lib.vscphlp_isConnected( c_long(handle) )
    return rv

###############################################################################
# doCommand
#

def doCommand(handle, command):
    rv = lib.vscphlp_doCommand( c_long(handle), c_char_p(command.encode('utf-8')) )
    return rv

###############################################################################
# checkReply
#

def checkReply(handle, bClear):
    rv = lib.vscphlp_checkReply( c_long(handle), c_int(bClear) )
    return rv

###############################################################################
# clearLocalInputQueue
#

def clearLocalInputQueue(handle):
    rv = lib.vscphlp_clearLocalInputQueue( c_long(handle) )
    return rv

###############################################################################
# noop
#

def noop(handle):    
    rv = lib.vscphlp_noop( c_long(handle) )
    return rv  

###############################################################################
# clearDaemonEventQueue
#

def clearDaemonEventQueue(handle):    
    rv = lib.vscphlp_clearDaemonEventQueue( c_long(handle) )
    return rv  

###############################################################################
# sendEvent
#

def sendEvent(handle,event):    
    rv = lib.vscphlp_sendEvent( c_long(handle), byref(event) )
    return rv 

###############################################################################
# sendEventEx
#

def sendEventEx(handle,eventex):    
    rv = lib.vscphlp_sendEventEx( c_long(handle), byref(eventex) )
    return rv 

###############################################################################
# sendEvent
#

def sendEvent(handle,event):    
    rv = lib.vscphlp_sendEvent( c_long(handle), byref(event) )
    return rv 

###############################################################################
# receiveEvent
#

def receiveEvent(handle,event):    
    rv = lib.vscphlp_receiveEvent( c_long(handle), byref(event) )
    return rv 

###############################################################################
# receiveEventEx
#

def receiveEventEx(handle,eventex):    
    rv = lib.vscphlp_receiveEventEx( c_long(handle), byref(eventex) )
    return rv 

###############################################################################
# isDataAvailable
#

def isDataAvailable(handle,cntAvailable):    
    rv = lib.vscphlp_isDataAvailable( c_long(handle), byref(cntAvailable))
    return rv

###############################################################################
# enterReceiveLoop
#

def enterReceiveLoop(handle):    
    rv = lib.vscphlp_enterReceiveLoop( c_long(handle) )
    return rv

###############################################################################
# quitReceiveLoop
#

def quitReceiveLoop(handle):    
    rv = lib.vscphlp_quitReceiveLoop( c_long(handle) )
    return rv

###############################################################################
# blockingReceiveEvent
#

def blockingReceiveEvent( handle, event, timeout):    
    rv = lib.vscphlp_blockingReceiveEvent( c_long(handle), byref(event), c_ulong(timeout) )
    return rv 

###############################################################################
# blockingReceiveEventEx
#

def blockingReceiveEventEx( handle, eventex, timeout ):    
    rv = lib.vscphlp_blockingReceiveEventEx( c_long(handle), byref(eventex), c_ulong(timeout) )
    return rv 

###############################################################################
# setStatistics
#

def getStatistics( handle, statistics ):    
    rv = lib.vscphlp_getStatistics( c_long(handle), byref(statistics) )
    return rv 

###############################################################################
# setStatus
#

def getStatus( handle, status ):    
    rv = lib.vscphlp_getStatus( c_long(handle), byref(status) )
    return rv

###############################################################################
# setFilter
#

def setFilter( handle, filter ):    
    rv = lib.vscphlp_setFilter( c_long(handle), byref(filter) )
    return rv 

###############################################################################
# getVersion
#

def getVersion(handle):
    v1 = c_ubyte()
    v2 = c_ubyte()
    v3 = c_ubyte()
    rv = lib.vscphlp_getVersion( c_long(handle), byref(v1), byref(v2), byref(v3) )
    return (rv,v1,v2,v3)

###############################################################################
# getDLLVersion
#

def getDLLVersion(handle):
    dllversion = c_ulong()
    rv = lib.vscphlp_getDLLVersion( c_long(handle), byref( dllversion ) )
    return (rv,dllversion )

###############################################################################
# getVendorString
#

def getVendorString(handle):
    strvendor = create_string_buffer(b'\000' * 80)
    rv = lib.vscphlp_getVendorString( c_long(handle), strvendor, c_size_t( 80 ) )
    return (rv,repr(strvendor.value) )

###############################################################################
# getDriverInfo
#

def getDriverInfo(handle):
    strdrvinfo = create_string_buffer(b'\000' * 32000)
    rv = lib.vscphlp_getDriverInfo( c_long(handle), strdrvinfo, c_size_t( 32000 ) )
    return (rv,repr(strdrvinfo.value) )

###############################################################################
# vscphlp_serverShutDown
#

def vscphlp_serverShutDown(handle):
    rv = lib.vscphlp_vscphlp_serverShutDown( c_long(handle)  )
    return rv 
