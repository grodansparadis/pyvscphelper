

```clike
(rv,str) convertEventExToXML( ex )
```

### Parameters

#### ex
VSCP event ex

### Return Value
Return a tuple consisting of a return value and the XML string. VSCP_ERROR_SUCCESS is returned on success, VSCP_ERROR_BUFFER_TO_SMALL is returned if the size of the supplied buffer is to small. 

### Description
Write VSCP event-ex on XML format to string. Format is specified in [vscp.h](https://github.com/grodansparadis/vscp/blob/master/src/vscp/common/vscp.h). 

### Example

```python
    from xml.dom.minidom import parse, parseString
    
    ex = vscp.vscpEventEx()

    ex.vscpclass = vc.VSCP_CLASS1_MEASUREMENT
    ex.vscptype = vt.VSCP_TYPE_MEASUREMENT_TEMPERATURE

    # 32-bit float coding = 100
    ex.sizedata = 4
    ex.data[0] = 11
    ex.data[1] = 22
    ex.data[2] = 33
    ex.data[3] = 44
    rv,s = vhlp.convertEventExToXML( ex )
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
    assert 11 == int(b[0],16)
    assert 22 == int(b[1],16)
    assert 33 == int(b[2],16)
    assert 44 == int(b[3],16)
```

### See Also
[convertEventToXML](converteventtoxml.md)



[filename](./bottom_copyright.md ':include')