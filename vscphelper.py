# FILE: vscphelper.py
#
# VSCP Helper Library binding for Python
#
# This file is part of the VSCP (http://www.vscp.org)
#
# The MIT License (MIT)
#
# Copyright (c) 2000-2026 Ake Hedman and contributors, the VSCP Project <info@grodansparadis.com>
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


def _loadHelperLib():
    # VSCPHELPER_LIB can point to the full path of the library
    if 'VSCPHELPER_LIB' in os.environ:
        return cdll.LoadLibrary(os.environ['VSCPHELPER_LIB'])
    if os.name == "nt":
        names = ['libvscphelper.dll', 'libvscphelper15.dll']
    else:
        names = ['libvscphelper.so', 'libvscphelper15.so', 'libvscphelper.so.15']
    for name in names:
        try:
            return cdll.LoadLibrary(name)
        except OSError:
            pass
    raise OSError('Unable to load the VSCP helper library (tried %s). '
                  'Set VSCPHELPER_LIB to its full path.' % ', '.join(names))

lib = _loadHelperLib()

# Some symbols have been renamed between helper lib versions
def _libfunc(*names):
    for name in names:
        try:
            return getattr(lib, name)
        except AttributeError:
            pass
    raise AttributeError('None of %s is exported by the VSCP helper library' % (names,))

###############################################################################
# newSession
#
# Start a new library session
# 
# @return Handle to a new session as a c_long or null on
# failure
#

def newSession():
    lib.vscphlp_newSession.restype = c_long
    handle = lib.vscphlp_newSession()
    return handle

###############################################################################
# closeSession
#
# End library session
# 
# @param handle c_long handle received from a newSession call.
#

def closeSession( handle ):
    lib.vscphlp_closeSession( c_long(handle) )
    _ctypes.dlclose(lib._handle) 
    # Is this needed?
    # if os.name == "nt":
    #     _ctypes.FreeLibrary(lib1._handle)
    # else:    
    #     _ctypes.dlclose(lib.vscphlp__handle)      

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
# getGUID
#

def getGUID(handle):
    guid = (c_ubyte * 16)()
    rv = lib.vscphlp_getGUID( c_long(handle), guid )
    return rv, guid

###############################################################################
# setGUID
#

def setGUID(handle, guid):
    rv = lib.vscphlp_setGUID( c_long(handle), guid )
    return rv

###############################################################################
# serverShutDown
#

def serverShutDown(handle):
    f = _libfunc('vscphlp_serverShutDown', 'vscphlp_shutDownServer')
    rv = f( c_long(handle)  )
    return rv 


# -----------------------------------------------------------------------------
#                             Measurement Helpers
# -----------------------------------------------------------------------------

def makeFloatMeasurementEvent( e, value, unit, sensoridx ):
    return lib.vscphlp_makeFloatMeasurementEvent( byref(e), c_float(value), c_ubyte(unit), c_ubyte(sensoridx) )                                

def makeFloatMeasurementEventEx( ex, value, unit, sensoridx ):
    return lib.vscphlp_makeFloatMeasurementEventEx( byref(ex), c_float(value), c_ubyte(unit), c_ubyte(sensoridx) )

def makeStringMeasurementEvent( e, value, unit, sensoridx ):
    return lib.vscphlp_makeStringMeasurementEvent( byref(e), c_float(value), c_ubyte(unit), c_ubyte(sensoridx) )                                

def makeStringMeasurementEventEx( ex, value, unit, sensoridx ):
    return lib.vscphlp_makeStringMeasurementEventEx( byref(ex), c_float(value), c_ubyte(unit), c_ubyte(sensoridx) ) 

def makeLevel2FloatMeasurementEvent( e,
                                        type,
                                        value,
                                        unit,
                                        sensoridx,
                                        zone,
                                        subzone ) :
    return lib.vscphlp_makeLevel2FloatMeasurementEvent( byref(e), c_uint16(type), c_double(value), c_ubyte(unit), 
                                                    c_ubyte(sensoridx), c_ubyte(zone), c_ubyte(subzone) )                                       

def makeLevel2FloatMeasurementEventEx( ex,
                                        type,
                                        value,
                                        unit,
                                        sensoridx,
                                        zone,
                                        subzone ) :
    return lib.vscphlp_makeLevel2FloatMeasurementEventEx( byref(ex), c_uint16(type), c_double(value), c_ubyte(unit), 
                                                    c_ubyte(sensoridx), c_ubyte(zone), c_ubyte(subzone) )

