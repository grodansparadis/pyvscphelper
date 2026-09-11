# FILE: test_functions.py
#
# Tests for the VSCP helper library bindings in vscphelper.py
#
# This file is part of the VSCP (http://www.vscp.org)
#
# Run with pytest from the tests folder, or directly with
# python test_functions.py
#
# Tests that need a remote VSCP daemon are collected in test_session()
# and are skipped if no server can be reached. Set VSCP_HOST, VSCP_USER
# and VSCP_PASSWORD in the environment to point at a test server.

import os
import sys
import time
from ctypes import *

sys.path.append('../../pyvscp')
import vscp

sys.path.append('../../pyvscpclasses')
import vscp_class as vc

sys.path.append('../../pyvscptypes')
import vscp_type as vt

sys.path.append('..')
import vscphelper as vhlp

GUID_STR = "FF:FF:FF:FF:FF:FF:FF:F5:00:00:00:00:00:00:00:01"


# canalMsg structure from canal.h
class canalMsg(Structure):
    _fields_ = [("flags", c_ulong),
                ("obid", c_ulong),
                ("id", c_ulong),
                ("sizeData", c_ubyte),
                ("data", c_ubyte * 8),
                ("timestamp", c_ulong)]


# Some functions are not exported by all versions of libvscphelper
def has_symbol(name):
    return hasattr(vhlp.lib, name)


# -----------------------------------------------------------------------------
#                              General helpers
# -----------------------------------------------------------------------------

def test_readStringValue():
    assert 42 == vhlp.readStringValue("42")
    assert 0x22 == vhlp.readStringValue("0x22")

# -----------------------------------------------------------------------------
def test_replaceBackslash():
    rv, s = vhlp.replaceBackslash("a\\b\\c")
    print(rv, s)
    assert s == "a/b/c"

# -----------------------------------------------------------------------------
def test_vscpPriority():
    e = vscp.vscpEvent()
    vhlp.setVscpPriority(e, 3)
    assert 3 == vhlp.getVscpPriority(e)

# -----------------------------------------------------------------------------
def test_vscpPriorityEx():
    ex = vscp.vscpEventEx()
    vhlp.setVscpPriorityEx(ex, 5)
    assert 5 == vhlp.getVscpPriorityEx(ex)

# -----------------------------------------------------------------------------
def test_CANALid():
    canalid = vhlp.getCANALidFromData(7, 10, 6)
    print("canalid = 0x%08X" % canalid)
    assert 10 == vhlp.getVSCPclassFromCANALid(canalid)
    assert 6 == vhlp.getVSCPtypeFromCANALid(canalid)
    assert 0 == vhlp.getVSCPnicknameFromCANALid(canalid)
    head = vhlp.getVSCPheadFromCANALid(canalid)
    print("head = 0x%02X" % head)
    assert 7 == (head >> 5)

# -----------------------------------------------------------------------------
def test_getCANALidFromEvent():
    e = vscp.vscpEvent()
    e.vscpclass = 10
    e.vscptype = 6
    e.guid[15] = 42
    canalid = vhlp.getCANALidFromEvent(e)
    assert 10 == vhlp.getVSCPclassFromCANALid(canalid)
    assert 6 == vhlp.getVSCPtypeFromCANALid(canalid)

# -----------------------------------------------------------------------------
def test_getCANALidFromEventEx():
    ex = vscp.vscpEventEx()
    ex.vscpclass = 10
    ex.vscptype = 6
    ex.guid[15] = 42
    canalid = vhlp.getCANALidFromEventEx(ex)
    assert 10 == vhlp.getVSCPclassFromCANALid(canalid)
    assert 6 == vhlp.getVSCPtypeFromCANALid(canalid)

# -----------------------------------------------------------------------------
def test_calc_crc_Event():
    e = vscp.vscpEvent()
    e.vscpclass = 10
    e.vscptype = 6
    crc = vhlp.calc_crc_Event(e, 0)
    print("crc = 0x%04X" % crc)
    assert 0 <= crc <= 0xFFFF

# -----------------------------------------------------------------------------
def test_calc_crc_EventEx():
    ex = vscp.vscpEventEx()
    ex.vscpclass = 10
    ex.vscptype = 6
    crc = vhlp.calc_crc_EventEx(ex, 0)
    print("crc = 0x%04X" % crc)
    assert 0 <= crc <= 0xFFFF

# -----------------------------------------------------------------------------
def test_calcCRC4GUID():
    rv, guid = vhlp.getGuidFromStringToArray(GUID_STR)
    assert rv == vscp.VSCP_ERROR_SUCCESS
    crc_array = vhlp.calcCRC4GUIDArray(guid)
    crc_str = vhlp.calcCRC4GUIDString(GUID_STR)
    print("crc = 0x%02X" % crc_array)
    assert crc_array == crc_str

# -----------------------------------------------------------------------------
def test_convertVSCPtoEx():
    e = vscp.vscpEvent()
    e.vscpclass = 30
    e.vscptype = 5
    e.sizedata = 0
    ex = vscp.vscpEventEx()
    rv = vhlp.convertVSCPtoEx(ex, e)
    assert rv == vscp.VSCP_ERROR_SUCCESS
    assert 30 == ex.vscpclass
    assert 5 == ex.vscptype

