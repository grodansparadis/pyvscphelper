

```clike
int pyisDataAvailable( handle, count )
```

### Parameters

#### handle
Handle for the communication channel obtained from a call to [newSession](newsession.md).

### count
Variable that gets the number of events waiting in the queue on a successful call.


### Return Value
Return VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while in a receive loop. 

### Description
Check the number of events (if any) that are available in the remote input queue. 

#### Example

```python
import vscp
import vscphelper as vhlp

....

print("Waiting for incoming data...")
 
cntAvailable = ctypes.c_uint(0)
while cntAvailable.value==0:
    print('Still waiting...')
    time.sleep(1)
    vhlp.isDataAvailable(h1,cntAvailable)
 
print('%d event(s) is available' % cntAvailable.value)
 
for i in range(0,cntAvailable.value):
    ex = vscp.vscpEventEx()
    if vscp.VSCP_ERROR_SUCCESS == vhlp.receiveEventEx(h1,ex):
        ex.dump()
```



[filename](./bottom_copyright.md ':include')