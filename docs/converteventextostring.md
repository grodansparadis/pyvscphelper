


```clike
(rv,str) convertEventExToString( ex )
```

### Parameters

#### e
The VSCP event ex which will be written to the string buffer.

### Return Value
Return a tuple consisting of a return value and the string. VSCP_ERROR_SUCCESS is returned on success.

### Description
Write VSCP event ex content to a string. 

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
    rv,s = vhlp.convertEventExToString( ex )
    print(rv)
    print(s)
    assert rv == vscp.VSCP_ERROR_SUCCESS
    assert -1 != s.find('0,10,6,0,')
    assert -1 != s.find(',00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00,0x0B,0x16,0x21,0x2C')
```

### See Also
[convertEventToString](converteventtostring.md)



[filename](./bottom_copyright.md ':include')
