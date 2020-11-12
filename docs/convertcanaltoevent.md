

```clike
int convertCanalToEvent( vscpEvent *pvscpEvent,
                                    const canalMsg *pcanalMsg,
                                    unsigned char *pGUID )
```

### Parameters

#### pvscpEvent
VSCP event that will hold the conversion result.

#### pcanalMsg
CANAL message that should be converted.

#### pGUID
GUID for event.

### Return Value
VSCP_ERROR_SUCCESS on success. 

### Description
Convert CANAL message to VSCP event. 

#### C example

```clike
canalMsg canalMsg;
canalMsg.id = 0x0c0a0601;
canalMsg.sizeData = 3;
canalMsg.data[0] = 138;
canalMsg.data[1] = 0;
canalMsg.data[2] = 30;
if ( VSCP_ERROR_SUCCESS == convertCanalToEvent( pEvent,
                                                          &canalMsg,
                                                          GUID2 ) ) {
    printf( "OK convertCanalToEvent VSCP class=%d Type=%d\n", 
                   pEvent->vscp_class, pEvent->vscp_type );
}
else {
    printf( "\aError: convertCanalToEvent\n");
}
```

### See Also
[convertCanalToEventEx](convertcanaltoeventex.md)  [convertEventToCanal](converteventtocanal.md)  [convertEventExToCanal](converteventextocanal.md)



[filename](./bottom_copyright.md ':include')