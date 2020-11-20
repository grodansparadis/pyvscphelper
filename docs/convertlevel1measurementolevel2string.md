

```clike
int convertLevel1MeasuremenToLevel2String( e )
```

### Parameters

#### e
VSCP event.

### Return Value
VSCP_ERROR_SUCCESS is returned if the measurement event is converted correctly, VSCP_ERROR_ERROR is returned if not. 

### Description
Convert Level I measurement to a Level II string measurement event [CLASS2.MEASUREMENT_STRING). 

### Example

```python
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
```

### See Also
(convertlevel1measurementolevel2doubleex.md)
[convertLevel1MeasuremenToLevel2String]
[convertLevel1MeasuremenToLevel2Double](convertlevel1measurementolevel2double.md)
[convertLevel1MeasuremenToLevel2DoubleEx](convertlevel1measurementolevel2string.md)


[filename](./bottom_copyright.md ':include')

