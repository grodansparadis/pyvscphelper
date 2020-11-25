# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import sys
import math
from ctypes import *
import _ctypes
import binascii
import json
from xml.dom.minidom import parse, parseString

sys.path.append('../../pyvscp')
import vscp

sys.path.append('../../pyvscpclasses')
import vscp_class as vc

sys.path.append('../../pyvscptypes')
import vscp_type as vt

sys.path.append('..')
import vscphelper as vhlp


# -----------------------------------------------------------------------------
def test_connect():
    print("New session")
    h1 = vhlp.newSession()
    assert h1 != 0
    print(h1)
    if (0 == h1 ):
        print("Failed to open new session")
    rv = vhlp.open(h1,"192.168.1.7:9598","admin","secret")
    print("connected rv=",rv)
    vhlp.close(h1)
    print("closed")
    assert True
    print("Close session")
    vhlp.closeSession(h1)


# -----------------------------------------------------------------------------
def test_conversions():
    value = 3.14
    ba = vhlp.float2ByteArray(value)
    f = vhlp.byteArray2Float(ba)
    print(f)
    print([ "0x%02x" % b for b in ba ])
    assert ba[0] == 0x40
    assert ba[1] == 0x48
    assert ba[2] == 0xf5
    assert ba[3] == 0xc3
    ba = vhlp.double2ByteArray(value)
    d = vhlp.byteArray2Double(ba)
    print(d)
    print([ "0x%02x" % b for b in ba ])
    assert ba[0] == 0x40
    assert ba[1] == 0x09
    assert ba[2] == 0x1e
    assert ba[3] == 0xb8
    assert ba[4] == 0x51
    assert ba[5] == 0xeb
    assert ba[6] == 0x85
    assert ba[7] == 0x1f

    ba = vhlp.string2ByteArray("412.45")
    print([ "0x%02x" % b for b in ba ])

    ba1 = bytearray([0,1,2,3,4,5,6,7,8,9])
    ba2 = bytearray([11,22,33])
    print(len(ba1))
    ba = vhlp.byteArrayToPos(ba1,3,ba2)
    print([ "0x%02x" % b for b in ba ])
    print([ "0x%02x" % b for b in ba1 ])


# -----------------------------------------------------------------------------
def test_struct_conversions():

    e = vscp.vscpEvent()
    e.timestamp = 0
    e.vscpclass = 20
    e.vscptype = 9
    e.sizedata = 3
    p = (c_ubyte*3)()
    p[0] = 11
    p[1] = 22
    p[2] = 33
    e.pdata = cast(p, POINTER(c_ubyte))
    (rv,s) = vhlp.convertEventToJSON(e)
    e.pdata = None
    print("rv=",rv,"str=",json.dumps(s, sort_keys=True, indent=4))
    d = json.loads(s)
    print("VSCP Class:", d["vscpClass"], "VSCP Type:", d["vscpType"])

    e = vscp.vscpEvent()
    e.timestamp = 0
    e.vscpclass = 20
    e.vscptype = 9
    e.sizedata = 3
    p = (c_ubyte*3)()
    p[0] = 11
    p[1] = 22
    p[2] = 33
    e.pdata = cast(p, POINTER(c_ubyte))
    (rv,s) = vhlp.convertEventToXML(e)
    e.pdata = None
    print("rv=",rv,"str=",s)

# -----------------------------------------------------------------------------
def test_makeFloatMeasurementEvent():

    e = vscp.vscpEvent()
    e.sizedata = 0
    e.vscpclass = vc.VSCP_CLASS1_MEASUREMENT
    e.vscptype = vt.VSCP_TYPE_MEASUREMENT_TEMPERATURE
    value = 3.14
    unit = 2
    sensorindex = 1
    rv = vhlp.makeFloatMeasurementEvent( e, value, unit, sensorindex )
    print("Return value = ",rv)
    assert rv == vscp.VSCP_ERROR_SUCCESS

