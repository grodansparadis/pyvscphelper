

```clike
int writeGuidToString( const vscpEvent *pEvent, 
                                char *pStr, 
                                size_t len )
```

### Parameters

#### pEvent
VSCP event.

#### pStr
Pointer to GUID in string form.

#### len
Size of string buffer.


### Return Value
VSCP_ERROR_SUCCESS on success. 

### Description
Write GUID from VSCP event to string. 

#### C example


```clike
if ( VSCP_ERROR_SUCCESS == getGuidFromString( pEvent, strguid ) ) {
   writeGuidToString( pEvent, strguid2, sizeof( strguid2 )-1 );
   printf( "GUID=%s\n", strguid2 );
}
else {
    printf( "\aError: writeGuidArrayToString\n");
}
```

### See Also
[writeGuidToStringEx](writeguidtostringex.md)



[filename](./bottom_copyright.md ':include')