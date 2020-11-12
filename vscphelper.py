# FILE: vscphelper.py
#
# VSCP Helper Library binding for Python
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
import sys
from ctypes import *
import _ctypes
import struct
import vscp 


if os.name == "nt":
    lib = cdll.LoadLibrary('libvscphelper.dll')
else:
    lib = cdll.LoadLibrary('libvscphelper.so')    

###############################################################################
# newSession
#
# Start a new library session
# 
# @return Handle to a new session as a c_long or null on
# failure
#

def newSession():
    lib.newSession.restype = c_long
    handle = lib.newSession()
    return handle

###############################################################################
# closeSession
#
# End library session
# 
# @param handle c_long handle received from a newSession call.
#

def closeSession( handle ):
    lib.closeSession( c_long(handle) )
    _ctypes.dlclose(lib._handle) 
    # Is this needed?
    # if os.name == "nt":
    #     _ctypes.FreeLibrary(lib1._handle)
    # else:    
    #     _ctypes.dlclose(lib._handle)      

###############################################################################
# setResponseTimeout
#

def setResponseTimeout(handle, timeout):
    rv = lib.setResponseTimeout( c_long(handle), c_ulong(timeout) )
    return rv

###############################################################################
# setAfterCommandSleep
#

def setAfterCommandSleep(handle, timeout):
    rv = lib.setAfterCommandSleep( c_long(handle), c_ushort(timeout) )
    return rv

###############################################################################
# open
#

def open(handle,host,user,password):
    rv = lib.open( c_long(handle),
                            c_char_p(host.encode('utf-8')),
                            c_char_p(user.encode('utf-8')),
                            c_char_p(password.encode('utf-8')))
    return rv        

###############################################################################
# openInterface
#

def openInterface(handle,interface,flags):
    rv = lib.openInterface( c_long(handle),
                                        c_char_p(interface.encode('utf-8')),
                                        c_ulong(flags) )
    return rv 

###############################################################################
# close
#

def close(handle):
    rv = lib.close( c_long(handle) )
    return rv    

###############################################################################
# isConnected
#

def isConnected(handle):
    rv = lib.isConnected( c_long(handle) )
    return rv

###############################################################################
# doCommand
#

def doCommand(handle, command):
    rv = lib.doCommand( c_long(handle), c_char_p(command.encode('utf-8')) )
    return rv

###############################################################################
# checkReply
#

def checkReply(handle, bClear):
    rv = lib.checkReply( c_long(handle), c_int(bClear) )
    return rv

###############################################################################
# clearLocalInputQueue
#

def clearLocalInputQueue(handle):
    rv = lib.clearLocalInputQueue( c_long(handle) )
    return rv

###############################################################################
# noop
#

def noop(handle):    
    rv = lib.noop( c_long(handle) )
    return rv  

###############################################################################
# clearDaemonEventQueue
#

def clearDaemonEventQueue(handle):    
    rv = lib.clearDaemonEventQueue( c_long(handle) )
    return rv  

###############################################################################
# sendEvent
#

def sendEvent(handle,event):    
    rv = lib.sendEvent( c_long(handle), byref(event) )
    return rv 

###############################################################################
# sendEventEx
#

def sendEventEx(handle,eventex):    
    rv = lib.sendEventEx( c_long(handle), byref(eventex) )
    return rv 

###############################################################################
# sendEvent
#

def sendEvent(handle,event):    
    rv = lib.sendEvent( c_long(handle), byref(event) )
    return rv 

###############################################################################
# receiveEvent
#

def receiveEvent(handle,event):    
    rv = lib.receiveEvent( c_long(handle), byref(event) )
    return rv 

###############################################################################
# receiveEventEx
#

def receiveEventEx(handle,eventex):    
    rv = lib.receiveEventEx( c_long(handle), byref(eventex) )
    return rv 

###############################################################################
# isDataAvailable
#

def isDataAvailable(handle,cntAvailable):    
    rv = lib.isDataAvailable( c_long(handle), byref(cntAvailable))
    return rv

###############################################################################
# enterReceiveLoop
#

def enterReceiveLoop(handle):    
    rv = lib.enterReceiveLoop( c_long(handle) )
    return rv

###############################################################################
# quitReceiveLoop
#

