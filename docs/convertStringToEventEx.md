

```clike
int convertStringToEventEx( vscpEvent, 
                            string )
```

### Parameters

#### vscpEvent
VSCP event ex

#### string
VSCP event on string form. The string is on the form

```csv
head,class,type,obid,datetime,timestamp,GUID,data1,data2,data3....
```


### Return Value
VSCP_ERROR_SUCCESS is returned on success, VSCP_ERROR_BUFFER_TO_SMALL is returned if the size of the supplied buffer is to small. 

### Description
Convert a VSCP event on string form to a vscpEventEx.


### See Also
[convertStringToEvent](convertstringtoevent.md)



[filename](./bottom_copyright.md ':include')