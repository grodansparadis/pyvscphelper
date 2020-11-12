

```clike
int getGuidFromStringEx( vscpEvent *pEvent, 
                            const char * pGUID )
```

### Parameters

#### pEvent
VSCP event ex.

#### pGUID
Pointer to GUID in string form.


### Return Value
VSCP_ERROR_SUCCESS on success.

### Description
Write GUID into VSCP event ex from a string. 

#### C example

```clike
char strguid[64], strguid2[64];
 
if ( VSCP_ERROR_SUCCESS == getGuidFromStringEx( &ex3, strguid ) ) {        
    writeGuidToStringEx( &ex3, strguid2, sizeof( strguid2 )-1 );
    printf( "GUID=%s\n", strguid2 );
}
else {
    printf( "\aError: writeGuidArrayToString\n");
}
```

### See Also
[getGuidFromString](getguidfromstring.md)



[filename](./bottom_copyright.md ':include')