def quitReceiveLoop(handle):    
    rv = lib.quitReceiveLoop( c_long(handle) )
    return rv

###############################################################################
# blockingReceiveEvent
#

def blockingReceiveEvent( handle, event, timeout):    
    rv = lib.blockingReceiveEvent( c_long(handle), byref(event), c_ulong(timeout) )
    return rv 

###############################################################################
# blockingReceiveEventEx
#

def blockingReceiveEventEx( handle, eventex, timeout ):    
    rv = lib.blockingReceiveEventEx( c_long(handle), byref(eventex), c_ulong(timeout) )
    return rv 

###############################################################################
# setStatistics
#

def getStatistics( handle, statistics ):    
    rv = lib.getStatistics( c_long(handle), byref(statistics) )
    return rv 

###############################################################################
# setStatus
#

def getStatus( handle, status ):    
    rv = lib.getStatus( c_long(handle), byref(status) )
    return rv

###############################################################################
# setFilter
#

def setFilter( handle, filter ):    
    rv = lib.setFilter( c_long(handle), byref(filter) )
    return rv 

###############################################################################
# getVersion
#

def getVersion(handle):
    v1 = c_ubyte()
    v2 = c_ubyte()
    v3 = c_ubyte()
    rv = lib.getVersion( c_long(handle), byref(v1), byref(v2), byref(v3) )
    return (rv,v1,v2,v3)

###############################################################################
# getDLLVersion
#

def getDLLVersion(handle):
    dllversion = c_ulong()
    rv = lib.getDLLVersion( c_long(handle), byref( dllversion ) )
    return (rv,dllversion )

###############################################################################
# getVendorString
#

def getVendorString(handle):
    strvendor = create_string_buffer(b'\000' * 80)
    rv = lib.getVendorString( c_long(handle), strvendor, c_size_t( 80 ) )
    return (rv,repr(strvendor.value) )

###############################################################################
# getDriverInfo
#

def getDriverInfo(handle):
    strdrvinfo = create_string_buffer(b'\000' * 32000)
    rv = lib.getDriverInfo( c_long(handle), strdrvinfo, c_size_t( 32000 ) )
    return (rv,repr(strdrvinfo.value) )

###############################################################################
# serverShutDown
#

def serverShutDown(handle):
    rv = lib.serverShutDown( c_long(handle)  )
    return rv 


# -----------------------------------------------------------------------------


###############################################################################
# float2ByteArray
# Convert floating point value to byte array (four bytes). This translation is
# done by the function if needed.
#
# value = 5.1
# ba = bytearray(struct.pack("d", value))   
# print([ "0x%02x" % b for b in ba ])
#

def float2ByteArray(val):
    ba = bytearray(struct.pack("f", val))
    if sys.byteorder == 'little':
        ba.reverse()
    return ba

###############################################################################
# double2ByteArray
# Convert floating point value to byte array (eight bytes)
# https://docs.python.org/2/library/struct.html

def double2ByteArray(val):
    ba = bytearray(struct.pack("d", val))
    if sys.byteorder == 'little':
        ba.reverse()
    return ba

###############################################################################
# byteArray2Float
# Convert floating point value in big endian bytearray to floating point
# value
#

def byteArray2Float(ba):
    return struct.unpack(">f", ba)

###############################################################################
# byteArray2Double
# Convert double precision floating point value in big endian bytearray to 
# double precision floating point value
#

def byteArray2Double(ba):
    return struct.unpack(">d", ba)

###############################################################################
# string2ByteArray
#
# String is converted into byte array with terminating zero
#
# @param str String toi convert to byte array
# @return bytearray representation fo string 
#

def string2ByteArray(str):
    ba = bytearray()
    if(sys.version_info[:3] < (3,0)):
        ba.extend(str)  # Python 2
    else:    
        ba.extend(map(ord, str))  # Python 3
    ba.append(0)
    return ba

###############################################################################
# byteArrayToPos
#
# Writes the content of as bytearray into a specific position of another
# byte array
#
# @param ba_to Byte array that should receive the content
# @param pos Position to copy to
# @param ba_from Byte array to copy from.
# @return Return the resulting bytearray

def byteArrayToPos(ba_to, pos, ba_from):
    return ba_to[:pos] + ba_from[:] + ba_to[pos+len(ba_from):]