# -----------------------------------------------------------------------------
def test_convertVSCPfromEx():
    ex = vscp.vscpEventEx()
    ex.vscpclass = 30
    ex.vscptype = 5
    ex.sizedata = 3
    ex.data[0] = 1
    ex.data[1] = 2
    ex.data[2] = 3
    e = vscp.vscpEvent()
    rv = vhlp.convertVSCPfromEx(e, ex)
    assert rv == vscp.VSCP_ERROR_SUCCESS
    assert 30 == e.vscpclass
    assert 5 == e.vscptype
    assert 3 == e.sizedata
    assert 1 == e.pdata[0]
    assert 2 == e.pdata[1]
    assert 3 == e.pdata[2]

# -----------------------------------------------------------------------------
def test_newVSCPevent_delete_v2():
    rv, pEvent = vhlp.newVSCPevent()
    assert rv == vscp.VSCP_ERROR_SUCCESS
    assert bool(pEvent)
    pEvent.contents.vscpclass = 10
    assert 10 == pEvent.contents.vscpclass
    vhlp.deleteVSCPevent_v2(pEvent)

# -----------------------------------------------------------------------------
def test_newVSCPevent_delete():
    rv, pEvent = vhlp.newVSCPevent()
    assert rv == vscp.VSCP_ERROR_SUCCESS
    assert bool(pEvent)
    vhlp.deleteVSCPevent(pEvent)

# -----------------------------------------------------------------------------
def test_deleteVSCPeventEx_available():
    # Can only be called safely with lib allocated events, so just make
    # sure the symbol is exported
    assert has_symbol('vscphlp_deleteVSCPeventEx')

# -----------------------------------------------------------------------------
def test_copyVSCPEvent():
    eFrom = vscp.vscpEvent()
    eFrom.vscpclass = 20
    eFrom.vscptype = 9
    eFrom.sizedata = 0
    eTo = vscp.vscpEvent()
    rv = vhlp.copyVSCPEvent(eTo, eFrom)
    assert rv == vscp.VSCP_ERROR_SUCCESS
    assert 20 == eTo.vscpclass
    assert 9 == eTo.vscptype

# -----------------------------------------------------------------------------
def test_makeTimeStamp():
    ts = vhlp.makeTimeStamp()
    print("timestamp =", ts)
    assert ts > 0

# -----------------------------------------------------------------------------
def test_setEventDateTimeBlockToNow():
    e = vscp.vscpEvent()
    e.year = 0
    rv = vhlp.setEventDateTimeBlockToNow(e)
    assert rv == vscp.VSCP_ERROR_SUCCESS
    assert e.year >= 2020

# -----------------------------------------------------------------------------
def test_setEventExDateTimeBlockToNow():
    ex = vscp.vscpEventEx()
    ex.year = 0
    rv = vhlp.setEventExDateTimeBlockToNow(ex)
    assert rv == vscp.VSCP_ERROR_SUCCESS
    assert ex.year >= 2020

# -----------------------------------------------------------------------------
def test_setEventToNow():
    if not has_symbol('vscphlp_setEventToNow'):
        print("symbol not exported by this libvscphelper - skipped")
        return
    e = vscp.vscpEvent()
    e.year = 0
    rv = vhlp.setEventToNow(e)
    assert rv == vscp.VSCP_ERROR_SUCCESS
    assert e.year >= 2020

# -----------------------------------------------------------------------------
def test_setEventExToNow():
    if not has_symbol('vscphlp_setEventExToNow'):
        print("symbol not exported by this libvscphelper - skipped")
        return
    ex = vscp.vscpEventEx()
    ex.year = 0
    rv = vhlp.setEventExToNow(ex)
    assert rv == vscp.VSCP_ERROR_SUCCESS
    assert ex.year >= 2020

# -----------------------------------------------------------------------------
def test_getTimeString():
    rv, s = vhlp.getTimeString(int(time.time()))
    print(rv, s)
    assert rv == vscp.VSCP_ERROR_SUCCESS
    assert len(s) > 0

# -----------------------------------------------------------------------------
def test_getISOTimeString():
    rv, s = vhlp.getISOTimeString(int(time.time()))
    print(rv, s)
    assert rv == vscp.VSCP_ERROR_SUCCESS
    assert len(s) > 0

# -----------------------------------------------------------------------------
def test_setVscpEventFromString():
    e = vscp.vscpEvent()
    s = "0,10,6,0,2020-11-24T17:28:11Z,4216090068," + \
        "00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00,0x80,0x02,0x1B,0x22"
    rv = vhlp.setVscpEventFromString(e, s)
    assert rv == vscp.VSCP_ERROR_SUCCESS
    assert 10 == e.vscpclass
    assert 6 == e.vscptype
    assert 4 == e.sizedata
    assert 0x80 == e.pdata[0]

# -----------------------------------------------------------------------------
def test_setVscpEventExFromString():
    ex = vscp.vscpEventEx()
    s = "0,10,6,0,2020-11-24T17:28:11Z,4216090068," + \
        "00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00,0x0B,0x16,0x21,0x2C"
    rv = vhlp.setVscpEventExFromString(ex, s)
    assert rv == vscp.VSCP_ERROR_SUCCESS
    assert 10 == ex.vscpclass
    assert 6 == ex.vscptype
    assert 4 == ex.sizedata
    assert 0x0B == ex.data[0]

