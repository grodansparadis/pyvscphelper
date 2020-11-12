

```clike
int quitReceiveLoop( handle )
```

### Parameters

#### handle
Handle for the communication channel obtained from a call to [newSession](newsession.md).

### Return Value
Return VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while in a receive loop. 

### Description
Quit the receive loop. 


### Example


```python
import vscp
import vscphelper as vhlp

...

if vscp.VSCP_ERROR_SUCCESS == vhlp.quitReceiveLoop(h1):
    print("Successfully left receive loop")
else:
    print("failed to leave receive loop")
```

### See Also
[enterReceiveLoop](enterreceiveloop.md)  
[blockingReceiveEvent](blockingreceiveevent.md)  
[blockingReceiveEventEx](blockingreceiveeventex.md)



[filename](./bottom_copyright.md ':include')