def makeLevel2StringMeasurementEvent( e,
                                        type,
                                        value,
                                        unit,
                                        sensoridx,
                                        zone,
                                        subzone ) :
    return lib.vscphlp_makeLevel2StringMeasurementEvent( byref(e), c_uint16(type), c_double(value), c_ubyte(unit), 
                                                    c_ubyte(sensoridx), c_ubyte(zone), c_ubyte(subzone) )                                        

def makeLevel2StringMeasurementEventEx( ex,
                                        type,
                                        value,
                                        unit,
                                        sensoridx,
                                        zone,
                                        subzone ) :
    return lib.vscphlp_makeLevel2StringMeasurementEventEx( byref(ex), c_uint16(type), c_double(value), c_ubyte(unit), 
                                                    c_ubyte(sensoridx), c_ubyte(zone), c_ubyte(subzone) ) 

def convertLevel1MeasuremenToLevel2Double( e ) :
    f = _libfunc('vscphlp_convertLevel1MeasuremenToLevel2Double',
                 'vscphlp_convertLevel1MeasurementToLevel2Double')
    return f( byref(e) )

def convertLevel1MeasuremenToLevel2DoubleEx( ex ) :
    f = _libfunc('vscphlp_convertLevel1MeasuremenToLevel2DoubleEx',
                 'vscphlp_convertLevel1MeasurementToLevel2DoubleEx')
    return f( byref(ex) )

def convertLevel1MeasuremenToLevel2String( e ) :
    f = _libfunc('vscphlp_convertLevel1MeasuremenToLevel2String',
                 'vscphlp_convertLevel1MeasurementToLevel2String')
    return f( byref(e) )

def convertLevel1MeasuremenToLevel2StringEx( ex ) :
    f = _libfunc('vscphlp_convertLevel1MeasuremenToLevel2StringEx',
                 'vscphlp_convertLevel1MeasurementToLevel2StringEx')
    return f( byref(ex) )

###############################################################################
# convertFloatToNormalizedEventData
#

def convertFloatToNormalizedEventData( value, unit, sensoridx ):
    data = (c_ubyte * 8)()
    size = c_ushort()
    rv = lib.vscphlp_convertFloatToNormalizedEventData( data,
                                                        byref(size),
                                                        c_double(value),
                                                        c_ubyte(unit),
                                                        c_ubyte(sensoridx) )
    return rv, bytearray(data[:size.value])

###############################################################################
# convertFloatToFloatEventData
#

def convertFloatToFloatEventData( value, unit, sensoridx ):
    data = (c_ubyte * 8)()
    size = c_ushort()
    rv = lib.vscphlp_convertFloatToFloatEventData( data,
                                                    byref(size),
                                                    c_float(value),
                                                    c_ubyte(unit),
                                                    c_ubyte(sensoridx) )
    return rv, bytearray(data[:size.value])

###############################################################################
# convertIntegerToNormalizedEventData
#

def convertIntegerToNormalizedEventData( value, unit, sensoridx ):
    data = (c_ubyte * 8)()
    size = c_ushort()
    rv = lib.vscphlp_convertIntegerToNormalizedEventData( data,
                                                            byref(size),
                                                            c_ulonglong(value),
                                                            c_ubyte(unit),
                                                            c_ubyte(sensoridx) )
    return rv, bytearray(data[:size.value])

###############################################################################
# getMeasurementAsFloat
#

def getMeasurementAsFloat( data ):
    buf = (c_ubyte * len(data))(*data)
    result = c_float()
    rv = lib.vscphlp_getMeasurementAsFloat( buf, c_ubyte(len(data)), byref(result) )
    return rv, result.value

###############################################################################
# getMeasurementUnit
#

def getMeasurementUnit( e ):
    return lib.vscphlp_getMeasurementUnit( byref(e) )

###############################################################################
# getMeasurementSensorIndex
#

def getMeasurementSensorIndex( e ):
    f = _libfunc('vscphlp_getMeasurementSensorIndex',
                 'vscphlp_getMeasuremenSensorIndex')
    return f( byref(e) )

###############################################################################
# getMeasurementZone
#

def getMeasurementZone( e ):
    return lib.vscphlp_getMeasurementZone( byref(e) )

###############################################################################
# getMeasurementSubZone
#

def getMeasurementSubZone( e ):
    return lib.vscphlp_getMeasurementSubZone( byref(e) )

###############################################################################
# isMeasurement
#

def isMeasurement( e ):
    return lib.vscphlp_isMeasurement( byref(e) )

###############################################################################
# getMeasurementDataCoding
#

def getMeasurementDataCoding( e ):
    lib.vscphlp_getMeasurementDataCoding.restype = c_ubyte
    return lib.vscphlp_getMeasurementDataCoding( byref(e) )