# -----------------------------------------------------------------------------
def test_setVscpDataFromString():
    e = vscp.vscpEvent()
    rv = vhlp.setVscpDataFromString(e, "1,2,3")
    assert rv == vscp.VSCP_ERROR_SUCCESS
    assert 3 == e.sizedata
    assert 1 == e.pdata[0]
    assert 2 == e.pdata[1]
    assert 3 == e.pdata[2]

# -----------------------------------------------------------------------------
def test_getVscpDataFromString():
    if not has_symbol('vscphlp_getVscpDataFromString'):
        print("symbol not exported by this libvscphelper - skipped")
        return
    e = vscp.vscpEvent()
    rv = vhlp.getVscpDataFromString(e, "11,22,0x21")
    assert rv == vscp.VSCP_ERROR_SUCCESS
    assert 3 == e.sizedata
    assert 11 == e.pdata[0]
    assert 22 == e.pdata[1]
    assert 0x21 == e.pdata[2]

# -----------------------------------------------------------------------------
def test_getVscpDataArrayFromString():
    if not has_symbol('vscphlp_getVscpDataArrayFromString'):
        print("symbol not exported by this libvscphelper - skipped")
        return
    rv, data = vhlp.getVscpDataArrayFromString("1,2,0x03")
    assert rv == vscp.VSCP_ERROR_SUCCESS
    assert bytearray([1, 2, 3]) == data

# -----------------------------------------------------------------------------
def test_setVscpDataArrayFromString():
    rv, data = vhlp.setVscpDataArrayFromString("1,2,0x03")
    assert rv == vscp.VSCP_ERROR_SUCCESS
    assert bytearray([1, 2, 3]) == data

# -----------------------------------------------------------------------------
def test_writeVscpDataToString():
    e = vscp.vscpEvent()
    e.sizedata = 4
    p = (c_ubyte * 4)()
    p[0] = 11
    p[1] = 22
    p[2] = 33
    p[3] = 44
    e.pdata = cast(p, POINTER(c_ubyte))
    rv, s = vhlp.writeVscpDataToString(e)
    e.pdata = None
    print(rv, s)
    assert rv == vscp.VSCP_ERROR_SUCCESS
    assert -1 != s.find('0x0B')
    assert -1 != s.find('0x2C')

# -----------------------------------------------------------------------------
def test_writeVscpDataWithSizeToString():
    rv, s = vhlp.writeVscpDataWithSizeToString(bytearray([11, 22, 33, 44]))
    print(rv, s)
    assert rv == vscp.VSCP_ERROR_SUCCESS
    assert -1 != s.find('0x0B')
    assert -1 != s.find('0x2C')


# -----------------------------------------------------------------------------
#                              Filter helpers
# -----------------------------------------------------------------------------

def test_readFilterFromString():
    f = vscp.vscpEventFilter()
    rv = vhlp.readFilterFromString(f,
        "1,0x0000,0x0006,ff:ff:ff:ff:ff:ff:ff:01:00:00:00:00:00:00:00:00")
    assert rv == vscp.VSCP_ERROR_SUCCESS
    assert 1 == f.filter_priority
    assert 0 == f.filter_class
    assert 6 == f.filter_type
    assert 0xff == f.filter_guid[0]
    assert 0x01 == f.filter_guid[7]

# -----------------------------------------------------------------------------
def test_readMaskFromString():
    f = vscp.vscpEventFilter()
    rv = vhlp.readMaskFromString(f,
        "1,0x0000,0x0006,ff:ff:ff:ff:ff:ff:ff:01:00:00:00:00:00:00:00:00")
    assert rv == vscp.VSCP_ERROR_SUCCESS
    assert 1 == f.mask_priority
    assert 0 == f.mask_class
    assert 6 == f.mask_type
    assert 0xff == f.mask_guid[0]
    assert 0x01 == f.mask_guid[7]

# -----------------------------------------------------------------------------
def test_writeFilterToString():
    f = vscp.vscpEventFilter()
    f.filter_priority = 1
    f.filter_class = 10
    f.filter_type = 6
    rv, s = vhlp.writeFilterToString(f)
    print(rv, s)
    assert rv == vscp.VSCP_ERROR_SUCCESS
    assert len(s) > 0

# -----------------------------------------------------------------------------
def test_writeMaskToString():
    f = vscp.vscpEventFilter()
    f.mask_priority = 1
    f.mask_class = 0xffff
    f.mask_type = 0xffff
    rv, s = vhlp.writeMaskToString(f)
    print(rv, s)
    assert rv == vscp.VSCP_ERROR_SUCCESS
    assert len(s) > 0

# -----------------------------------------------------------------------------
def test_copyVSCPFilter():
    f1 = vscp.vscpEventFilter()
    f1.filter_class = 10
    f1.filter_type = 6
    f2 = vscp.vscpEventFilter()
    vhlp.copyVSCPFilter(f2, f1)
    assert 10 == f2.filter_class
    assert 6 == f2.filter_type

# -----------------------------------------------------------------------------
def test_clearVSCPFilter():
    f = vscp.vscpEventFilter()
    f.filter_class = 10
    f.mask_class = 0xffff
    vhlp.clearVSCPFilter(f)
    assert 0 == f.filter_class
    assert 0 == f.mask_class

# -----------------------------------------------------------------------------
def test_doLevel2Filter():
    e = vscp.vscpEvent()
    e.vscpclass = 10
    e.vscptype = 6
    f = vscp.vscpEventFilter()
    vhlp.clearVSCPFilter(f)
    # All zero filter/mask lets everything through
    assert vscp.VSCP_ERROR_SUCCESS == vhlp.doLevel2Filter(e, f)


