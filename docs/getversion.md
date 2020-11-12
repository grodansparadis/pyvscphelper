

```clike
unsigned long pygetVersion( handle, 
                            MajorVer,
                            MinorVer,
                            SubMinorVer )
```

### Parameters

#### handle
Handle for the communication channel obtained from a call to [newSession](newsession.md).

#### MajorVer
VSCP server major version.

#### MinorVer
VSCP server minor version.

#### SubMinorVer
VSCP server sub minor version.

### Return Value
Return VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while in a receive loop.

### Description
Get the version of the remote VSCP server. 

### Example

```python
import vscp
import vscphelper as vhlp

...

print("command: Get sever version")
(rv,v1,v2,v3) = vhlp.getVersion(h1)
if vscp.VSCP_ERROR_SUCCESS != rv :
    vhlp.closeSession(h1)
    raise ValueError('Command error: ''pygetVersion''  Error code=%d' % rv )
print("Server version = %d.%d.%d" % (v1.value,v2.value,v3.value))
```




[filename](./bottom_copyright.md ':include')