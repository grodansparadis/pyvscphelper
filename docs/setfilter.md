
```clike
int pysetFilter( handle, filter )
```

### Parameters

#### handle
Handle for the communication channel obtained from a call to [newSession](newsession.md).

#### filter 

VSCP filter structure that should be applied to the sending stream on the server. 


### Return Value
Return VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while in a receive loop. 

### Description
Set VSCP filter/mask.

#### Example - Set filter

```python
import vscp
import vscphelper as vhlp

...


# Set filter
filter = vscp.vscpEventFilter()
filter.mask_class = 0xFFFF                          # All bits should be checked
filter.filter_class = vscp.VSCP_CLASS1_MEASUREMENT  # Only CLASS1.MEASUREMENT received
rv = vhlp.setFilter( h1, filter )
if vscp.VSCP_ERROR_SUCCESS != rv :
    vhlp.closeSession(h1)
    raise ValueError('Command error: setFilter  Error code=%d' % rv )
 
print("Enter receive loop. Will lock channel for 60 seconds or unit CLASS1.MEASUREMENT event received")
if vscp.VSCP_ERROR_SUCCESS == vhlp.enterReceiveLoop(h1):
    cnt = 0   
    rv = -1
    while vscp.VSCP_ERROR_SUCCESS != rv:
        ex = vscp.vscpEventEx()
        rv = vhlp.blockingReceiveEventEx(h1,ex, 1000 )
 
        if vscp.VSCP_ERROR_SUCCESS == rv: 
            ex.dump()
        else: 
            print("Waiting for CLASS1.MEASUREMENT event in blocking mode rv=%d" % rv)
 
        cnt += 1
        if ( cnt > 60 ):
            print("Not received within 60 seconds. We quit!")
            break
 
    if vscp.VSCP_ERROR_SUCCESS == vhlp.quitReceiveLoop(h1):
        print("Successfully left receive loop")
    else:
        print("failed to leave receive loop")    
 
else:    
    print("Failed to enter receive loop!")


```

### Example - Clear filter

```python
import vscp
import vscphelper as vhlp

...

# Clear filter
print("Clear filter")
filter = vscp.vscpEventFilter()
filter.clear()
rv = vhlp.setFilter( h1, filter )
if vscp.VSCP_ERROR_SUCCESS != rv :
    vhlp.closeSession(h1)
    raise ValueError('Command error: pysetFilter  Error code=%d' % rv )
```





[filename](./bottom_copyright.md ':include')