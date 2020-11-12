

```clike
int isConnected( handle )
```

### Parameters

#### handle
Handle for the communication channel obtained from a call to [newsession](newsession.md).

### Return Value
VSCP_ERROR_SUCCESS if the session is active and VSCP_ERROR_ERROR if it is inactive. VSCP_ERROR_INVALID_HANDLE is returned if an invalid handle is given. 

### Description
Check if the session is active or not. 

### Example

```python
import vscp
import vscphelper as vhlp

print("\n\nConnection in progress...")
rv = vhlp.open(h1,"127.0.0.1:9598","admin","secret")
if vscp.VSCP_ERROR_SUCCESS == rv :
    print("Command success: open on channel 1")
else:
    vphlp.closeSession(h1)
    raise ValueError('Command error: open on channel 1  Error code=%d' % rv )
 
if ( vscp.VSCP_ERROR_SUCCESS == vhlp.isConnected(h1) ):
    print("CONNECTED!")
else:
    print("DISCONNECTED!")
```




[filename](./bottom_copyright.md ':include')