# -----------------------------------------------------------------------------
#                              CANAL helpers
# -----------------------------------------------------------------------------

def test_convertEventToCanal_and_back():
    e = vscp.vscpEvent()
    e.vscpclass = 10
    e.vscptype = 6
    e.sizedata = 3
    p = (c_ubyte * 3)()
    p[0] = 1
    p[1] = 2
    p[2] = 3
    e.pdata = cast(p, POINTER(c_ubyte))

    msg = canalMsg()
    rv = vhlp.convertEventToCanal(msg, e)
    e.pdata = None
    assert rv == vscp.VSCP_ERROR_SUCCESS
    assert 3 == msg.sizeData
    assert 1 == msg.data[0]

    guid = (c_ubyte * 16)()
    e2 = vscp.vscpEvent()
    rv = vhlp.convertCanalToEvent(e2, msg, guid)
    assert rv == vscp.VSCP_ERROR_SUCCESS
    assert 10 == e2.vscpclass
    assert 6 == e2.vscptype
    assert 3 == e2.sizedata

# -----------------------------------------------------------------------------
def test_convertEventExToCanal_and_back():
    ex = vscp.vscpEventEx()
    ex.vscpclass = 10
    ex.vscptype = 6
    ex.sizedata = 3
    ex.data[0] = 1
    ex.data[1] = 2
    ex.data[2] = 3

    msg = canalMsg()
    rv = vhlp.convertEventExToCanal(msg, ex)
    assert rv == vscp.VSCP_ERROR_SUCCESS
    assert 3 == msg.sizeData
    assert 1 == msg.data[0]

    guid = (c_ubyte * 16)()
    ex2 = vscp.vscpEventEx()
    rv = vhlp.convertCanalToEventEx(ex2, msg, guid)
    assert rv == vscp.VSCP_ERROR_SUCCESS
    assert 10 == ex2.vscpclass
    assert 6 == ex2.vscptype
    assert 3 == ex2.sizedata


# -----------------------------------------------------------------------------
#                              Measurement helpers
# -----------------------------------------------------------------------------

def test_convertFloatToFloatEventData():
    rv, data = vhlp.convertFloatToFloatEventData(3.14, 2, 1)
    print(rv, ["0x%02x" % b for b in data])
    assert rv == vscp.VSCP_ERROR_SUCCESS
    assert 5 == len(data)
    # Float coding | unit 2 | sensorindex 1
    assert 0xB1 == data[0]

# -----------------------------------------------------------------------------
def test_convertFloatToNormalizedEventData():
    rv, data = vhlp.convertFloatToNormalizedEventData(3.14, 2, 1)
    print(rv, ["0x%02x" % b for b in data])
    assert rv == vscp.VSCP_ERROR_SUCCESS
    assert len(data) > 1

# -----------------------------------------------------------------------------
def test_convertIntegerToNormalizedEventData():
    if not has_symbol('vscphlp_convertIntegerToNormalizedEventData'):
        print("symbol not exported by this libvscphelper - skipped")
        return
    rv, data = vhlp.convertIntegerToNormalizedEventData(1234, 2, 1)
    print(rv, ["0x%02x" % b for b in data])
    assert rv == vscp.VSCP_ERROR_SUCCESS
    assert len(data) > 1

# -----------------------------------------------------------------------------
def test_getMeasurementAsFloat():
    rv, data = vhlp.convertFloatToFloatEventData(3.14, 2, 1)
    assert rv == vscp.VSCP_ERROR_SUCCESS
    rv, value = vhlp.getMeasurementAsFloat(data)
    print(rv, value)
    assert rv == vscp.VSCP_ERROR_SUCCESS
    assert abs(value - 3.14) < 0.001

# -----------------------------------------------------------------------------
def test_measurement_info():
    e = vscp.vscpEvent()
    e.sizedata = 0
    e.vscpclass = vc.VSCP_CLASS1_MEASUREMENT
    e.vscptype = vt.VSCP_TYPE_MEASUREMENT_TEMPERATURE
    rv = vhlp.makeFloatMeasurementEvent(e, 3.14, 2, 1)
    assert rv == vscp.VSCP_ERROR_SUCCESS

    assert vscp.VSCP_ERROR_SUCCESS == vhlp.isMeasurement(e)
    assert 2 == vhlp.getMeasurementUnit(e)
    assert 1 == vhlp.getMeasurementSensorIndex(e)
    assert 0 == vhlp.getMeasurementZone(e)
    assert 0 == vhlp.getMeasurementSubZone(e)
    assert 0xB1 == vhlp.getMeasurementDataCoding(e)

    rv, value = vhlp.getVSCPMeasurementAsDouble(e)
    print(rv, value)
    assert rv == vscp.VSCP_ERROR_SUCCESS
    assert abs(value - 3.14) < 0.001

    rv, s = vhlp.getVSCPMeasurementAsString(e)
    print(rv, s)
    assert rv == vscp.VSCP_ERROR_SUCCESS
    assert -1 != s.find('3.14')

