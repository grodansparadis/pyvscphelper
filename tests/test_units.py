# FILE: test_units.py
#
# Tests for the measurement unit conversion bindings in vscphelper.py
# (needs libvscphelper 16.0.0.292 or later).
#
# Run with pytest from the tests folder, or directly with
# python test_units.py
#
# VSCPHELPER_LIB can point to the helper library and VSCP_UNITS_JSON to
# vscp-units.json (default: the copy in a vscp checkout next to this one).

import os
import struct
import sys
from ctypes import POINTER, c_ubyte, cast

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(HERE, '..', '..', 'pyvscp'))
import vscp

sys.path.append(os.path.join(HERE, '..'))
import vscphelper as vhlp

import pytest

TEMPERATURE = 6
INVALID_SYNTAX = getattr(vscp, 'VSCP_ERROR_INVALID_SYNTAX', 58)
PRESSURE = 12
POSITION = 31

UNITS_JSON = os.environ.get(
    'VSCP_UNITS_JSON',
    os.path.join(HERE, '..', '..', 'vscp', 'src', 'vscp', 'common', 'vscp-units.json'))

if not hasattr(vhlp.lib, 'vscphlp_convertMeasurementUnit'):
    pytest.skip('The loaded helper library has no unit conversion (needs 16.0.0.292 or later)',
                allow_module_level=True)


def near(a, b, rel=1e-12):
    return abs(a - b) <= rel * max(1.0, abs(a), abs(b))


def test_convert_unit():
    rv, r = vhlp.convertMeasurementUnit(TEMPERATURE, 2, 1, 212)   # F -> C
    assert rv == vscp.VSCP_ERROR_SUCCESS and near(r, 100)
    rv, r = vhlp.convertMeasurementUnit(PRESSURE, 3, 1, 1)        # atm -> bar
    assert rv == vscp.VSCP_ERROR_SUCCESS and near(r, 1.01325)
    rv, _ = vhlp.convertMeasurementUnit(POSITION, 0, 1, 1)        # longitude -> latitude
    assert rv == vscp.VSCP_ERROR_NOT_SUPPORTED
    rv, _ = vhlp.convertMeasurementUnit(TEMPERATURE, 0, 9, 1)
    assert rv == vscp.VSCP_ERROR_UNKNOWN_ITEM


def test_unit_info():
    rv, name, ascii_symbol, utf8_symbol, convertible = vhlp.getMeasurementUnitInfo(TEMPERATURE, 1)
    assert rv == vscp.VSCP_ERROR_SUCCESS
    assert (name, ascii_symbol, utf8_symbol, convertible) == ('Celsius', 'C', '°C', True)
    rv, name, _, _, convertible = vhlp.getMeasurementUnitInfo(POSITION, 1)
    assert rv == vscp.VSCP_ERROR_SUCCESS and name == 'Latitude' and convertible is False


def test_convert_event():
    # CLASS2.MEASUREMENT_FLOAT: index, zone, subzone, unit, double MSB first
    payload = bytes((0, 0, 0, 1)) + struct.pack('>d', 2.5)   # 2.5 bar
    data = (c_ubyte * len(payload))(*payload)
    e = vscp.vscpEvent()
    e.vscpclass = 1060
    e.vscptype = PRESSURE
    e.sizedata = len(payload)
    e.pdata = cast(data, POINTER(c_ubyte))
    rv, r = vhlp.convertMeasurement(e, 0)
    assert rv == vscp.VSCP_ERROR_SUCCESS and near(r, 250000)

    ex = vscp.vscpEventEx()
    ex.vscpclass = 1060
    ex.vscptype = PRESSURE
    ex.sizedata = len(payload)
    for i, b in enumerate(payload):
        ex.data[i] = b
    rv, r = vhlp.convertMeasurementEx(ex, 3)                      # atm
    assert rv == vscp.VSCP_ERROR_SUCCESS and near(r, 250000 / 101325.0)


def test_expressions():
    rv, r = vhlp.evalUnitExpression('({{{val}}} + 459.67) * 5/9', 32)
    assert rv == vscp.VSCP_ERROR_SUCCESS and near(r, 273.15)
    rv, _ = vhlp.evalUnitExpression('2^3', 0)
    assert rv == INVALID_SYNTAX

    units = {'units': [{'type': 500, 'unit': 0},
                       {'type': 500, 'unit': 1, 'conversion0': '{{{val}}}*2', 'conversion': '{{{val}}}/2'}]}
    assert vhlp.loadUnitExpressionsFromString(units) == vscp.VSCP_ERROR_SUCCESS
    rv, r = vhlp.convertMeasurementUnitExpr(500, 1, 0, 4)
    assert rv == vscp.VSCP_ERROR_SUCCESS and r == 8


@pytest.mark.skipif(not os.path.exists(UNITS_JSON), reason='vscp-units.json not found')
def test_expressions_match_table():
    assert vhlp.loadUnitExpressions(UNITS_JSON) == vscp.VSCP_ERROR_SUCCESS
    for vscp_type in (TEMPERATURE, PRESSURE, 13, 30, 32, POSITION):
        for a in range(8):
            for b in range(8):
                rvt, rt = vhlp.convertMeasurementUnit(vscp_type, a, b, 21.5)
                rve, re = vhlp.convertMeasurementUnitExpr(vscp_type, a, b, 21.5)
                assert rvt == rve, (vscp_type, a, b)
                if rvt == vscp.VSCP_ERROR_SUCCESS:
                    assert near(rt, re), (vscp_type, a, b)
    assert vhlp.loadUnitExpressions('/no/such/vscp-units.json') == vscp.VSCP_ERROR_INVALID_PATH


if __name__ == '__main__':
    sys.exit(pytest.main([__file__, '-v']))