###############################################################################
# getDataCodingBitArray
#

def getDataCodingBitArray( data ):
    buf = (c_ubyte * len(data))(*data)
    lib.vscphlp_getDataCodingBitArray.restype = c_ulonglong
    return lib.vscphlp_getDataCodingBitArray( buf, c_int(len(data)) )

###############################################################################
# getDataCodingInteger
#

def getDataCodingInteger( data ):
    buf = (c_ubyte * len(data))(*data)
    lib.vscphlp_getDataCodingInteger.restype = c_ulonglong
    return lib.vscphlp_getDataCodingInteger( buf, c_int(len(data)) )

###############################################################################
# getDataCodingNormalizedInteger
#

def getDataCodingNormalizedInteger( data ):
    buf = (c_ubyte * len(data))(*data)
    lib.vscphlp_getDataCodingNormalizedInteger.restype = c_double
    return lib.vscphlp_getDataCodingNormalizedInteger( buf, c_int(len(data)) )

###############################################################################
# getDataCodingString
#

def getDataCodingString( data ):
    buf = (c_ubyte * len(data))(*data)
    result = create_string_buffer(b'\000' * 512)
    rv = lib.vscphlp_getDataCodingString( buf,
                                            c_ubyte(len(data)),
                                            result,
                                            c_size_t(len(result)) )
    return rv, result.value.decode('utf-8')

###############################################################################
# getVSCPMeasurementAsDouble
#

def getVSCPMeasurementAsDouble( e ):
    value = c_double()
    rv = lib.vscphlp_getVSCPMeasurementAsDouble( byref(e), byref(value) )
    return rv, value.value

###############################################################################
# getVSCPMeasurementAsString
#

def getVSCPMeasurementAsString( e ):
    result = create_string_buffer(b'\000' * 512)
    rv = lib.vscphlp_getVSCPMeasurementAsString( byref(e), result, c_size_t(len(result)) )
    return rv, result.value.decode('utf-8')

###############################################################################
# getVSCPMeasurementFloat64AsString
#

def getVSCPMeasurementFloat64AsString( e ):
    result = create_string_buffer(b'\000' * 512)
    rv = lib.vscphlp_getVSCPMeasurementFloat64AsString( byref(e), result, c_size_t(len(result)) )
    return rv, result.value.decode('utf-8')

# -----------------------------------------------------------------------------
#                              Python Helpers
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

# -----------------------------------------------------------------------------
#                              General Helpers
# -----------------------------------------------------------------------------


###############################################################################
# convertEventToJSON
#

def convertEventToJSON(e):
    result = create_string_buffer(b'\000' * 2048)
    result_len = c_size_t(len(result))

    rv = lib.vscphlp_convertEventToJSON( byref(e), result, result_len )
    #s = repr(result.value).decode('utf-8')
    s = result.value.decode('utf-8')
    return rv,s

###############################################################################
# convertEventExToJSON
#

def convertEventExToJSON(ex):
    result = create_string_buffer(b'\000' * 2048)
    result_len = c_size_t(len(result))

    rv = lib.vscphlp_convertEventExToJSON( byref(ex), result, result_len )
    s = result.value.decode('utf-8')
    return rv,s

###############################################################################
# convertEventToXML
#

def convertEventToXML(e):
    result = create_string_buffer(b'\000' * 2048)
    result_len = c_size_t(len(result))

    rv = lib.vscphlp_convertEventToXML( byref(e), result, result_len )    
    s = result.value.decode('utf-8')
    return rv,s

###############################################################################
# convertEventExToXML
#

def convertEventExToXML(ex):
    result = create_string_buffer(b'\000' * 2048)
    result_len = c_size_t(len(result))

    rv = lib.vscphlp_convertEventExToXML( byref(ex), result, result_len )
    s = result.value.decode('utf-8')
    return rv,s

###############################################################################
# convertEventToHTML
#

def convertEventToHTML(e):
    result = create_string_buffer(b'\000' * 2048)
    result_len = c_size_t(len(result))

    rv = lib.vscphlp_convertEventToHTML( byref(e), result, result_len )
    s = result.value.decode('utf-8')
    return rv,s

###############################################################################
# convertEventExToHTML
#

def convertEventExToHTML(ex):
    result = create_string_buffer(b'\000' * 2048)
    result_len = c_size_t(len(result))

    rv = lib.vscphlp_convertEventExToHTML( byref(ex), result, result_len )
    s = result.value.decode('utf-8')
    return rv,s


###############################################################################
# convertEventToString
#

