

```clike
int writeGuidToStringEc( const vscpEventEx *pEvent, 
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
VSCP_ERROR_SUCCESS on success

### Description
Write GUID from VSCP event to string. 

#### C example
mmmm

```clike
if ( VSCP_ERROR_SUCCESS == getGuidFromStringEx( &ex3, strguid ) ) {
    writeGuidToStringEx( &ex3, strguid2, sizeof( strguid2 )-1 );
    printf( "GUID=%s\n", strguid2 );
}
else {
    printf( "\aError: writeGuidArrayToString\n");
}

```


### See Also
[writeGuidToString](writeguidtostring.md)



[filename](./bottom_copyright.md ':include')