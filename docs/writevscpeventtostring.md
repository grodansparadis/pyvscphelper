


```clike
int writeVscpEventToString( const vscpEvent *pEvent, 
                                    char *pstr, 
                                    size_t len )
```

### Parameters

#### pEvent
The VSCP event which will be written to the string buffer.

#### pstr
Pointer to string buffer that will receive result.

#### len
Size of buffer.

### Return Value
VSCP_ERROR_SUCCESS is returned on success. 

### Description
Write VSCP event content to a string. 

#### C example

```clike
char eventBuf[128];
if ( VSCP_ERROR_SUCCESS == writeVscpEventToString( pEvent, eventBuf, sizeof( eventBuf )-1 ) ) {
    printf( "OK writeVscpEventToString Event = %s\n", eventBuf );    
}
else {
    printf( "\aError: writeVscpEventToString\n");
}
```

### See Also

[writeVscpEventExToString](writevscpeventextostring.md)



[filename](./bottom_copyright.md ':include')