# -----------------------------------------------------------------------------
def test_getVSCPMeasurementFloat64AsString():
    e = vscp.vscpEvent()
    e.vscpclass = vc.VSCP_CLASS1_MEASUREMENT64
    e.vscptype = vt.VSCP_TYPE_MEASUREMENT_TEMPERATURE
    ba = vhlp.double2ByteArray(3.14)
    e.sizedata = 8
    p = (c_ubyte * 8)(*ba)
    e.pdata = cast(p, POINTER(c_ubyte))
    rv, s = vhlp.getVSCPMeasurementFloat64AsString(e)
    e.pdata = None
    print(rv, s)
    assert rv == vscp.VSCP_ERROR_SUCCESS
    assert -1 != s.find('3.14')

# -----------------------------------------------------------------------------
def test_getDataCodingBitArray():
    data = bytearray([0x00, 0x55])
    assert 0x55 == vhlp.getDataCodingBitArray(data)

# -----------------------------------------------------------------------------
def test_getDataCodingInteger():
    data = bytearray([0x60, 0x01, 0x02])
    assert 258 == vhlp.getDataCodingInteger(data)

# -----------------------------------------------------------------------------
def test_getDataCodingNormalizedInteger():
    # Same coding as used in the level1 to level2 tests
    data = bytearray([0x80, 0x02, 0x1B, 0x22])
    value = vhlp.getDataCodingNormalizedInteger(data)
    print(value)
    assert abs(value - 694600.0) < 0.1

# -----------------------------------------------------------------------------
def test_getDataCodingString():
    data = bytearray([0x40, ord('3'), ord('.'), ord('1')])
    rv, s = vhlp.getDataCodingString(data)
    print(rv, s)
    assert rv == vscp.VSCP_ERROR_SUCCESS
    assert -1 != s.find('3.1')


# -----------------------------------------------------------------------------
#                              GUID helpers
# -----------------------------------------------------------------------------

def test_parseGuid():
    rv, guid = vhlp.parseGuid(GUID_STR)
    assert rv == vscp.VSCP_ERROR_SUCCESS
    assert 0xFF == guid[0]
    assert 0xF5 == guid[7]
    assert 0x01 == guid[15]

# -----------------------------------------------------------------------------
def test_getGuidFromStringToArray():
    rv, guid = vhlp.getGuidFromStringToArray(GUID_STR)
    assert rv == vscp.VSCP_ERROR_SUCCESS
    assert 0xFF == guid[0]
    assert 0xF5 == guid[7]
    assert 0x01 == guid[15]

# -----------------------------------------------------------------------------
def test_getGuidFromString_writeGuidToString():
    e = vscp.vscpEvent()
    rv = vhlp.getGuidFromString(e, GUID_STR)
    assert rv == vscp.VSCP_ERROR_SUCCESS
    assert 0xFF == e.guid[0]
    assert 0x01 == e.guid[15]
    rv, s = vhlp.writeGuidToString(e)
    print(rv, s)
    assert rv == vscp.VSCP_ERROR_SUCCESS
    assert GUID_STR.lower() == s.lower()

# -----------------------------------------------------------------------------
def test_getGuidFromStringEx_writeGuidToStringEx():
    ex = vscp.vscpEventEx()
    rv = vhlp.getGuidFromStringEx(ex, GUID_STR)
    assert rv == vscp.VSCP_ERROR_SUCCESS
    assert 0xFF == ex.guid[0]
    assert 0x01 == ex.guid[15]
    rv, s = vhlp.writeGuidToStringEx(ex)
    print(rv, s)
    assert rv == vscp.VSCP_ERROR_SUCCESS
    assert GUID_STR.lower() == s.lower()

# -----------------------------------------------------------------------------
def test_writeGuidToString4Rows():
    e = vscp.vscpEvent()
    rv = vhlp.getGuidFromString(e, GUID_STR)
    assert rv == vscp.VSCP_ERROR_SUCCESS
    rv, s = vhlp.writeGuidToString4Rows(e)
    print(rv, s)
    assert rv == vscp.VSCP_ERROR_SUCCESS
    assert len(s) > 0

# -----------------------------------------------------------------------------
def test_writeGuidToString4RowsEx():
    ex = vscp.vscpEventEx()
    rv = vhlp.getGuidFromStringEx(ex, GUID_STR)
    assert rv == vscp.VSCP_ERROR_SUCCESS
    rv, s = vhlp.writeGuidToString4RowsEx(ex)
    print(rv, s)
    assert rv == vscp.VSCP_ERROR_SUCCESS
    assert len(s) > 0

# -----------------------------------------------------------------------------
def test_writeGuidArrayToString():
    rv, guid = vhlp.getGuidFromStringToArray(GUID_STR)
    assert rv == vscp.VSCP_ERROR_SUCCESS
    rv, s = vhlp.writeGuidArrayToString(guid)
    print(rv, s)
    assert rv == vscp.VSCP_ERROR_SUCCESS
    assert GUID_STR.lower() == s.lower()

# -----------------------------------------------------------------------------
def test_reverseGUID():
    guid = (c_ubyte * 16)(*range(16))
    rv = vhlp.reverseGUID(guid)
    assert rv == vscp.VSCP_ERROR_SUCCESS
    assert 15 == guid[0]
    assert 0 == guid[15]

# -----------------------------------------------------------------------------
def test_isGuidEmpty():
    empty = (c_ubyte * 16)()
    assert vhlp.isGuidEmpty(empty)
    rv, guid = vhlp.getGuidFromStringToArray(GUID_STR)
    assert rv == vscp.VSCP_ERROR_SUCCESS
    assert not vhlp.isGuidEmpty(guid)