# -----------------------------------------------------------------------------
def test_makeFloatMeasurementEventEx():
    ex = vscp.vscpEventEx()
    ex.sizedata = 0
    ex.vscpclass = vc.VSCP_CLASS1_MEASUREMENT
    ex.vscptype = vt.VSCP_TYPE_MEASUREMENT_TEMPERATURE
    value = 3.14
    unit = 2
    sensorindex = 1
    rv = vhlp.makeFloatMeasurementEventEx( ex, value, unit, sensorindex )
    print("Return value = ",rv)
    assert rv == vscp.VSCP_ERROR_SUCCESS

# -----------------------------------------------------------------------------
def test_makeStringMeasurementEvent():

    e = vscp.vscpEvent()
    e.sizedata = 0
    e.vscpclass = vc.VSCP_CLASS1_MEASUREMENT
    e.vscptype = vt.VSCP_TYPE_MEASUREMENT_TEMPERATURE
    value = 3.14
    unit = 2
    sensorindex = 1
    rv = vhlp.makeStringMeasurementEvent( e, value, unit, sensorindex )
    print("Return value = ",rv)
    assert rv == vscp.VSCP_ERROR_SUCCESS

# -----------------------------------------------------------------------------
def test_makeStringMeasurementEventEx():

    ex = vscp.vscpEventEx()
    ex.sizedata = 0
    ex.vscpclass = vc.VSCP_CLASS1_MEASUREMENT
    ex.vscptype = vt.VSCP_TYPE_MEASUREMENT_TEMPERATURE
    value = 3.14
    unit = 2
    sensorindex = 1
    rv = vhlp.makeStringMeasurementEventEx( ex, value, unit, sensorindex )
    print("Return value = ",rv)
    assert rv == vscp.VSCP_ERROR_SUCCESS

# -----------------------------------------------------------------------------
def test_makeLevel2FloatMeasurementEvent():

    e = vscp.vscpEvent()
    e.sizedata = 0
    e.vscpclass = vc.VSCP_CLASS1_MEASUREMENT
    e.vscptype = vt.VSCP_TYPE_MEASUREMENT_TEMPERATURE
    value = 3.14
    unit = 2
    sensorindex = 1
    zone = 11
    subzone = 22
    rv = vhlp.makeLevel2FloatMeasurementEvent( e, vt.VSCP_TYPE_MEASUREMENT_TEMPERATURE, 
                                                value, unit, sensorindex, zone, subzone  )
    print("Return value = ",rv)
    assert rv == vscp.VSCP_ERROR_SUCCESS

# -----------------------------------------------------------------------------
def test_makeLevel2FloatMeasurementEventEx():

    ex = vscp.vscpEvent()
    ex.sizedata = 0
    ex.vscpclass = vc.VSCP_CLASS1_MEASUREMENT
    ex.vscptype = vt.VSCP_TYPE_MEASUREMENT_TEMPERATURE
    value = 3.14
    unit = 2
    sensorindex = 1
    zone = 11
    subzone = 22
    rv = vhlp.makeLevel2FloatMeasurementEvent( ex, vt.VSCP_TYPE_MEASUREMENT_TEMPERATURE, 
                                                value, unit, sensorindex, zone, subzone  )
    print("Return value = ",rv)
    assert rv == vscp.VSCP_ERROR_SUCCESS

# -----------------------------------------------------------------------------
def test_makeLevel2StringMeasurementEvent():

    e = vscp.vscpEvent()
    e.sizedata = 0
    e.vscpclass = vc.VSCP_CLASS1_MEASUREMENT
    e.vscptype = vt.VSCP_TYPE_MEASUREMENT_TEMPERATURE
    value = 3.14
    unit = 2
    sensorindex = 1
    zone = 11
    subzone = 22
    rv = vhlp.makeLevel2StringMeasurementEvent( e, vt.VSCP_TYPE_MEASUREMENT_TEMPERATURE, 
                                                value, unit, sensorindex, zone, subzone  )
    print("Return value = ",rv)
    assert rv == vscp.VSCP_ERROR_SUCCESS