def convertEventToString(e) :
    result = create_string_buffer(b'\000' * 2048)
    result_len = c_size_t(len(result))

    rv = lib.vscphlp_writeVscpEventToString( byref(e), result, result_len )
    #s = repr(result.value).decode('utf-8')
    s = result.value.decode('utf-8')
    return rv,s


###############################################################################
# convertEventExToString
#

def convertEventExToString(ex):
    result = create_string_buffer(b'\000' * 2048)
    result_len = c_size_t(len(result))

    rv = lib.vscphlp_writeVscpEventExToString( byref(ex), result, result_len )
    s = result.value.decode('utf-8')
    return rv,s

###############################################################################
# convertStringToEvent
#

def convertStringToEvent(e, str) :
    bstr = str.encode('utf-8')
    rv = lib.vscphlp_convertStringToEvent( byref(e), c_char_p(bstr) )
    return rv,e

###############################################################################
# convertStringToEventEx
#

def convertStringToEventEx(ex, str) :
    bstr = str.encode('utf-8')
    rv = lib.vscphlp_convertStringToEventEx( byref(ex), c_char_p(bstr) )
    return rv,ex

###############################################################################
# getDateStringFromEvent
#

def getDateStringFromEvent(e) :
    buf = create_string_buffer(b'\000' * 60)
    buf_len = c_size_t(len(buf))
    rv = lib.vscphlp_getDateStringFromEvent( buf, buf_len, byref(e) )
    s = buf.value.decode('utf-8')
    return rv,s

###############################################################################
# getDateStringFromEventEx
#

def getDateStringFromEventEx(ex) :
    buf = create_string_buffer(b'\000' * 60)
    buf_len = c_size_t(len(buf))
    rv = lib.vscphlp_getDateStringFromEventEx( buf, buf_len, byref(ex) )
    s = buf.value.decode('utf-8')
    return rv,s

###############################################################################
# readStringValue
#
# Read a numerical value from a string. The string may be expressed as a
# decimal value or a hexadecimal value (preceded by 0x).
#

def readStringValue(str):
    lib.vscphlp_readStringValue.restype = c_ulong
    return lib.vscphlp_readStringValue( c_char_p(str.encode('utf-8')) )

###############################################################################
# replaceBackslash
#
# Replace all backslashes in a string with forward slashes
#

def replaceBackslash(str):
    buf = create_string_buffer(str.encode('utf-8'))
    rv = lib.vscphlp_replaceBackslash( buf )
    return rv, buf.value.decode('utf-8')

###############################################################################
# getVscpPriority
#

def getVscpPriority(e):
    lib.vscphlp_getVscpPriority.restype = c_ubyte
    return lib.vscphlp_getVscpPriority( byref(e) )

###############################################################################
# getVscpPriorityEx
#

def getVscpPriorityEx(ex):
    lib.vscphlp_getVscpPriorityEx.restype = c_ubyte
    return lib.vscphlp_getVscpPriorityEx( byref(ex) )

###############################################################################
# setVscpPriority
#

def setVscpPriority(e, priority):
    lib.vscphlp_setVscpPriority( byref(e), c_ubyte(priority) )

###############################################################################
# setVscpPriorityEx
#

def setVscpPriorityEx(ex, priority):
    lib.vscphlp_setVscpPriorityEx( byref(ex), c_ubyte(priority) )

###############################################################################
# getVSCPheadFromCANALid
#

def getVSCPheadFromCANALid(id):
    lib.vscphlp_getVSCPheadFromCANALid.restype = c_ubyte
    return lib.vscphlp_getVSCPheadFromCANALid( c_ulong(id) )

###############################################################################
# getVSCPclassFromCANALid
#

def getVSCPclassFromCANALid(id):
    lib.vscphlp_getVSCPclassFromCANALid.restype = c_ushort
    return lib.vscphlp_getVSCPclassFromCANALid( c_ulong(id) )

###############################################################################
# getVSCPtypeFromCANALid
#

def getVSCPtypeFromCANALid(id):
    lib.vscphlp_getVSCPtypeFromCANALid.restype = c_ushort
    return lib.vscphlp_getVSCPtypeFromCANALid( c_ulong(id) )

###############################################################################
# getVSCPnicknameFromCANALid
#

def getVSCPnicknameFromCANALid(id):
    lib.vscphlp_getVSCPnicknameFromCANALid.restype = c_ubyte
    return lib.vscphlp_getVSCPnicknameFromCANALid( c_ulong(id) )

###############################################################################
# getCANALidFromData
#

