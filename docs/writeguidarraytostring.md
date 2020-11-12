


```clike
int writeGuidArrayToString( const unsigned char * pGUID, 
                                    char *strGUID,
                                    size_t len )
```

### Parameters

#### pGUID
A 16 byte GUID array.

#### strGUID
Pointer to buffer that can hold the GUID in string form.

#### len
Size of string buffer.

### Return Value
VSCP_ERROR_SUCCESS on success. 

### Description
Write GUID from byte array to string. 

#### C example

```clike
if ( VSCP_ERROR_SUCCESS == writeGuidArrayToString( GUID2, strguid2, sizeof( strguid2 )-1 ) ) {
    printf( "GUID=%s\n", strguid2 );
}
else {
    printf( "Error: writeGuidArrayToString\n");
}
```




[filename](./bottom_copyright.md ':include')