# -----------------------------------------------------------------------------
def test_makeLevel2StringMeasurementEventEx():

    ex = vscp.vscpEvent()
    ex.sizedata = 0
    ex.vscpclass = vc.VSCP_CLASS1_MEASUREMENT
    ex.vscptype = vt.VSCP_TYPE_MEASUREMENT_TEMPERATURE
    value = 3.14
    unit = 2
    sensorindex = 1
    zone = 11
    subzone = 22
    rv = vhlp.makeLevel2StringMeasurementEventEx( ex, vt.VSCP_TYPE_MEASUREMENT_TEMPERATURE, 
                                                    value, unit, sensorindex, zone, subzone  )
    print("Return value = ",rv)
    assert rv == vscp.VSCP_ERROR_SUCCESS

# -----------------------------------------------------------------------------
def test_convertLevel1MeasuremenToLevel2Double():

    e = vscp.vscpEvent()

    e.vscpclass = vc.VSCP_CLASS1_MEASUREMENT
    e.vscptype = vt.VSCP_TYPE_MEASUREMENT_TEMPERATURE

    # 32-bit float coding = 100
    e.sizedata = 4
    p = (c_ubyte*4)()
    p[0] = 0x80
    p[1] = 0x02
    p[2] = 0x1B
    p[3] = 0x22
    e.pdata = cast(p, POINTER(c_ubyte))

    # IMPORTANT     TODO
    # ---------
    # Will give invalid free as the data structure size is changed
    # in the lib. Have no solution on this yet.
    rv = vhlp.convertLevel1MeasuremenToLevel2Double( e )
    p = None
    #print("Return value = ",rv)
    assert rv == vscp.VSCP_ERROR_SUCCESS


# -----------------------------------------------------------------------------
def test_convertLevel1MeasuremenToLevel2DoubleEx():

    e = vscp.vscpEventEx()

    e.vscpclass = vc.VSCP_CLASS1_MEASUREMENT
    e.vscptype = vt.VSCP_TYPE_MEASUREMENT_TEMPERATURE

    # 32-bit float coding = 100
    e.sizedata = 4
    e.data[0] = 0x80
    e.data[1] = 0x02
    e.data[2] = 0x1B
    e.data[3] = 0x22
    rv = vhlp.convertLevel1MeasuremenToLevel2DoubleEx( e )
    print("Return value = ",rv)
    assert rv == vscp.VSCP_ERROR_SUCCESS

# -----------------------------------------------------------------------------
def test_convertLevel1MeasuremenToLevel2String():

    e = vscp.vscpEvent()

    e.vscpclass = vc.VSCP_CLASS1_MEASUREMENT
    e.vscptype = vt.VSCP_TYPE_MEASUREMENT_TEMPERATURE

    # 32-bit float coding = 100
    e.sizedata = 4
    p = (c_ubyte*4)()
    p[0] = 0x80
    p[1] = 0x02
    p[2] = 0x1B
    p[3] = 0x22
    e.pdata = cast(p, POINTER(c_ubyte))

    # IMPORTANT    TODO
    # ---------
    # Will give invalid free as the data structure size is changed
    # in the lib. Have no solution on this yet.
    rv = vhlp.convertLevel1MeasuremenToLevel2String( e )
    print("Return value = ",rv)
    assert rv == vscp.VSCP_ERROR_SUCCESS


# -----------------------------------------------------------------------------
def test_convertLevel1MeasuremenToLevel2StringEx():

    e = vscp.vscpEventEx()

    e.vscpclass = vc.VSCP_CLASS1_MEASUREMENT
    e.vscptype = vt.VSCP_TYPE_MEASUREMENT_TEMPERATURE

    # 32-bit float coding = 100
    e.sizedata = 4
    e.data[0] = 0x80
    e.data[1] = 0x02
    e.data[2] = 0x1B
    e.data[3] = 0x22
    rv = vhlp.convertLevel1MeasuremenToLevel2StringEx( e )
    print("Return value = ",rv)
    assert rv == vscp.VSCP_ERROR_SUCCESS

