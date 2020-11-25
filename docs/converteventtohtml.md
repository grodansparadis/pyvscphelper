

```clike
(rv,str) convertEventToHTML( e )
```

### Parameters

#### e
VSCP Event

### Return Value
Return a tuple consisting of a return value and the HTML string. VSCP_ERROR_SUCCESS is returned on success, VSCP_ERROR_BUFFER_TO_SMALL is returned if the size of the supplied buffer is to small. 

### Description
Write VSCP event on HTML format to string. Format is specified in [vscp.h](https://github.com/grodansparadis/vscp/blob/master/src/vscp/common/vscp.h). 

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

    rv,s = vhlp.convertEventToHTML( e )
    print(rv)
    print(s)
    assert rv == vscp.VSCP_ERROR_SUCCESS
    assert -1 != s.find('Class: 10 ')
    assert -1 != s.find('Type: 6 ')
    assert -1 != s.find('<p>Data count: 4<br>Data: 0x80,0x02,0x1B,0x22<br></p>')
```

### See Also
[convertEventExToHTML](converteventextohtml.md)



[filename](./bottom_copyright.md ':include')