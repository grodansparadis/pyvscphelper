

```clike
int convertVSCPtoEx( vscpEventEx *pEventEx, 
                              const vscpEvent *pEvent )
```

### Parameters

#### pEventEx
VSCP event ex to convert to

#### pEvent
VSCP event to convert to.

### Return Value
VSCP_ERROR_SUCCESS on success. 

### Description
Convert VSCP standard event form to ex form. 

#### C example

```clike
vscpEventEx ex4;
if ( VSCP_ERROR_SUCCESS != convertVSCPtoEx( &ex4, pEvent ) ) {
    printf( "\aError: getGuidFromStringToArray\n");
}
```


### See Also
[convertVSCPfromEx](convertvscpfromex.md)



[filename](./bottom_copyright.md ':include')