#------------------------------------------------------------------------------
def test_convertEventToJSON() :

    e = vscp.vscpEvent()

    e.vscpclass = vc.VSCP_CLASS1_MEASUREMENT
    e.vscptype = vt.VSCP_TYPE_MEASUREMENT_TEMPERATURE

    # 32-bit float coding = 100
    e.sizedata = 4
    p = (c_ubyte*4)()
    p[0] = 0x80
    p[1] = 0x02
    p[2] = 0x1B
    p[3] = 0x22
    e.pdata = cast(p, POINTER(c_ubyte))

    rv,s = vhlp.convertEventToJSON( e )
    print(rv)
    print(s)
    assert rv == vscp.VSCP_ERROR_SUCCESS
    j = json.loads(s)
    print("class = ",j["vscpClass"])
    assert 10 == j["vscpClass"]
    print("Type = ", j["vscpType"])
    assert 6 == j["vscpType"]
    assert 0x80 == j["vscpData"][0]
    assert 0x02 == j["vscpData"][1]
    assert 0x1B == j["vscpData"][2]
    assert 0x22 == j["vscpData"][3]

#------------------------------------------------------------------------------
def test_convertEventExToJSON() :
    ex = vscp.vscpEventEx()

    ex.vscpclass = vc.VSCP_CLASS1_MEASUREMENT
    ex.vscptype = vt.VSCP_TYPE_MEASUREMENT_TEMPERATURE

    # 32-bit float coding = 100
    ex.sizedata = 4
    ex.data[0] = 11
    ex.data[1] = 22
    ex.data[2] = 33
    ex.data[3] = 44
    rv,s = vhlp.convertEventExToJSON( ex )
    print(rv)
    print(s)
    assert rv == vscp.VSCP_ERROR_SUCCESS
    j = json.loads(s)
    print("class = ",j["vscpClass"])
    assert 10 == j["vscpClass"]
    print("Type = ", j["vscpType"])
    assert 6 == j["vscpType"]
    assert 11 == j["vscpData"][0]
    assert 22 == j["vscpData"][1]
    assert 33 == j["vscpData"][2]
    assert 44 == j["vscpData"][3]

# -----------------------------------------------------------------------------
def test_convertEventToXML() :

    e = vscp.vscpEvent()

    e.vscpclass = vc.VSCP_CLASS1_MEASUREMENT
    e.vscptype = vt.VSCP_TYPE_MEASUREMENT_TEMPERATURE

    # 32-bit float coding = 100
    e.sizedata = 4
    p = (c_ubyte*4)()
    p[0] = 0x80
    p[1] = 0x02
    p[2] = 0x1B
    p[3] = 0x22
    e.pdata = cast(p, POINTER(c_ubyte))

    rv,s = vhlp.convertEventToXML( e )
    print(rv)
    print(s)
    assert rv == vscp.VSCP_ERROR_SUCCESS
    x = parseString(s)
    item = x.getElementsByTagName('event')
    print(len(item))
    print(item[0].attributes['vscpGuid'].value)
    #for s in item:
    #    print(s.attributes['vscpGuid'].value)
    print("class = ", item[0].attributes['vscpClass'].value)
    assert 10 == int(item[0].attributes['vscpClass'].value)
    print("type = ", item[0].attributes['vscpType'].value)
    assert 6 == int(item[0].attributes['vscpType'].value)
    b = item[0].attributes['vscpData'].value.split(',')
    print(b[0],int(b[0],16))
    assert 0x80 == int(b[0],16)
    assert 0x02 == int(b[1],16)
    assert 0x1B == int(b[2],16)
    assert 0x22 == int(b[3],16)

# -----------------------------------------------------------------------------
def test_convertEventExToXML() :
    ex = vscp.vscpEventEx()

    ex.vscpclass = vc.VSCP_CLASS1_MEASUREMENT
    ex.vscptype = vt.VSCP_TYPE_MEASUREMENT_TEMPERATURE

    # 32-bit float coding = 100
    ex.sizedata = 4
    ex.data[0] = 11
    ex.data[1] = 22
    ex.data[2] = 33
    ex.data[3] = 44
    rv,s = vhlp.convertEventExToXML( ex )
    print(rv)
    print(s)
    assert rv == vscp.VSCP_ERROR_SUCCESS
    x = parseString(s)
    item = x.getElementsByTagName('event')
    print(len(item))
    print(item[0].attributes['vscpGuid'].value)
    #for s in item:
    #    print(s.attributes['vscpGuid'].value)
    print("class = ", item[0].attributes['vscpClass'].value)
    assert 10 == int(item[0].attributes['vscpClass'].value)
    print("type = ", item[0].attributes['vscpType'].value)
    assert 6 == int(item[0].attributes['vscpType'].value)
    b = item[0].attributes['vscpData'].value.split(',')
    print(b[0],int(b[0],16))
    assert 11 == int(b[0],16)
    assert 22 == int(b[1],16)
    assert 33 == int(b[2],16)
    assert 44 == int(b[3],16)

