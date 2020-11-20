# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import sys
import math
from ctypes import *
import _ctypes
import json

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
    # rv = vhlp.convertLevel1MeasuremenToLevel2Double( e )
    # print("Return value = ",rv)
    # assert rv == vscp.VSCP_ERROR_SUCCESS


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
    test_convertLevel1MeasuremenToLevel2Double()
    test_convertLevel1MeasuremenToLevel2DoubleEx()
    test_convertLevel1MeasuremenToLevel2String()
    test_convertLevel1MeasuremenToLevel2StringEx()
    print("Everything passed")