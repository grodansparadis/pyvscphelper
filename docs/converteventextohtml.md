

```clike
(rv,str) convertEventExToHTML( ex )
```

### Parameters

#### ex
VSCP event ex


### Return Value
Return a tuple consisting of a return value and the HTML string. VSCP_ERROR_SUCCESS is returned on success, VSCP_ERROR_BUFFER_TO_SMALL is returned if the size of the supplied buffer is to small. 

### Description
Write VSCP event-ex on HTML format to string. Format is specified in [vscp.h](https://github.com/grodansparadis/vscp/blob/master/src/vscp/common/vscp.h). 


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
    rv,s = vhlp.convertEventExToHTML( ex )
    print(rv)
    print(s)
    assert rv == vscp.VSCP_ERROR_SUCCESS
    assert -1 != s.find('Class: 10 ')
    assert -1 != s.find('Type: 6 ')
    assert -1 != s.find('<p>Data count: 4<br>Data: 0x0B,0x16,0x21,0x2C<br></p>')
```

### See Also
[convertEventToHTML](converteventtohtml.md)



[filename](./bottom_copyright.md ':include')