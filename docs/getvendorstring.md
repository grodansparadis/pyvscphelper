

```clike
(rv,strversion) getVendorString( handle )
```

### Parameters

#### handle
Handle for the communication channel obtained from a call to [newSession](newsession.md).

### Return Value

#### Python
A tuple that consist of the return value (see c/c++ version) and the vendor string is returned. 

Return value is VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while in a receive loop. 

### Description
Fetch the vendor string from the driver. 

### Example

```python
import vscp
import vscphelper as vhlp

...

print("Get vendor string")
(rv,strvendor) = vhlp.getVendorString( h1 )
if vscp.VSCP_ERROR_SUCCESS != rv :
    vhlp.closeSession(h1)
    raise ValueError('Command error: pygetVendorString  Error code=%d' % rv )
print("Vendor string = %s" % strvendor)
```






[filename](./bottom_copyright.md ':include')
