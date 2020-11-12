

```clike
(rv,dllversion) = getDLLVersion( handle )
```

### Parameters

#### handle
Handle for the communication channel obtained from a call to [newSession](newsession.md).

### Return Value

Returned a tuple consisting of return value and dllversion. Return value is VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while in a receive loop.


### Description
Fetch the dll version from the VSCP server. This is the version of the interface. 

#### Example

```python
import vscp
import vscphelper as vhlp

...

print("Get DLL version")
(rv,dllversion) = vhlp.getDLLVersion( h1 )
if vscp.VSCP_ERROR_SUCCESS != rv :
    vhlp.closeSession(h1)
    raise ValueError('Command error: pygetStatus  Error code=%d' % rv )
print("DLL version = %d" % dllversion)
```



[filename](./bottom_copyright.md ':include')