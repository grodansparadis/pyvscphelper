

```clike
int reverseGUID(unsigned char *pGUID)
```

```python
xxxx
```

### Parameters

#### pGUID1
GUID array to be reversed.


### Return Value
Return VSCP_ERROR_SUCCESS on success. 

### Description
Reverse a GUID array. 

#### C example

```clike
writeGuidArrayToString( GUID2, strguid2, sizeof( strguid2 )-1 );
printf( "GUID before reverse = %s\n", strguid2 );
if ( VSCP_ERROR_SUCCESS == reverseGUID( GUID2 ) ) {
    writeGuidArrayToString( GUID2, strguid2, sizeof( strguid2 )-1 );
    printf( "GUID  after reverse = %s\n", strguid2 );
}
else {
    printf( "\aError: reverseGUID\n");
}
```



[filename](./bottom_copyright.md ':include')