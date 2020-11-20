

```clike
int convertLevel1MeasuremenToLevel2Double( e )
```

### Parameters

#### pEvent
VSCP event.

### Return Value
VSCP_ERROR_SUCCESS is returned if the event is a measurement, VSCP_ERROR_ERROR is returned if the event is not a measurement. 

### Description
Convert Level I measurement to a Level II float measurement event [CLASS2.MEASUREMENT_FLOAT](https://grodansparadis.gitbooks.io/the-vscp-specification/class2.measurement_float.html). 

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

    rv = vhlp.convertLevel1MeasuremenToLevel2Double( e )
    print("Return value = ",rv)
    assert rv == vscp.VSCP_ERROR_SUCCESS
```


### See Also
[convertLevel1MeasuremenToLevel2DoubleEx](convertlevel1measurementolevel2doubleex.md)
[convertLevel1MeasuremenToLevel2String](convertlevel1measurementolevel2string.md)
[convertLevel1MeasuremenToLevel2StringEx](convertlevel1measurementolevel2stringex.md)



[filename](./bottom_copyright.md ':include')
