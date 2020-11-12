
```clike
int pyclearDaemonEventQueue( handle )
```

### Parameters

#### handle
Handle for the communication channel obtained from a call to [newSession](newsession.md).

### Return Value
VSCP_ERROR_SUCCESS if the VSCP daemon cleared the queue and VSCP_ERROR_ERROR. if not or no response is received before the timeout expires. VSCP_ERROR_CONNECTION is returned if the communication channel is not open. VSCP_ERROR_INVALID_HANDLE is returned if an invalid handle is given. 

### Description
Clear the receiving side (to us) event queue on the VSCP daemon. 


### Example
```python
import vscp
import vscphelper as vhlp

...

print("Empty VSCP server queue")
rv = vhlp.clearDaemonEventQueue(h1)
if vscp.VSCP_ERROR_SUCCESS == rv:
    print("Server queue now is empty")
else:
    print("Failed to clear server queue", rv)
```




[filename](./bottom_copyright.md ':include')