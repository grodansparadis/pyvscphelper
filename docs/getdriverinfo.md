

```clike
(rv,strdriverinfo) = getDriverInfo( handle )
```

### Parameters

#### handle
Handle for the communication channel obtained from a call to [newSession](newsession.md).

### Return Value

A touple consisting of the the return vale and the driver info string is returned. For return codes see c/c++ return value.

Return value is VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while in a receive loop.


### Description
Get driver information. A buffer with size enough to hold the XML data must be supplied. For Python 32000 byte is used. 

### Example

```python
import vscp
import vscphelper as vhlp

...

print("Get driver info string")
(rv,strdriverinfo) = vhlp.getDriverInfo( h1 )
if vscp.VSCP_ERROR_SUCCESS != rv :
    vhlp.closeSession(h1)
    raise ValueError('Command error: pygetDriverInfo  Error code=%d' % rv )
print("Driver info string = %s" % strdriverinfo)
```



[filename](./bottom_copyright.md ':include')