def getCANALidFromData(priority, vscp_class, vscp_type):
    lib.vscphlp_getCANALidFromData.restype = c_ulong
    return lib.vscphlp_getCANALidFromData( c_ubyte(priority),
                                            c_ushort(vscp_class),
                                            c_ushort(vscp_type) )

###############################################################################
# getCANALidFromEvent
#

def getCANALidFromEvent(e):
    lib.vscphlp_getCANALidFromEvent.restype = c_ulong
    return lib.vscphlp_getCANALidFromEvent( byref(e) )

###############################################################################
# getCANALidFromEventEx
#

def getCANALidFromEventEx(ex):
    lib.vscphlp_getCANALidFromEventEx.restype = c_ulong
    return lib.vscphlp_getCANALidFromEventEx( byref(ex) )

###############################################################################
# calc_crc_Event
#
# Calculate the CRC for a VSCP event. The CRC is set in the event if
# bSet is non-zero.
#

def calc_crc_Event(e, bSet):
    lib.vscphlp_calc_crc_Event.restype = c_ushort
    return lib.vscphlp_calc_crc_Event( byref(e), c_short(bSet) )

###############################################################################
# calc_crc_EventEx
#

def calc_crc_EventEx(ex, bSet):
    lib.vscphlp_calc_crc_EventEx.restype = c_ushort
    return lib.vscphlp_calc_crc_EventEx( byref(ex), c_short(bSet) )

###############################################################################
# convertVSCPtoEx
#
# Convert VSCP event to VSCP event ex
#

def convertVSCPtoEx(ex, e):
    return lib.vscphlp_convertVSCPtoEx( byref(ex), byref(e) )

###############################################################################
# convertVSCPfromEx
#
# Convert VSCP event ex to VSCP event
#

def convertVSCPfromEx(e, ex):
    return lib.vscphlp_convertVSCPfromEx( byref(e), byref(ex) )

###############################################################################
# newVSCPevent
#
# Allocate a new VSCP event. Returns rv and a pointer to the new event.
#

def newVSCPevent():
    pEvent = POINTER(vscp.vscpEvent)()
    rv = lib.vscphlp_newVSCPevent( byref(pEvent) )
    return rv, pEvent

###############################################################################
# deleteVSCPevent
#

def deleteVSCPevent(pEvent):
    lib.vscphlp_deleteVSCPevent( pEvent )

###############################################################################
# deleteVSCPevent_v2
#

def deleteVSCPevent_v2(pEvent):
    lib.vscphlp_deleteVSCPevent_v2( byref(pEvent) )

###############################################################################
# deleteVSCPeventEx
#

def deleteVSCPeventEx(pEventEx):
    lib.vscphlp_deleteVSCPeventEx( byref(pEventEx) )

###############################################################################
# copyVSCPEvent
#

def copyVSCPEvent(eTo, eFrom):
    return lib.vscphlp_copyVSCPEvent( byref(eTo), byref(eFrom) )

###############################################################################
# makeTimeStamp
#
# Get new VSCP timestamp (microseconds)
#

def makeTimeStamp():
    lib.vscphlp_makeTimeStamp.restype = c_ulong
    return lib.vscphlp_makeTimeStamp()

###############################################################################
# setEventDateTimeBlockToNow
#

def setEventDateTimeBlockToNow(e):
    return lib.vscphlp_setEventDateTimeBlockToNow( byref(e) )

###############################################################################
# setEventExDateTimeBlockToNow
#

def setEventExDateTimeBlockToNow(ex):
    return lib.vscphlp_setEventExDateTimeBlockToNow( byref(ex) )

###############################################################################
# setEventToNow
#

def setEventToNow(e):
    return lib.vscphlp_setEventToNow( byref(e) )

###############################################################################
# setEventExToNow
#

def setEventExToNow(ex):
    return lib.vscphlp_setEventExToNow( byref(ex) )

###############################################################################
# getTimeString
#
# Get time string from unix timestamp
#

def getTimeString(t):
    buf = create_string_buffer(b'\000' * 60)
    tt = c_long(int(t))
    rv = lib.vscphlp_getTimeString( buf, c_size_t(len(buf)), byref(tt) )
    return rv, buf.value.decode('utf-8')

###############################################################################
# getISOTimeString
#
# Get ISO formatted time string from unix timestamp
#

def getISOTimeString(t):
    buf = create_string_buffer(b'\000' * 60)
    tt = c_long(int(t))
    rv = lib.vscphlp_getISOTimeString( buf, c_size_t(len(buf)), byref(tt) )
    return rv, buf.value.decode('utf-8')

###############################################################################
# setVscpEventFromString
#
# Deprecated: use convertStringToEvent
#

