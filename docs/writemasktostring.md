

```clike
int writeMaskToString( vscpEventFilter *pFilter, 
                                char * strMask )
```

### Parameters

#### pFilter
Filter structure to write mask from.

#### strMask
String that will get mask in comma separated string form. Must be at least 65 bytes.

    mask-priority, mask-class, mask-type, mask-GUID

### Return Value
VSCP_ERROR_SUCCESS on success. 

### Description
Write the mask in comma separated form to a string. If strMask is an empty string elements in mask will be set to zero. 

#### C example

```clike
if ( VSCP_ERROR_SUCCESS != writeMaskToString( &filter, 
                "1,0x0000,0x0006,ff:ff:ff:ff:ff:ff:ff:01:00:00:00:00:00:00:00:00" ) ) {
    printf( "\aError: writeMaskToString\n");   
} 
```

### See Also
[readMaskFromString](readmaskfromstring.md)




[filename](./bottom_copyright.md ':include')