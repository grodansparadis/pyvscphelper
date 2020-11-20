

```clike
int convertLevel1MeasuremenToLevel2DoubleEx( ex )
```

### Parameters

#### pEvent
VSCP event ex.

### Return Value
VSCP_ERROR_SUCCESS is returned if the event is a measurement, VSCP_ERROR_ERROR is returned if the event is not a measurement. 

### Description
Convert Level I measurement to a Level II float measurement event [CLASS2.MEASUREMENT_FLOAT](https://grodansparadis.gitbooks.io/the-vscp-specification/class2.measurement_float.html). 

### Example

```python
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
```

### See Also
[convertLevel1MeasuremenToLevel2Double](convertlevel1measurementolevel2double.md)
[convertLevel1MeasuremenToLevel2String](convertlevel1measurementolevel2string.md)
[convertLevel1MeasuremenToLevel2StringEx](convertlevel1measurementolevel2stringex.md)



[filename](./bottom_copyright.md ':include')
