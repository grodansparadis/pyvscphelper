

```clike
int convertVSCPfromEx( vscpEvent *pEvent, 
                    const vscpEventEx *pEventEx )
```

### Parameters

#### pEvent
VSCP event to convert to.

#### pEventEx
VSCP event ex to convert from.

### Return Value
VSCP_ERROR_SUCCESS on success. 

### Description
Convert VSCP ex. event form to standard form.

#### C example

```clike
if ( VSCP_ERROR_SUCCESS != convertVSCPfromEx( pEvent, &ex4 ) ) {
    printf( "\aError: convertVSCPfromEx\n");
}
```

### See Also
[convertVSCPtoEx](convertvscptoex.md)



[filename](./bottom_copyright.md ':include')