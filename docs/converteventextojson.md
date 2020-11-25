

```clike
(rv,str) convertEventExToJSON( e  )
```

### Parameters

#### ex
VSCP event ex

### Return Value
Return a tuple consisting of a return value and the JSON string. A return value of VSCP_ERROR_SUCCESS is returned on success, VSCP_ERROR_BUFFER_TO_SMALL is returned if the size of the supplied buffer is to small. 

### Description
Write VSCP event-ex on JSON format to string. Format is specified in [vscp.h](https://github.com/grodansparadis/vscp/blob/master/src/vscp/common/vscp.h). 

### Example

```python
    import json
    
    ex = vscp.vscpEventEx()

    ex.vscpclass = vc.VSCP_CLASS1_MEASUREMENT
    ex.vscptype = vt.VSCP_TYPE_MEASUREMENT_TEMPERATURE

    # 32-bit float coding = 100
    ex.sizedata = 4
    ex.data[0] = 11
    ex.data[1] = 22
    ex.data[2] = 33
    ex.data[3] = 44
    rv,s = vhlp.convertEventExToJSON( ex )
    print(rv)
    print(s)
    assert rv == vscp.VSCP_ERROR_SUCCESS
    j = json.loads(s)
    print("class = ",j["vscpClass"])
    assert 10 == j["vscpClass"]
    print("Type = ", j["vscpType"])
    assert 6 == j["vscpType"]
    assert 11 == j["vscpData"][0]
    assert 22 == j["vscpData"][1]
    assert 33 == j["vscpData"][2]
    assert 44 == j["vscpData"][3]
```

### See Also
[convertEventToJSON](converteventtojson.md)



[filename](./bottom_copyright.md ':include')