def setVscpEventFromString(e, str):
    return lib.vscphlp_setVscpEventFromString( byref(e), c_char_p(str.encode('utf-8')) )

###############################################################################
# setVscpEventExFromString
#
# Deprecated: use convertStringToEventEx
#

def setVscpEventExFromString(ex, str):
    return lib.vscphlp_setVscpEventExFromString( byref(ex), c_char_p(str.encode('utf-8')) )

###############################################################################
# setVscpDataFromString
#
# Set the data of an event from a comma separated string
#

def setVscpDataFromString(e, str):
    return lib.vscphlp_setVscpDataFromString( byref(e), c_char_p(str.encode('utf-8')) )

###############################################################################
# getVscpDataFromString
#

def getVscpDataFromString(e, str):
    return lib.vscphlp_getVscpDataFromString( byref(e), c_char_p(str.encode('utf-8')) )

###############################################################################
# getVscpDataArrayFromString
#
# Get a data array from a comma separated string
#

def getVscpDataArrayFromString(str):
    data = (c_ubyte * 512)()
    size = c_ushort()
    rv = lib.vscphlp_getVscpDataArrayFromString( data, byref(size), c_char_p(str.encode('utf-8')) )
    return rv, bytearray(data[:size.value])

###############################################################################
# setVscpDataArrayFromString
#

def setVscpDataArrayFromString(str):
    data = (c_ubyte * 512)()
    size = c_ushort()
    rv = lib.vscphlp_setVscpDataArrayFromString( data, byref(size), c_char_p(str.encode('utf-8')) )
    return rv, bytearray(data[:size.value])

###############################################################################
# writeVscpDataToString
#
# Write the data of an event to a string
#

def writeVscpDataToString(e, bUseHtmlBreak=0):
    result = create_string_buffer(b'\000' * 2048)
    rv = lib.vscphlp_writeVscpDataToString( result,
                                            byref(e),
                                            c_size_t(len(result)),
                                            c_int(bUseHtmlBreak) )
    return rv, result.value.decode('utf-8')

###############################################################################
# writeVscpDataWithSizeToString
#

def writeVscpDataWithSizeToString(data, bUseHtmlBreak=0, bBreak=0):
    buf = (c_ubyte * len(data))(*data)
    result = create_string_buffer(b'\000' * 2048)
    # Note: the compiled lib takes the string buffer first, unlike the header
    rv = lib.vscphlp_writeVscpDataWithSizeToString( result,
                                                    buf,
                                                    c_ushort(len(data)),
                                                    c_size_t(len(result)),
                                                    c_int(bUseHtmlBreak),
                                                    c_int(bBreak) )
    return rv, result.value.decode('utf-8')


# -----------------------------------------------------------------------------
#                              Filter Helpers
# -----------------------------------------------------------------------------


###############################################################################
# clearVSCPFilter
#

def clearVSCPFilter(filter):
    lib.vscphlp_clearVSCPFilter( byref(filter) )

###############################################################################
# copyVSCPFilter
#

def copyVSCPFilter(filterTo, filterFrom):
    lib.vscphlp_copyVSCPFilter( byref(filterTo), byref(filterFrom) )

###############################################################################
# readFilterFromString
#
# Read a filter from a string on the form
# "priority,class,type,GUID"
#

def readFilterFromString(filter, str):
    return lib.vscphlp_readFilterFromString( byref(filter), c_char_p(str.encode('utf-8')) )

###############################################################################
# readMaskFromString
#
# Read a mask from a string on the form
# "priority,class,type,GUID"
#

def readMaskFromString(filter, str):
    return lib.vscphlp_readMaskFromString( byref(filter), c_char_p(str.encode('utf-8')) )

###############################################################################
# writeFilterToString
#

def writeFilterToString(filter):
    result = create_string_buffer(b'\000' * 128)
    rv = lib.vscphlp_writeFilterToString( byref(filter), result )
    return rv, result.value.decode('utf-8')

###############################################################################
# writeMaskToString
#

def writeMaskToString(filter):
    result = create_string_buffer(b'\000' * 128)
    rv = lib.vscphlp_writeMaskToString( byref(filter), result )
    return rv, result.value.decode('utf-8')

###############################################################################
# doLevel2Filter
#
# Check an event against a filter. Returns non-zero if the event should
# be delivered.
#

def doLevel2Filter(e, filter):
    return lib.vscphlp_doLevel2Filter( byref(e), byref(filter) )


# -----------------------------------------------------------------------------
#                              CANAL Helpers
# -----------------------------------------------------------------------------


