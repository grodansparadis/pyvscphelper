


```clike
(rv,e) convertStringToEvent( e, str )
```

### Parameters

#### e
The VSCP event ex that will be written from the string data

### Return Value
Tuple with return value and resulting event. VSCP_ERROR_SUCCESS is returned on success. 

### Description
Write VSCP event content to a string. 

### Example

```python
    e = vscp.vscpEvent()
    str = "0,10,6,0,2020-11-24T17:28:11Z,4216090068,00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00,0x80,0x02,0x1B,0x22"
    rv,e = vhlp.convertStringToEvent( e, str )
    print(rv)
    #print(e.dump())
    assert rv == vscp.VSCP_ERROR_SUCCESS
    assert e.vscpclass == 10
    assert e.vscptype == 6
    assert e.timestamp == 4216090068
    assert e.year == 2020
    assert e.month == 11
    assert e.day == 24
    assert e.hour == 17
    assert e.minute == 28
    assert e.second == 11
    assert e.pdata[0] == 128
    assert e.pdata[1] == 2
    assert e.pdata[2] == 0x1b
    assert e.pdata[3] == 0x22
```

### See Also

[writeVscpEventExToString](writevscpeventextostring.md)



[filename](./bottom_copyright.md ':include')
