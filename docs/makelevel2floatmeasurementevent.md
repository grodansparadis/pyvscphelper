

```clike
int makeLevel2FloatMeasurementEvent( e, 
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
Construct a Level II floating point measurement event from supplied data. **Note** that the GUID must be set externally. 

### See Also
[makeLevel2StringMeasurementEvent](makelevel2stringmeasurementevent.md)



[filename](./bottom_copyright.md ':include')