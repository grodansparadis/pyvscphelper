

```clike
int close( handle )
```

### Parameters

#### handle
Handle for the communication channel obtained from a call to [newSession](newsession.md).

### Return Value
VSCP_ERROR_SUCCESS is returned on sucess. VSCP_ERROR_INVALID_HANDLE will be returned if the interface is not initialized. 

### Description
Close the interface. 


### Example

```python
import vscp
import vscphelper as vhlp

print("command: close")
rv = vhlp.close(h1)
if vscp.VSCP_ERROR_SUCCESS != rv :
    vhlp.closeSession(h1)
    raise ValueError('Command error: close  Error code=%d' % rv )
```

### See Also
[open](open.md)  
[openInterface](openinterface.md)  



[filename](./bottom_copyright.md ':include')