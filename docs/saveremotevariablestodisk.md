

```clike
int saveRemoteVariablesToDisk( long handle ) 
```

### Parameters

#### handle
Handle for the communication channel obtained from a call to [newSession](newsession.md).

### Return Value
Return VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while in a receive loop. 

### Description
Saves variables marked as persistent to disk. 

#### C example

```clike
// Save variables marked as persistent
if ( VSCP_ERROR_SUCCESS == 
       ( rv = saveRemoteVariablesToDisk( handle1 ) ) )  {
    printf( "Command success: saveRemoteVariablesToDisk on channel 1\n" );
}
else {
    printf("\aCommand error: saveRemoteVariablesToDisk on channel 1  Error code=%d\n", rv);
}
```



[filename](./bottom_copyright.md ':include')