# -----------------------------------------------------------------------------
def test_isSameGuid():
    rv, guid1 = vhlp.getGuidFromStringToArray(GUID_STR)
    assert rv == vscp.VSCP_ERROR_SUCCESS
    rv, guid2 = vhlp.getGuidFromStringToArray(GUID_STR)
    assert rv == vscp.VSCP_ERROR_SUCCESS
    assert vhlp.isSameGuid(guid1, guid2)
    guid2[15] = 0x55
    assert not vhlp.isSameGuid(guid1, guid2)

# -----------------------------------------------------------------------------
# The following GUID helpers are not exported by all versions of
# libvscphelper so their tests are skipped when the symbol is missing

def test_convertGuidToString():
    if not has_symbol('vscphlp_convertGuidToString'):
        print("symbol not exported by this libvscphelper - skipped")
        return
    rv, guid = vhlp.getGuidFromStringToArray(GUID_STR)
    assert rv == vscp.VSCP_ERROR_SUCCESS
    rv, s = vhlp.convertGuidToString(guid)
    assert rv == vscp.VSCP_ERROR_SUCCESS
    assert GUID_STR.lower() == s.lower()

# -----------------------------------------------------------------------------
def test_convertStringToGuid():
    if not has_symbol('vscphlp_convertStringToGuid'):
        print("symbol not exported by this libvscphelper - skipped")
        return
    rv, guid = vhlp.convertStringToGuid(GUID_STR)
    assert rv == vscp.VSCP_ERROR_SUCCESS
    assert 0xFF == guid[0]
    assert 0x01 == guid[15]

# -----------------------------------------------------------------------------
def test_clearGuid():
    if not has_symbol('vscphlp_clearGuid'):
        print("symbol not exported by this libvscphelper - skipped")
        return
    rv, guid = vhlp.getGuidFromStringToArray(GUID_STR)
    assert rv == vscp.VSCP_ERROR_SUCCESS
    vhlp.clearGuid(guid)
    assert vhlp.isGuidEmpty(guid)

# -----------------------------------------------------------------------------
def test_compareGuids():
    if not has_symbol('vscphlp_compareGuids'):
        print("symbol not exported by this libvscphelper - skipped")
        return
    rv, guid1 = vhlp.getGuidFromStringToArray(GUID_STR)
    assert rv == vscp.VSCP_ERROR_SUCCESS
    rv, guid2 = vhlp.getGuidFromStringToArray(GUID_STR)
    assert rv == vscp.VSCP_ERROR_SUCCESS
    assert 0 == vhlp.compareGuids(guid1, guid2)

# -----------------------------------------------------------------------------
def test_copyGuid():
    if not has_symbol('vscphlp_copyGuid'):
        print("symbol not exported by this libvscphelper - skipped")
        return
    rv, src = vhlp.getGuidFromStringToArray(GUID_STR)
    assert rv == vscp.VSCP_ERROR_SUCCESS
    dest = (c_ubyte * 16)()
    vhlp.copyGuid(dest, src)
    assert vhlp.isSameGuid(dest, src)

# -----------------------------------------------------------------------------
def test_isValidGuid():
    if not has_symbol('vscphlp_isValidGuid'):
        print("symbol not exported by this libvscphelper - skipped")
        return
    rv, guid = vhlp.getGuidFromStringToArray(GUID_STR)
    assert rv == vscp.VSCP_ERROR_SUCCESS
    assert vhlp.isValidGuid(guid)

# -----------------------------------------------------------------------------
def test_generateNewGuid():
    if not has_symbol('vscphlp_generateNewGuid'):
        print("symbol not exported by this libvscphelper - skipped")
        return
    guid = (c_ubyte * 16)()
    vhlp.generateNewGuid(guid)
    assert not vhlp.isGuidEmpty(guid)


# -----------------------------------------------------------------------------
#                        UDP / Multicast / Encryption
# -----------------------------------------------------------------------------

def test_encryptionTokenCode():
    if not has_symbol('vscphlp_getEncryptionTokenFromCode'):
        print("symbol not exported by this libvscphelper - skipped")
        return
    rv, token = vhlp.getEncryptionTokenFromCode(vscp.VSCP_ENCRYPTION_AES128)
    print(rv, token)
    assert rv == vscp.VSCP_ERROR_SUCCESS
    assert "aes128" == token.lower()
    rv, code = vhlp.getEncryptionCodeFromToken(token)
    assert rv == vscp.VSCP_ERROR_SUCCESS
    assert vscp.VSCP_ENCRYPTION_AES128 == code

# -----------------------------------------------------------------------------
def test_getUdpFrameSizeFromEvent():
    if not has_symbol('vscphlp_getUDpFrameSizeFromEvent'):
        print("symbol not exported by this libvscphelper - skipped")
        return
    e = vscp.vscpEvent()
    e.vscpclass = 10
    e.vscptype = 6
    e.sizedata = 0
    size = vhlp.getUdpFrameSizeFromEvent(e)
    print("frame size =", size)
    assert size > 0

# -----------------------------------------------------------------------------
def test_getUdpFrameSizeFromEventEx():
    if not has_symbol('vscphlp_getUDpFrameSizeFromEventEx'):
        print("symbol not exported by this libvscphelper - skipped")
        return
    ex = vscp.vscpEventEx()
    ex.vscpclass = 10
    ex.vscptype = 6
    ex.sizedata = 0
    size = vhlp.getUdpFrameSizeFromEventEx(ex)
    print("frame size =", size)
    assert size > 0