###############################################################################
# convertCanalToEvent
#

def convertCanalToEvent(e, canalMsg, guid):
    return lib.vscphlp_convertCanalToEvent( byref(e), byref(canalMsg), guid )

###############################################################################
# convertCanalToEventEx
#

def convertCanalToEventEx(ex, canalMsg, guid):
    return lib.vscphlp_convertCanalToEventEx( byref(ex), byref(canalMsg), guid )

###############################################################################
# convertEventToCanal
#

def convertEventToCanal(canalMsg, e):
    return lib.vscphlp_convertEventToCanal( byref(canalMsg), byref(e) )

###############################################################################
# convertEventExToCanal
#

def convertEventExToCanal(canalMsg, ex):
    return lib.vscphlp_convertEventExToCanal( byref(canalMsg), byref(ex) )



# -----------------------------------------------------------------------------
#                              GUID Helpers
# -----------------------------------------------------------------------------

def convertGuidToString(guid):
    result = create_string_buffer(b'\000' * 64)
    result_len = c_size_t(len(result))
    rv = lib.vscphlp_convertGuidToString(byref(guid), result, result_len)
    s = result.value.decode('utf-8')
    return rv, s

def convertStringToGuid(str):
    bstr = str.encode('utf-8')
    guid = (c_ubyte * 16)()
    rv = lib.vscphlp_convertStringToGuid(c_char_p(bstr), byref(guid))
    return rv, guid

def isGuidEmpty(guid):
    rv = lib.vscphlp_isGUIDEmpty(byref(guid))
    return rv

def clearGuid(guid):
    rv = lib.vscphlp_clearGuid(byref(guid))
    return rv

def compareGuids(guid1, guid2):
    rv = lib.vscphlp_compareGuids(byref(guid1), byref(guid2))
    return rv

def isSameGuid(guid1, guid2):
    rv = lib.vscphlp_isSameGUID(byref(guid1), byref(guid2))
    return rv

def copyGuid(dest, src):
    rv = lib.vscphlp_copyGuid(byref(dest), byref(src))
    return rv

def isValidGuid(guid):
    rv = lib.vscphlp_isValidGuid(byref(guid))
    return rv

def generateNewGuid(guid):
    rv = lib.vscphlp_generateNewGuid(byref(guid))
    return rv

def parseGuid(str):
    bstr = str.encode('utf-8')
    guid = (c_ubyte * 16)()
    rv = lib.vscphlp_parseGuid(byref(guid), c_char_p(bstr))
    return rv, guid

###############################################################################
# reverseGUID
#

def reverseGUID(guid):
    return lib.vscphlp_reverseGUID( guid )

###############################################################################
# calcCRC4GUIDArray
#

def calcCRC4GUIDArray(guid):
    lib.vscphlp_calcCRC4GUIDArray.restype = c_ubyte
    return lib.vscphlp_calcCRC4GUIDArray( guid )

###############################################################################
# calcCRC4GUIDString
#

def calcCRC4GUIDString(strguid):
    lib.vscphlp_calcCRC4GUIDString.restype = c_ubyte
    return lib.vscphlp_calcCRC4GUIDString( c_char_p(strguid.encode('utf-8')) )

###############################################################################
# getGuidFromString
#
# Set the GUID of an event from a GUID string
#

def getGuidFromString(e, str):
    return lib.vscphlp_getGuidFromString( byref(e), c_char_p(str.encode('utf-8')) )

###############################################################################
# getGuidFromStringEx
#

def getGuidFromStringEx(ex, str):
    return lib.vscphlp_getGuidFromStringEx( byref(ex), c_char_p(str.encode('utf-8')) )

###############################################################################
# getGuidFromStringToArray
#

def getGuidFromStringToArray(str):
    guid = (c_ubyte * 16)()
    rv = lib.vscphlp_getGuidFromStringToArray( guid, c_char_p(str.encode('utf-8')) )
    return rv, guid

###############################################################################
# writeGuidToString
#
# Write the GUID of an event to a string
#

def writeGuidToString(e):
    result = create_string_buffer(b'\000' * 64)
    rv = lib.vscphlp_writeGuidToString( byref(e), result, c_size_t(len(result)) )
    return rv, result.value.decode('utf-8')

###############################################################################
# writeGuidToStringEx
#

def writeGuidToStringEx(ex):
    result = create_string_buffer(b'\000' * 64)
    rv = lib.vscphlp_writeGuidToStringEx( byref(ex), result, c_size_t(len(result)) )
    return rv, result.value.decode('utf-8')

###############################################################################
# writeGuidToString4Rows
#

