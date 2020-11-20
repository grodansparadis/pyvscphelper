

```clike
int makeFloatMeasurementEvent( e, value, unit, sensoridx )
```

### Parameters

#### e
VSCP event that will get the result as it's data.

#### value
Floating point value to write as a 32-bit float.

#### unit
A unit value 0-3

#### sensorid
A sensor index value 0-7

### Return Value
VSCP_ERROR_SUCCESS is returned on success.

### Description
Make a floating point ()32-bit) coded event from floating point data.

#### C example

```python
e = vscp.vscpEvent()
e.sizedata = 0
e.vscpclass = vc.VSCP_CLASS1_MEASUREMENT
e.vscptype = vt.VSCP_TYPE_MEASUREMENT_TEMPERATURE
value = 3.14
unit = 2
sensorindex = 1
rv = vhlp.makeFloatMeasurementEvent( e, value, unit, sensorindex )
print("Return value = ",rv)
```



[filename](./bottom_copyright.md ':include')