

```clike
bool convertEventToCanal( canalMsg *pcanalMsg, 
                        const vscpEvent *pvscpEvent )
```

```python
xxxx
```

### Parameters

#### pcanalMsg
CANAL message that will hold result.

#### pvscpEvent
VSCP event that will be converted.

### Return Value
VSCP_ERROR_SUCCESS on succes. 

### Description
Convert VSCP event to CANAL message. 

#### C example

```clike
if ( VSCP_ERROR_SUCCESS == convertEventToCanal( &canalMsg, pEvent ) ) {
    printf( "OK convertEventToCanal id=%08X\n", canalMsg.id );
}
else {
    printf( "\aError: convertEventToCanal\n");
}
```

### See Also
[convertCanalToEvent](convertcanaltoevent.md)  
[convertCanalToEventEx](convertcanaltoeventex.md)



[filename](./bottom_copyright.md ':include')