


```clike
int getStatistics( handle, statistics )
```

### Parameters

#### handle
Handle for the communication channel obtained from a call to [newSession](newsession.md).

#### pStatistics (c/c++)
A pointer to a VSCP statistics structure as defined in [vscp.h](https://github.com/grodansparadis/vscp_software/blob/master/src/vscp/common/vscp.h). 


### Return Value
Return VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while in a receive loop. 

### Description
Get VSCP statistics. 


### Example - Get statistics

```python
import vscp
import vscphelper as vhlp

...

print("Get statistics")
statistics = VSCPStatistics()
rv = vhlp.getStatistics( h1, statistics )
if vscp.VSCP_ERROR_SUCCESS != rv :
    vhlp.closeSession(h1)
    raise ValueError('Command error: pysetStatistics  Error code=%d' % rv )      
print("Received frames = %d" % statistics.cntReceiveFrames)
print("Transmitted frames = %d" % statistics.cntTransmitFrames)
print("Receive data = %d" % statistics.cntReceiveData)
print("Transmitted data = %d" % statistics.cntTransmitData)
print("Overruns = %d" % statistics.cntOverruns)
```



[filename](./bottom_copyright.md ':include')