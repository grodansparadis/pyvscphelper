

```clike
int pyclearLocalInputQueue( handle )
```

### Parameters

#### handle
Handle for the communication channel obtained from a call to [newSession](newsession.md).

### Return Value
rVSCP_ERROR_SUCCESS if the VSCP daemon cleared the queue and VSCP_ERROR_ERROR if not or no response is received before the timeout expires. VSCP_ERROR_INVALID_HANDLE is returned if an invalid handle is given. rrr

### Description
Clear the local communication input queue. This is the same things that is done when setting **bClear** for [checkReply](checkreply)

#### C example



### Example

```python
import vscp
import vscphelper as vhlp

print("command: pyclearLocalInputQueue")
command = "NOOP\r\n"
rv = vhlp.clearLocalInputQueue( h1 )
if vscp.VSCP_ERROR_SUCCESS != rv :
    vhlp.closeSession(h1)
    raise ValueError('Command error: ''clearLocalInputQueue''  Error code=%d' % rv )
```

### See Also
[checkReply](checkreply.md)  
[doCommand](docommand.md)



[filename](./bottom_copyright.md ':include')