

```clike
int setEventDateTimeBlockToNow( vscpEvent *pEvent )
```

### Parameters

#### pEvent
Pointer to event that will get the datetime block set to **now**.

### Return Value
VSCP_ERROR_SUCCESS is returned on success. 

### Description
Get date/time block for an event. 

#### C example

```clike
vscpEvent *pEvent;
setEventDateTimeBlockToNow( pEvent );
```
[setEventExDateTimeBlockToNow](seteventexdatetimeblocktonow.md)



[filename](./bottom_copyright.md ':include')