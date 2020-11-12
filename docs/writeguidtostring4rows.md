

```clike
int writeGuidToString4Rows( const vscpEvent *pEvent, 
                                      char *strGUID,
                                      size_t len )
```

### Parameters

#### pEvent
VSCP event.

#### strGUID
String that get formatted GUID.

#### len
Size of string buffer.

### Return Value
VSCP_ERROR_SUCCESS on success. 

### Description
Write GUID from VSCP event to string with four bytes on each row separated by “\r\n”. 

#### C example

```clike
if ( VSCP_ERROR_SUCCESS == writeGuidToString4Rows( pEvent, strguid2, sizeof( strguid2 )-1 ) ) {
    printf( "GUID\n%s\n", strguid2 );
}
else {
    printf( "Error: writeGuidArrayToString\n");
}
```

### See Also
[writeGuidToString4RowsEx](writeguidtostring4rowsex.md)



[filename](./bottom_copyright.md ':include')