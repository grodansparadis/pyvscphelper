

```clike
int pysendEvent( handle, event )
```

### Parameters

#### handle
Handle for the communication channel obtained from a call to [newSession](newsession.md).

#### pEvent
The level I or level II event to send. The structure vscpEvent is defined in [vscp.h](https://github.com/grodansparadis/vscp_software/blob/master/src/vscp/common/vscp.h)


### Return Value
Return VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while in a receive loop. 

### Description
Send a VSCP event. If the event is successfully sent or not it's the calling programs responsibility to deallocate the event. It's easy to forget to free the data part of an event created on the stack.

Note that there is no need to calculate a crc for the data it is only used as placeholder for more insecure transfer mechanisms. Also head, obid, the UTC timeblock and timestamp can be set to zero in most cases. The timeblock and timestamp will be set by the server interface when the event is received.

[sendEventEx](sendeventex.md) may a better alternative to use with Python as that version does not have dynamically allocated event data but one should be aware that it is more wasteful with memory. 


### Example

```python
import vscp
import vscphelper as vhlp

...

e = vscp.vscpEvent()
e.timestamp = 0
e.vscpclass = 20
e.vscptype = 9
e.sizedata = 3
p = (c_ubyte*3)()
p[0] = 11
p[1] = 22
p[2] = 33
e.pdata = cast(p, POINTER(c_ubyte))
 
print("------------------------------------------------------------------------")
print "command: sendEvent"
rv = vhlp.sendEvent(h1,e)
if vscp.VSCP_ERROR_SUCCESS != rv :
    vhlp.closeSession(h1)
    raise ValueError('Command error: sendEvent  Error code=%d' % rv )
e.pdata = None 
```

### See Also
[sendEventEx](sendeventex.md)



[filename](./bottom_copyright.md ':include')