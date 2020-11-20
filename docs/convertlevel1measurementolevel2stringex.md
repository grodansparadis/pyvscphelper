

```clike
int convertLevel1MeasuremenToLevel2String( ex )
```

### Parameters

#### ex
VSCP event ex.

### Return Value
VSCP_ERROR_SUCCESS is returned if the measurement event is converted correctly, VSCP_ERROR_ERROR is returned if not. 

### Description
Convert Level I measurement to a Level II string measurement event [CLASS2.MEASUREMENT_STRING). 

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
rv = vhlp.convertLevel1MeasuremenToLevel2StringEx( e )
print("Return value = ",rv)
```

### See Also
(convertlevel1measurementolevel2doubleex.md)
[convertLevel1MeasuremenToLevel2String]
[convertLevel1MeasuremenToLevel2Double](convertlevel1measurementolevel2double.md)
[convertLevel1MeasuremenToLevel2DoubleEx](convertlevel1measurementolevel2string.md)


[filename](./bottom_copyright.md ':include')

