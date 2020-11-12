

```clike
const char * pygetStatus( handle, status)
```

### Parameters

#### handle
Handle for the communication channel obtained from a call to [newSession](newsession.md).

#### status 
[VSCPStatus](https://github.com/grodansparadis/vscp_software/blob/master/src/vscp/common/vscp.h) structure that will hold status information after a successful call.

### Return Value
Return VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while in a receive loop. 

### Description
Fetch the status structure from the VSCP server. 


### Example

```python
import vscp
import vscphelper as vhlp

...

print("Get status")
status = VSCPStatus()
rv = vhlp.getStatus( h1, status )
if vscp.VSCP_ERROR_SUCCESS != rv :
    vhlp.closeSession(h1)
    raise ValueError('Command error: pysetFilter  Error code=%d' % rv )
print("Channel status = %d" % status.channel_status)
print("Channel status = %d" % status.lasterrorcode)
print("Channel status = %d" % status.lasterrorsubcode)
```



[filename](./bottom_copyright.md ':include')