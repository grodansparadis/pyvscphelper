
```clike
int pyenterReceiveLoop( handle )
```

### Parameters

#### handle
Handle for the communication channel obtained from a call to [newSession](newsession.md).

### Return Value
Return VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while in a receive loop. 

### Description
Enter the receive loop. After this command only quitReceiveLoop and Close and the blocking receive methods [blockingReceiveEvent](blockingreceiveevent.md) / [blockingReceiveEventEx](blockingreceiveeventex.md) is available. The intent of the command is for threaded communication where one thread is sending events and one is receiving events and can use blocking calls to do so. 


### Example

```python
import vscp
import vscphelper as vhlp

...

print("Enter receive loop. Will lock channel on just receiving events")
if vscpVSCP_ERROR_SUCCESS == vhlp.enterReceiveLoop(h1):
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
        print("failed to leave receive loop")    
 
else:    
    print("Failed to enter receive loop!")
```

### See Also
[quitReceiveLoop](quitreceiveloop.md)  
[blockingReceiveEvent](blockingreceiveevent.md)  
[blockingReceiveEventEx](blockingreceiveeventex.md)



[filename](./bottom_copyright.md ':include')