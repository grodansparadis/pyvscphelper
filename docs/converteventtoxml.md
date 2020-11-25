

```clike
(rv,str) convertEventToXML( e )
```

### Parameters

#### e
VSCP event

### Return Value
Return a tuple consisting of a return value and the XML string. VSCP_ERROR_SUCCESS is returned on success, VSCP_ERROR_BUFFER_TO_SMALL is returned if the size of the supplied buffer is to small. 

### Description
Write VSCP event on XML format to string. Format is specified in [vscp.h](https://github.com/grodansparadis/vscp/blob/master/src/vscp/common/vscp.h). 

### Example

```python
    from xml.dom.minidom import parse, parseString
    
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

    rv,s = vhlp.convertEventToXML( e )
    print(rv)
    print(s)
    assert rv == vscp.VSCP_ERROR_SUCCESS
    x = parseString(s)
    item = x.getElementsByTagName('event')
    print(len(item))
    print(item[0].attributes['vscpGuid'].value)
    #for s in item:
    #    print(s.attributes['vscpGuid'].value)
    print("class = ", item[0].attributes['vscpClass'].value)
    assert 10 == int(item[0].attributes['vscpClass'].value)
    print("type = ", item[0].attributes['vscpType'].value)
    assert 6 == int(item[0].attributes['vscpType'].value)
    b = item[0].attributes['vscpData'].value.split(',')
    print(b[0],int(b[0],16))
    assert 0x80 == int(b[0],16)
    assert 0x02 == int(b[1],16)
    assert 0x1B == int(b[2],16)
    assert 0x22 == int(b[3],16)
```

### See Also
[convertEventExToXML](converteventextoxml.md)



[filename](./bottom_copyright.md ':include')
