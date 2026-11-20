# Measurement unit conversion

Convert measurement values between units. All measurement classes (CLASS1.MEASUREMENT and its X1-X4 classes, MEASUREMENT32/64, MEASUREZONE, SETVALUEZONE, their Level II variants, MEASUREMENT_STR and MEASUREMENT_FLOAT) use the types and units of CLASS1.MEASUREMENT. Needs libvscphelper 16.0.0.292 or later.

Two ways are available:

* **Unit table** compiled into the helper library: exact and needs no files.
* **Expressions** loaded at runtime from `vscp-units.json` (published with the [VSCP class definitions](https://github.com/grodansparadis/vscp-classes)) or `vscp-hashtypeevents.json`: new or changed units work without a new library.

Both give the same results for the published units. Units that can not be converted (latitude/longitude, ppm/percent of a molar concentration, date/time formats, ...) give `VSCP_ERROR_NOT_SUPPORTED`.

| Function | Returns |
| --- | --- |
| `convertMeasurementUnit(vscp_type, from_unit, to_unit, value)` | `(rv, result)` |
| `getMeasurementUnitInfo(vscp_type, unit)` | `(rv, name, symbol_ascii, symbol_utf8, convertible)` |
| `convertMeasurement(event, to_unit)` | `(rv, result)`; value and unit are read from the event |
| `convertMeasurementEx(eventex, to_unit)` | `(rv, result)` |
| `loadUnitExpressions(path)` | `rv` |
| `loadUnitExpressionsFromString(text)` | `rv`; `text` is JSON text or a `dict` |
| `convertMeasurementUnitExpr(vscp_type, from_unit, to_unit, value)` | `(rv, result)`; needs loaded expressions |
| `evalUnitExpression(expr, value)` | `(rv, result)`; for example `"({{{val}}} + 459.67) * 5/9"` |

See the [C functions](https://github.com/grodansparadis/vscp-helper-lib/blob/master/docs/vscphlp_convertmeasurementunit.md) for the error codes.

```python
import vscp
import vscphelper as vhlp

# 25 degrees Celsius (unit 1) to Fahrenheit (unit 2) for temperature (type 6)
rv, f = vhlp.convertMeasurementUnit(6, 1, 2, 25.0)
if rv == vscp.VSCP_ERROR_SUCCESS:
    print(f)                                   # 77.0

rv, name, ascii_symbol, utf8_symbol, convertible = vhlp.getMeasurementUnitInfo(6, 1)
print(name, utf8_symbol)                       # Celsius °C

# The same with the expressions of vscp-units.json
if vhlp.loadUnitExpressions('vscp-units.json') == vscp.VSCP_ERROR_SUCCESS:
    rv, f = vhlp.convertMeasurementUnitExpr(6, 1, 2, 25.0)
```

[filename](./bottom_copyright.md ':include')
