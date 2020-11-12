

```clike
int pycheckReply( handle, bclear )
```

### Parameters

#### handle
Handle for the communication channel obtained from a call to [newSession](newsession.md).

#### bclear
If TRUE (not zero) the input buffer will be cleared before starting to wait for a +OK/-OK in the incoming data.


### Return Value
VSCP_ERROR_SUCCESS if the VSCP daemon respond with “+OK” after it has received the command and VSCP_ERROR_ERROR if not or no response before the timeout expires. 

### Description
Check reply data for “+OK”/“-OK” on server. 


### Example

```python
import vscp
import vscphelper as vhlp

print("command: checkReply")
rv = vhlp.checkReply( h1, command, 1)
if vscp-VSCP_ERROR_SUCCESS != rv :
    vhlp.closeSession(h1)
    raise ValueError('Command error: ''checkReply''  Error code=%d' % rv ) 
```

### See Also
[doCommand](docommand.md)



[filename](./bottom_copyright.md ':include')