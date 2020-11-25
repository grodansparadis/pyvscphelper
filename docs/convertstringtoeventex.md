


```clike
(rv,ex) convertStringToEventEx( ex, str )
```

### Parameters

#### ex
The VSCP event ex that will be written from the string data

### Return Value
Tuple with return value and resulting event ex. VSCP_ERROR_SUCCESS is returned on success. 

### Description
Write VSCP event content to a string. 

### Example

```python
    ex = vscp.vscpEventEx()
    str = "0,10,6,0,2020-11-24T17:28:11Z,4216090068,00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00,0x0B,0x16,0x21,0x2C"
    rv,e2 = vhlp.convertStringToEventEx( ex, str )
    print(rv)
    print(e2.dump())
    assert rv == vscp.VSCP_ERROR_SUCCESS
    assert e2.vscpclass == 10
    assert e2.vscptype == 6
    assert e2.timestamp == 4216090068
    assert e2.year == 2020
    assert e2.month == 11
    assert e2.day == 24
    assert e2.hour == 17
    assert e2.minute == 28
    assert e2.second == 11
    assert e2.data[0] == 11
    assert e2.data[1] == 0x16
    assert e2.data[2] == 0x21
    assert e2.data[3] == 0x2c
```

### See Also

[writeVscpEventExToString](writevscpeventextostring.md)



[filename](./bottom_copyright.md ':include')
