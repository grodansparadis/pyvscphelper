

```clike
(rv,str) convertEventToJSON( e  )
```

### Parameters

#### e
VSCP event.

### Return Value
Return a tuple consisting of a return value and the JSON string. A return value of VSCP_ERROR_SUCCESS is returned on success, VSCP_ERROR_BUFFER_TO_SMALL is returned if the size of the supplied buffer is to small. 

### Description
Write VSCP event on JSON format to string. Format is specified in [vscp.h](https://github.com/grodansparadis/vscp/blob/master/src/vscp/common/vscp.h). 

### Example

```python
    import json
    
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

    rv,s = vhlp.convertEventToJSON( e )
    print(rv)
    print(s)
    assert rv == vscp.VSCP_ERROR_SUCCESS
    j = json.loads(s)
    print("class = ",j["vscpClass"])
    assert 10 == j["vscpClass"]
    print("Type = ", j["vscpType"])
    assert 6 == j["vscpType"]
    assert 0x80 == j["vscpData"][0]
    assert 0x02 == j["vscpData"][1]
    assert 0x1B == j["vscpData"][2]
    assert 0x22 == j["vscpData"][3]
```

### See Also
[convertEventExToJSON](converteventextojson.md)



[filename](./bottom_copyright.md ':include')