# -----------------------------------------------------------------------------
def test_writeEventToUdpFrame():
    if not has_symbol('vscphlp_writeEventToUdpFrame'):
        print("symbol not exported by this libvscphelper - skipped")
        return
    e = vscp.vscpEvent()
    e.vscpclass = 10
    e.vscptype = 6
    e.sizedata = 0
    rv, frame = vhlp.writeEventToUdpFrame(e, 0)
    print(rv, len(frame))
    assert rv == vscp.VSCP_ERROR_SUCCESS
    assert len(frame) > 0

# -----------------------------------------------------------------------------
def test_writeEventExToUdpFrame():
    if not has_symbol('vscphlp_writeEventExToUdpFrame'):
        print("symbol not exported by this libvscphelper - skipped")
        return
    ex = vscp.vscpEventEx()
    ex.vscpclass = 10
    ex.vscptype = 6
    ex.sizedata = 0
    rv, frame = vhlp.writeEventExToUdpFrame(ex, 0)
    print(rv, len(frame))
    assert rv == vscp.VSCP_ERROR_SUCCESS
    assert len(frame) > 0

# -----------------------------------------------------------------------------
def test_encrypt_decrypt_frame():
    if not has_symbol('vscphlp_encryptVscpUdpFrame'):
        print("symbol not exported by this libvscphelper - skipped")
        return
    ex = vscp.vscpEventEx()
    ex.vscpclass = 10
    ex.vscptype = 6
    ex.sizedata = 0
    rv, frame = vhlp.writeEventExToUdpFrame(ex, 0)
    assert rv == vscp.VSCP_ERROR_SUCCESS

    key = bytearray(range(16))
    iv = bytearray(range(16))
    rv, encrypted = vhlp.encryptVscpUdpFrame(frame, key, iv,
                                             vscp.VSCP_ENCRYPTION_AES128)
    print("encrypt rv =", rv)
    assert isinstance(rv, int)

    rv, decrypted = vhlp.decryptVscpUdpFrame(encrypted, key, iv,
                                             vscp.VSCP_ENCRYPTION_AES128)
    print("decrypt rv =", rv)
    assert isinstance(rv, int)
    assert isinstance(decrypted, bytearray)


# -----------------------------------------------------------------------------
#                       Remote server (tcp/ip) functions
# -----------------------------------------------------------------------------
#
# These tests need a live VSCP daemon. They are skipped if no connection
# can be established.

def test_session():
    host = os.environ.get("VSCP_HOST", "192.168.1.7:9598")
    user = os.environ.get("VSCP_USER", "admin")
    password = os.environ.get("VSCP_PASSWORD", "secret")

    h1 = vhlp.newSession()
    assert h1 != 0

    assert vscp.VSCP_ERROR_SUCCESS == vhlp.setResponseTimeout(h1, 2000)
    assert vscp.VSCP_ERROR_SUCCESS == vhlp.setAfterCommandSleep(h1, 100)

    rv = vhlp.open(h1, host, user, password)
    if vscp.VSCP_ERROR_SUCCESS != rv:
        print("No VSCP server available (rv=%d) - remote tests skipped" % rv)
        vhlp.closeSession(h1)
        return

    assert vscp.VSCP_ERROR_SUCCESS == vhlp.isConnected(h1)
    assert vscp.VSCP_ERROR_SUCCESS == vhlp.noop(h1)
    assert vscp.VSCP_ERROR_SUCCESS == vhlp.doCommand(h1, "NOOP\r\n")
    assert vscp.VSCP_ERROR_SUCCESS == vhlp.checkReply(h1, 1)
    assert vscp.VSCP_ERROR_SUCCESS == vhlp.clearLocalInputQueue(h1)
    assert vscp.VSCP_ERROR_SUCCESS == vhlp.clearDaemonEventQueue(h1)

    (rv, v1, v2, v3) = vhlp.getVersion(h1)
    assert vscp.VSCP_ERROR_SUCCESS == rv
    print("Server version = %d.%d.%d" % (v1.value, v2.value, v3.value))

    (rv, dllversion) = vhlp.getDLLVersion(h1)
    assert vscp.VSCP_ERROR_SUCCESS == rv
    print("DLL version =", dllversion)

    (rv, vendor) = vhlp.getVendorString(h1)
    assert vscp.VSCP_ERROR_SUCCESS == rv
    print("Vendor =", vendor)

    (rv, drvinfo) = vhlp.getDriverInfo(h1)
    assert vscp.VSCP_ERROR_SUCCESS == rv
    print("Driver info =", drvinfo)

    status = vscp.VSCPStatus()
    assert vscp.VSCP_ERROR_SUCCESS == vhlp.getStatus(h1, status)

    statistics = vscp.VSCPStatistics()
    assert vscp.VSCP_ERROR_SUCCESS == vhlp.getStatistics(h1, statistics)

    f = vscp.vscpEventFilter()
    vhlp.clearVSCPFilter(f)
    assert vscp.VSCP_ERROR_SUCCESS == vhlp.setFilter(h1, f)

    (rv, guid) = vhlp.getGUID(h1)
    assert vscp.VSCP_ERROR_SUCCESS == rv
    assert vscp.VSCP_ERROR_SUCCESS == vhlp.setGUID(h1, guid)

    # Send an event and check the queue
    ex = vscp.vscpEventEx()
    ex.vscpclass = 10
    ex.vscptype = 99
    ex.sizedata = 3
    ex.data[0] = 1
    ex.data[1] = 2
    ex.data[2] = 3
    assert vscp.VSCP_ERROR_SUCCESS == vhlp.sendEventEx(h1, ex)

    e = vscp.vscpEvent()
    e.vscpclass = 20
    e.vscptype = 9
    e.sizedata = 3
    p = (c_ubyte * 3)()
    p[0] = 11
    p[1] = 22
    p[2] = 33
    e.pdata = cast(p, POINTER(c_ubyte))
    assert vscp.VSCP_ERROR_SUCCESS == vhlp.sendEvent(h1, e)
    e.pdata = None

    cnt = c_uint(0)
    assert vscp.VSCP_ERROR_SUCCESS == vhlp.isDataAvailable(h1, cnt)
    print("count =", cnt.value)

    if cnt.value >= 1:
        exr = vscp.vscpEventEx()
        assert vscp.VSCP_ERROR_SUCCESS == vhlp.receiveEventEx(h1, exr)
    if cnt.value >= 2:
        er = vscp.vscpEvent()
        assert vscp.VSCP_ERROR_SUCCESS == vhlp.receiveEvent(h1, er)

    # Blocking receive in receive loop
    assert vscp.VSCP_ERROR_SUCCESS == vhlp.enterReceiveLoop(h1)
    er = vscp.vscpEvent()
    rv = vhlp.blockingReceiveEvent(h1, er, 1000)
    assert rv in (vscp.VSCP_ERROR_SUCCESS, vscp.VSCP_ERROR_TIMEOUT)
    exr = vscp.vscpEventEx()
    rv = vhlp.blockingReceiveEventEx(h1, exr, 1000)
    assert rv in (vscp.VSCP_ERROR_SUCCESS, vscp.VSCP_ERROR_TIMEOUT)
    assert vscp.VSCP_ERROR_SUCCESS == vhlp.quitReceiveLoop(h1)

    assert vscp.VSCP_ERROR_SUCCESS == vhlp.close(h1)

    # openInterface variant
    h2 = vhlp.newSession()
    assert h2 != 0
    interface = "tcp://%s;%s;%s" % (host, user, password)
    rv = vhlp.openInterface(h2, interface, 0)
    print("openInterface rv =", rv)
    if vscp.VSCP_ERROR_SUCCESS == rv:
        vhlp.close(h2)

    # serverShutDown is not tested as it would take down the test server

    vhlp.closeSession(h1)


