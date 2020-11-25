

```clike
(rv,str) getDateStringFromEvent( e )
```

### Parameters

#### e
VSCP event to get date string from

### Return Value
Tuple with return value and string containing date string. VSCP_ERROR_SUCCESS on success. 

### Description
Extract an ISO date string from the datetime block of an event.

Example result: “2003-11-02T12:23:10Z”

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

    rv,s = vhlp.getDateStringFromEvent( e )
    print(rv)
    print(s)
    assert rv == vscp.VSCP_ERROR_SUCCESS
```

### See Also
[getDateStringFromEventEx](getdatestringfromeventex.md)



[filename](./bottom_copyright.md ':include')