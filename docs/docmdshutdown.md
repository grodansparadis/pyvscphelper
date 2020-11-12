
```clike
int doCmdShutDown( handle )
```

### Parameters

#### handle
Handle for the communication channel obtained from a call to [newSession](newsession.md).

### Return Value
Return VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while in a receive loop. 

### Description
Shut down the daemon. Needless to say this is a privileged command on the server side. 


### Example

```python
import vscp
import vscphelper as vhlp

...

print("Shut down server")
rv = vhlp.serverShutDown( h1 )
if vscp.VSCP_ERROR_SUCCESS != rv :
    vhlp.closeSession(h1)
    raise ValueError('Command error: serverShutDown  Error code=%d' % rv )
```



[filename](./bottom_copyright.md ':include')
