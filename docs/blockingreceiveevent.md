

```clike
int blockingReceiveEvent( handle, event, timeout )
```

### Parameters

#### handle
Handle for the communication channel obtained from a call to [newSession](newsession.md).

#### event
Pointer to event that will get event data after a sucessful call. See [receiveEvent](receiveevent.md) for a description.

#### timeout
This is the max time to block. Zero means wait forever.

### Return Value
Return VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while NOT in a receive loop (see enterReceiveLoop. 

### Description
Blocking receive one VSCP event from the remote VSCP server if there is one available in the server queue. Data for the event is dynamically allocated and must be deleted by the application.

For Python use of [receiveEventEx](receiveeventex.md) may be simpler as there id no dynamically allocated data to take care off. 

### Example


```python
import vscp
import vscphelper as vhlp

...

print("Enter receive loop. Will lock channel on just receiving events")
if vscp.VSCP_ERROR_SUCCESS == vhlp.enterReceiveLoop(h1):
    print("Now blocking receive - will take forever if no events is received")
 
    rv = -1
    while vscp.VSCP_ERROR_SUCCESS != rv:
        e = vscp.vscpEvent()
        rv = vhlp.blockingReceiveEvent(h1,e, 1000 )
 
        if vscp.VSCP_ERROR_SUCCESS == rv: 
            e.dump()
        else:
            if vscp.VSCP_ERROR_TIMEOUT != rv:
                print("Blocking receive failed with error code = %d" % rv) 
                break
            print("Waiting for event in blocking moderv=%d" % rv)
 
    if vscp.VSCP_ERROR_SUCCESS == vhlp.quitReceiveLoop(h1):
        print("Successfully left receive loop")
    else:
        print("failed to leave receive loop")    
 
else:    
    print("Failed to enter receive loop!")
```

### See Also
[enterReceiveLoop](enterreceiveloop.md)   
[quitReceiveLoop](quitreceiveloop.md)   
[blockingReceiveEventEx](blockingreceiveeventex.md)



[filename](./bottom_copyright.md ':include')