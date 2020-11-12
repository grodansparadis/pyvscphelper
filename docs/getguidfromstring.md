

```clike
int getGuidFromString( vscpEvent *pEvent, 
                            const char *pGUID )
```
### Parameters

#### pEvent
VSCP event.

#### pGUID
Pointer to GUID in string form.

### Return Value
VSCP_ERROR_SUCCESS on success.

### Description
Write GUID into VSCP event from a string. 

#### C example
mmmm

```clike
char strguid[64], strguid2[64];
 
if ( VSCP_ERROR_SUCCESS == getGuidFromString( pEvent, strguid ) )  { 
    writeGuidToString( pEvent, strguid2, sizeof( strguid2 )-1 );
    printf( "GUID=%s\n", strguid2 );
}
else {
    printf( "\aError: writeGuidArrayToString\n");
}
```

### See Also
[getGuidFromString](getguidfromstring.md)



[filename](./bottom_copyright.md ':include')