# -----------------------------------------------------------------------------
if __name__ == "__main__":
    test_readStringValue()
    test_replaceBackslash()
    test_vscpPriority()
    test_vscpPriorityEx()
    test_CANALid()
    test_getCANALidFromEvent()
    test_getCANALidFromEventEx()
    test_calc_crc_Event()
    test_calc_crc_EventEx()
    test_calcCRC4GUID()
    test_convertVSCPtoEx()
    test_convertVSCPfromEx()
    test_newVSCPevent_delete_v2()
    test_newVSCPevent_delete()
    test_deleteVSCPeventEx_available()
    test_copyVSCPEvent()
    test_makeTimeStamp()
    test_setEventDateTimeBlockToNow()
    test_setEventExDateTimeBlockToNow()
    test_setEventToNow()
    test_setEventExToNow()
    test_getTimeString()
    test_getISOTimeString()
    test_setVscpEventFromString()
    test_setVscpEventExFromString()
    test_setVscpDataFromString()
    test_getVscpDataFromString()
    test_getVscpDataArrayFromString()
    test_setVscpDataArrayFromString()
    test_writeVscpDataToString()
    test_writeVscpDataWithSizeToString()
    test_readFilterFromString()
    test_readMaskFromString()
    test_writeFilterToString()
    test_writeMaskToString()
    test_copyVSCPFilter()
    test_clearVSCPFilter()
    test_doLevel2Filter()
    test_convertEventToCanal_and_back()
    test_convertEventExToCanal_and_back()
    test_convertFloatToFloatEventData()
    test_convertFloatToNormalizedEventData()
    test_convertIntegerToNormalizedEventData()
    test_getMeasurementAsFloat()
    test_measurement_info()
    test_getVSCPMeasurementFloat64AsString()
    test_getDataCodingBitArray()
    test_getDataCodingInteger()
    test_getDataCodingNormalizedInteger()
    test_getDataCodingString()
    test_parseGuid()
    test_getGuidFromStringToArray()
    test_getGuidFromString_writeGuidToString()
    test_getGuidFromStringEx_writeGuidToStringEx()
    test_writeGuidToString4Rows()
    test_writeGuidToString4RowsEx()
    test_writeGuidArrayToString()
    test_reverseGUID()
    test_isGuidEmpty()
    test_isSameGuid()
    test_convertGuidToString()
    test_convertStringToGuid()
    test_clearGuid()
    test_compareGuids()
    test_copyGuid()
    test_isValidGuid()
    test_generateNewGuid()
    test_encryptionTokenCode()
    test_getUdpFrameSizeFromEvent()
    test_getUdpFrameSizeFromEventEx()
    test_writeEventToUdpFrame()
    test_writeEventExToUdpFrame()
    test_encrypt_decrypt_frame()

    # Needs a live server - run last as closeSession unloads the library
    test_session()

    print("Everything passed")
