

## xxx

```clike
bool convertEventExToCanal( canalMsg *pcanalMsg, 
                                       const vscpEventEx *pvscpEvent )
```

### Parameters

#### pcanalMsg
CANAL message that will hold result.

#### pvscpEvent
VSCP ex event that will be converted.


### Return Value
VSCP_ERROR_SUCCESS on succes. 

### Description
Convert VSCP event ex to CANAL message. 

#### C example

```clike
if ( VSCP_ERROR_SUCCESS == convertEventExToCanal( &canalMsg, &ex5 ) ) {
    printf( "OK convertEventExToCanal id=%08X\n", canalMsg.id );
}
else {
    printf( "\aError: convertEventExToCanal\n");
}
```

### See Also
[convertCanalToEvent](convertcanaltoevent.md)   [convertCanalToEventEx](convertcanaltoeventex.md)    [convertEventToCanal](converteventtocanal.md)  



[filename](./bottom_copyright.md ':include')