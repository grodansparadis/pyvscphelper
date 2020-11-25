


```clike
(rv,str) convertEventToString( e )
```

### Parameters

#### pEvent
The VSCP event which will be written to the string buffer.

### Return Value
VReturn a tuple consisting of a return value and the string. SCP_ERROR_SUCCESS is returned on success. 

### Description
Write VSCP event content to a string. 

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

    rv,s = vhlp.convertEventToString( e )
    print(rv)
    print(s)
    assert rv == vscp.VSCP_ERROR_SUCCESS
    assert -1 != s.find('0,10,6,0,')
    assert -1 != s.find(',00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00,0x80,0x02,0x1B,0x22')
```

### See Also

[writeVscpEventExToString](writevscpeventextostring.md)



[filename](./bottom_copyright.md ':include')