def writeGuidToString4Rows(e):
    result = create_string_buffer(b'\000' * 128)
    rv = lib.vscphlp_writeGuidToString4Rows( byref(e), result, c_int(len(result)) )
    return rv, result.value.decode('utf-8')

###############################################################################
# writeGuidToString4RowsEx
#

def writeGuidToString4RowsEx(ex):
    result = create_string_buffer(b'\000' * 128)
    rv = lib.vscphlp_writeGuidToString4RowsEx( byref(ex), result, c_size_t(len(result)) )
    return rv, result.value.decode('utf-8')

###############################################################################
# writeGuidArrayToString
#

def writeGuidArrayToString(guid):
    result = create_string_buffer(b'\000' * 64)
    rv = lib.vscphlp_writeGuidArrayToString( guid, result, c_size_t(len(result)) )
    return rv, result.value.decode('utf-8')


# -----------------------------------------------------------------------------
#                       UDP / Multicast / Encryption
# -----------------------------------------------------------------------------


###############################################################################
# getEncryptionCodeFromToken
#

def getEncryptionCodeFromToken(token):
    code = c_int()
    rv = lib.vscphlp_getEncryptionCodeFromToken( c_char_p(token.encode('utf-8')), byref(code) )
    return rv, code.value

###############################################################################
# getEncryptionTokenFromCode
#

def getEncryptionTokenFromCode(code):
    result = create_string_buffer(b'\000' * 64)
    rv = lib.vscphlp_getEncryptionTokenFromCode( c_int(code), result, c_size_t(len(result)) )
    return rv, result.value.decode('utf-8')

###############################################################################
# encryptVscpUdpFrame
#
# Encrypt a VSCP UDP frame. key is 16/24/32 bytes depending on algorithm,
# iv is 16 bytes.
#

def encryptVscpUdpFrame(input, key, iv, algorithm):
    inbuf = (c_ubyte * len(input))(*input)
    outbuf = (c_ubyte * (len(input) + 32))()
    keybuf = (c_ubyte * len(key))(*key)
    ivbuf = (c_ubyte * len(iv))(*iv)
    rv = lib.vscphlp_encryptVscpUdpFrame( outbuf,
                                            inbuf,
                                            c_size_t(len(input)),
                                            keybuf,
                                            ivbuf,
                                            c_ubyte(algorithm) )
    return rv, bytearray(outbuf)

###############################################################################
# decryptVscpUdpFrame
#

def decryptVscpUdpFrame(input, key, iv, algorithm):
    inbuf = (c_ubyte * len(input))(*input)
    outbuf = (c_ubyte * (len(input) + 32))()
    keybuf = (c_ubyte * len(key))(*key)
    ivbuf = (c_ubyte * len(iv))(*iv)
    rv = lib.vscphlp_decryptVscpUdpFrame( outbuf,
                                            inbuf,
                                            c_size_t(len(input)),
                                            keybuf,
                                            ivbuf,
                                            c_ubyte(algorithm) )
    return rv, bytearray(outbuf)

###############################################################################
# getUdpFrameSizeFromEvent
#

def getUdpFrameSizeFromEvent(e):
    lib.vscphlp_getUDpFrameSizeFromEvent.restype = c_size_t
    return lib.vscphlp_getUDpFrameSizeFromEvent( byref(e) )

###############################################################################
# getUdpFrameSizeFromEventEx
#

def getUdpFrameSizeFromEventEx(ex):
    lib.vscphlp_getUDpFrameSizeFromEventEx.restype = c_size_t
    return lib.vscphlp_getUDpFrameSizeFromEventEx( byref(ex) )

###############################################################################
# writeEventToUdpFrame
#

def writeEventToUdpFrame(e, pkttype):
    lib.vscphlp_getUDpFrameSizeFromEvent.restype = c_size_t
    size = lib.vscphlp_getUDpFrameSizeFromEvent( byref(e) )
    frame = (c_ubyte * size)()
    rv = lib.vscphlp_writeEventToUdpFrame( frame, c_size_t(size), c_ubyte(pkttype), byref(e) )
    return rv, bytearray(frame)

###############################################################################
# writeEventExToUdpFrame
#

def writeEventExToUdpFrame(ex, pkttype):
    lib.vscphlp_getUDpFrameSizeFromEventEx.restype = c_size_t
    size = lib.vscphlp_getUDpFrameSizeFromEventEx( byref(ex) )
    frame = (c_ubyte * size)()
    rv = lib.vscphlp_writeEventExToUdpFrame( frame, c_size_t(size), c_ubyte(pkttype), byref(ex) )
    return rv, bytearray(frame)



