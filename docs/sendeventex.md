
```clike
int sendEventEx( handle, eventex )
```

### Parameters

#### handle
Handle for the communication channel obtained from a call to [newSession](newsession.md).

#### pEvent

The level I or level II event to send. The structure *vscpEventEx* is defined in [vscp.h](https://github.com/grodansparadis/vscp_software/blob/master/src/vscp/common/vscp.h)

### Return Value
Return VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while in a receive loop. 

### Description
Send a VSCP event. If the event is not successfully sent it's the calling programs responsibility to deallocate the event.

Note that there is no need to calculate a crc for the data it is only used as placeholder for more insecure transfer mechanisms. Also head, obid, the UTC timeblock and timestamp can be set to zero in most cases. The timeblock and timestamp will be set by the server interface when the event is received. 


### Example

```python
import vscp
import vscphelper as vhlp

...

ex = vscp.vscpEventEx()
ex.timestamp = 0
ex.vscpclass = 10
ex.vscptype = 99
ex.sizedata = 3
ex.data[0] = 1
ex.data[1] = 2
ex.data[2] = 3
print "command: sendEventEx"
rv = vhlp.sendEventEx(h1,ex)
if VSCP_ERROR_SUCCESS != rv :
    pycloseSession(h1)
    raise ValueError('Command error: sendEventEx  Error code=%d' % rv )
```

### See Also
[sendEventEx](sendevent.md)



[filename](./bottom_copyright.md ':include')