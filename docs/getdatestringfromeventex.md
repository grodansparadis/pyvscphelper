

```clike
(rv,str) getDateStringFromEvent( ex )
```

### Parameters

#### ex
VSCP event ex to get date string from

### Return Value
Tuple with return value and string containing date string. VSCP_ERROR_SUCCESS on success. 

### Description
Extract an ISO date string from the datetime block of an event.

Example result: “2003-11-02T12:23:10Z”

### Example

```python
    ex = vscp.vscpEventEx()

    ex.vscpclass = vc.VSCP_CLASS1_MEASUREMENT
    ex.vscptype = vt.VSCP_TYPE_MEASUREMENT_TEMPERATURE

    # 32-bit float coding = 100
    ex.sizedata = 4
    ex.data[0] = 11
    ex.data[1] = 22
    ex.data[2] = 33
    ex.data[3] = 44
    rv,s = vhlp.getDateStringFromEventEx( ex )
    print(rv)
    print(s)
    assert rv == vscp.VSCP_ERROR_SUCCESS
```

### See Also
[getDateStringFromEventEx](getdatestringfromeventex.md)



[filename](./bottom_copyright.md ':include')