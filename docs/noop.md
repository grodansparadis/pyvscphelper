

```clike
int noop( handle )
```

### Parameters

#### handle
Handle for the communication channel obtained from a call to [newSession](newsession.md).

### Return Value
Return VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while in a receive loop. 

### Description
This is a command that can be used for test purposes. It does not do anything else then to send a command over the interfaces and check the result. 


### Example

```python
import vscp
import vscphelper as vhlp

... new session, open etc

print("command: noop")
rv = vhlp.noop( h1 )
if vscp.VSCP_ERROR_SUCCESS != rv :
    vhlp.closeSession(h1)
    raise ValueError('Command error: ''noop''  Error code=%d' % rv )
```




[filename](./bottom_copyright.md ':include')