# -----------------------------------------------------------------------------
def test_convertEventToHTML() :

    e = vscp.vscpEvent()

    e.vscpclass = vc.VSCP_CLASS1_MEASUREMENT
    e.vscptype = vt.VSCP_TYPE_MEASUREMENT_TEMPERATURE

    # 32-bit float coding = 100
    e.sizedata = 4
    p = (c_ubyte*4)()
    p[0] = 0x80
    p[1] = 0x02
    p[2] = 0x1B
    p[3] = 0x22
    e.pdata = cast(p, POINTER(c_ubyte))

    rv,s = vhlp.convertEventToHTML( e )
    print(rv)
    print(s)
    assert rv == vscp.VSCP_ERROR_SUCCESS
    assert -1 != s.find('Class: 10 ')
    assert -1 != s.find('Type: 6 ')
    assert -1 != s.find('<p>Data count: 4<br>Data: 0x80,0x02,0x1B,0x22<br></p>')

# -----------------------------------------------------------------------------
def test_convertEventExToHTML() :
    ex = vscp.vscpEventEx()

    ex.vscpclass = vc.VSCP_CLASS1_MEASUREMENT
    ex.vscptype = vt.VSCP_TYPE_MEASUREMENT_TEMPERATURE

    # 32-bit float coding = 100
    ex.sizedata = 4
    ex.data[0] = 11
    ex.data[1] = 22
    ex.data[2] = 33
    ex.data[3] = 44
    rv,s = vhlp.convertEventExToHTML( ex )
    print(rv)
    print(s)
    assert rv == vscp.VSCP_ERROR_SUCCESS
    assert -1 != s.find('Class: 10 ')
    assert -1 != s.find('Type: 6 ')
    assert -1 != s.find('<p>Data count: 4<br>Data: 0x0B,0x16,0x21,0x2C<br></p>')

# -----------------------------------------------------------------------------
def test_convertEventToString() :
    e = vscp.vscpEvent()

    e.vscpclass = vc.VSCP_CLASS1_MEASUREMENT
    e.vscptype = vt.VSCP_TYPE_MEASUREMENT_TEMPERATURE

    # 32-bit float coding = 100
    e.sizedata = 4
    p = (c_ubyte*4)()
    p[0] = 0x80
    p[1] = 0x02
    p[2] = 0x1B
    p[3] = 0x22
    e.pdata = cast(p, POINTER(c_ubyte))

    rv,s = vhlp.convertEventToString( e )
    print(rv)
    print(s)
    assert rv == vscp.VSCP_ERROR_SUCCESS
    assert -1 != s.find('0,10,6,0,')
    assert -1 != s.find(',00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00,0x80,0x02,0x1B,0x22')

# -----------------------------------------------------------------------------
def test_convertEventExToString() :
    ex = vscp.vscpEventEx()

    ex.vscpclass = vc.VSCP_CLASS1_MEASUREMENT
    ex.vscptype = vt.VSCP_TYPE_MEASUREMENT_TEMPERATURE

    # 32-bit float coding = 100
    ex.sizedata = 4
    ex.data[0] = 11
    ex.data[1] = 22
    ex.data[2] = 33
    ex.data[3] = 44
    rv,s = vhlp.convertEventExToString( ex )
    print(rv)
    print(s)
    assert rv == vscp.VSCP_ERROR_SUCCESS
    assert -1 != s.find('0,10,6,0,')
    assert -1 != s.find(',00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00,0x0B,0x16,0x21,0x2C')

