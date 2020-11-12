

```clike
int setEventExDateTimeBlockToNow( vscpEventEx *pEventEx )
```

### Parameters

#### pEventEx
Pointer to event that willhave its daettime block set to the current time.

### Return Value
VSCP_ERROR_SUCCESS is returned on success. 

### Description
Get date/time block for an ex event. 

#### C example

```clike
vscpEventEx *pEventEx;
setEventExDateTimeBlockToNow( pEventEx );
```

### See Also
[setEventDateTimeBlockToNow](seteventdatetimeblocktonow.md)



[filename](./bottom_copyright.md ':include')