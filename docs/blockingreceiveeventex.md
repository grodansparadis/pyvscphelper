

```clike
int pyblockingReceiveEventEx( handle, eventex, timeout )
```

### Parameters

#### handle
Handle for the communication channel obtained from a call to [newSession](newsession.md).

#### pEvent (c/c++)
Pointer to event that will get event data after a sucessfull call. See receiveEvent for a description.

#### pEvent (Python)
Event that will get event data after a successfull call. See receiveEvent for a description.
timeout

This is the max time to block. Zero means wait forever.


### Return Value
Return VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while in a receive loop. 

### Description
Blocking receive one VSCP event from the remote VSCP server if there is one available in the server queue. 


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
        ex = vscp.vscpEventEx()
        rv = vhlp.blockingReceiveEventEx(h1,ex, 1000 )
 
        if vscp.VSCP_ERROR_SUCCESS == rv: 
            ex.dump()
        else:
            if vscp.VSCP_ERROR_TIMEOUT != rv:
                print("Blocking receive failed with error code = %d" % rv)
                break
            print("Waiting for event in blocking mode rv=%d" % rv)
 
    if vscp.VSCP_ERROR_SUCCESS == vhlp.quitReceiveLoop(h1):
        print("Successfully left receive loop")
    else:
        print("Failed to leave receive loop")
 
else:    
    print("Failed to enter receive loop!")
```

### See Also
[enterReceiveLoop](enterreceiveloop.md)   
[quitReceiveLoop](quitreceiveloop.md)   
[blockingReceiveEvent](blockingreceiveevent.md)



[filename](./bottom_copyright.md ':include')