# -----------------------------------------------------------------------------
def test_convertStringToEvent():
    e = vscp.vscpEvent()
    str = "0,10,6,0,2020-11-24T17:28:11Z,4216090068,00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00,0x80,0x02,0x1B,0x22"
    rv,e = vhlp.convertStringToEvent( e, str )
    print(rv)
    #print(e.dump())
    assert rv == vscp.VSCP_ERROR_SUCCESS
    assert e.vscpclass == 10
    assert e.vscptype == 6
    assert e.timestamp == 4216090068
    assert e.year == 2020
    assert e.month == 11
    assert e.day == 24
    assert e.hour == 17
    assert e.minute == 28
    assert e.second == 11
    assert e.pdata[0] == 128
    assert e.pdata[1] == 2
    assert e.pdata[2] == 0x1b
    assert e.pdata[3] == 0x22

# -----------------------------------------------------------------------------
def test_convertStringToEventEx():
    ex = vscp.vscpEventEx()
    str = "0,10,6,0,2020-11-24T17:28:11Z,4216090068,00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00,0x0B,0x16,0x21,0x2C"
    rv,e2 = vhlp.convertStringToEventEx( ex, str )
    print(rv)
    print(e2.dump())
    assert rv == vscp.VSCP_ERROR_SUCCESS
    assert e2.vscpclass == 10
    assert e2.vscptype == 6
    assert e2.timestamp == 4216090068
    assert e2.year == 2020
    assert e2.month == 11
    assert e2.day == 24
    assert e2.hour == 17
    assert e2.minute == 28
    assert e2.second == 11
    assert e2.data[0] == 11
    assert e2.data[1] == 0x16
    assert e2.data[2] == 0x21
    assert e2.data[3] == 0x2c

# -----------------------------------------------------------------------------
def test_getDateStringFromEvent() :
    e = vscp.vscpEvent()

    e.vscpclass = vc.VSCP_CLASS1_MEASUREMENT
    e.vscptype = vt.VSCP_TYPE_MEASUREMENT_TEMPERATURE

    # 32-bit float coding = 100
    e.sizedata = 4
    p = (c_ubyte*4)()
    p[0] = 0x80
    p[1] = 0x02
    p[2] = 0x1B
    p[3] = 0x22
    e.pdata = cast(p, POINTER(c_ubyte))

    rv,s = vhlp.getDateStringFromEvent( e )
    print(rv)
    print(s)
    assert rv == vscp.VSCP_ERROR_SUCCESS

# -----------------------------------------------------------------------------
def test_getDateStringFromEventEx() :
    ex = vscp.vscpEventEx()

    ex.vscpclass = vc.VSCP_CLASS1_MEASUREMENT
    ex.vscptype = vt.VSCP_TYPE_MEASUREMENT_TEMPERATURE

    # 32-bit float coding = 100
    ex.sizedata = 4
    ex.data[0] = 11
    ex.data[1] = 22
    ex.data[2] = 33
    ex.data[3] = 44
    rv,s = vhlp.getDateStringFromEventEx( ex )
    print(rv)
    print(s)
    assert rv == vscp.VSCP_ERROR_SUCCESS


# -----------------------------------------------------------------------------
#                                    The END
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
if __name__ == "__main__":
    test_connect()
    test_conversions()
    test_struct_conversions()
    test_makeFloatMeasurementEvent()
    test_makeFloatMeasurementEventEx()
    test_makeStringMeasurementEvent()
    test_makeStringMeasurementEventEx()
    test_makeLevel2FloatMeasurementEvent()
    test_makeLevel2FloatMeasurementEventEx()
    test_makeLevel2StringMeasurementEvent()
    test_makeLevel2StringMeasurementEventEx()
    # ***** Fails to release pointer
    #test_convertLevel1MeasuremenToLevel2Double()
    test_convertLevel1MeasuremenToLevel2DoubleEx()
    # ***** Fails to release pointer
    #test_convertLevel1MeasuremenToLevel2String()
    test_convertLevel1MeasuremenToLevel2StringEx()
    test_convertEventToJSON()
    test_convertEventExToJSON()
    test_convertEventToXML()
    test_convertEventExToXML()
    test_convertEventToHTML()
    test_convertEventExToHTML()
    test_convertEventToString() 
    test_convertEventExToString()
    test_convertStringToEvent()
    test_convertStringToEventEx()
    test_getDateStringFromEvent()
    test_getDateStringFromEventEx()

    print("Everything passed")