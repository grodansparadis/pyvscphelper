

```clike
int makeLevel2StringMeasurementEvent( e, 
                                        type,
                                        value,
                                        unit,
                                        sensoridx,
                                        zone,
                                        subzone )
```

### Parameters

#### e
VSCP event that data should be written to.

#### type
The VSCP type for the event. Must be one of the types in [CLASS1.MEASUREMENT](https://grodansparadis.gitbooks.io/the-vscp-specification/class1.measurement.html)

#### value
Floating point measurement value.

#### unit
Unit (0-255) for the measurement.

#### sensoridx
Sensor index (0-255) for the measurement.

#### zone
Zone (0-255) for the measurement.

#### subzone
Sub zone (0-255) for the measurement. 

### Return Value
VSCP_ERROR_SUCCESS is returned if the measurement event is constructed correctly, VSCP_ERROR_ERROR is returned if not. 

### Description
Construct a Level II string measurement event from supplied data. **Note** that the GUID must be set externally. 

### Example

```python
e = vscp.vscpEvent()
e.sizedata = 0
e.vscpclass = vc.VSCP_CLASS1_MEASUREMENT
e.vscptype = vt.VSCP_TYPE_MEASUREMENT_TEMPERATURE
value = 3.14
unit = 2
sensorindex = 1
rv = vhlp.makeStringMeasurementEvent( e, value, unit, sensorindex )
print("Return value = ",rv)
```

### See Also
[makeLevel2FloatMeasurementEvent](makelevel2floatmeasurementevent.md)



[filename](./bottom_copyright.md ':include')