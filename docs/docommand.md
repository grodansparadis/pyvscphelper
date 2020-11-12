

```clike
int doCommand( handle, command )
```

### Parameters

#### handle
Handle for the communication channel obtained from a call to [newSession](newsession.md).

#### cmd
This is the command that should be sent to the server. It should be terminated with “\r\n”.


### Return Value
VSCP_ERROR_SUCCESS if the VSCP daemon respond with +OK after it has received the command and VSCP_ERROR_ERROR if not (-OK) or no response before the timeout expires. VSCP_ERROR_CONNECTION is returned if the communication channel is not open. VSCP_ERROR_INVALID_HANDLE is returned if an invalid handle is given. 

### Description
Send a command over the communication link. The command should have “\r\n” to it's end. The response from the server will be checked for +OK. 


### Example

```python
import vacp
import vscphelper as vhlp

print("command: doCommand")
command = "NOOP\r\n"
rv = vhlp.doCommand( h1, command )
if vscp.VSCP_ERROR_SUCCESS != rv :
    vhlp.closeSession(h1)
    raise ValueError('Command error: ''doCommand''  Error code=%d' % rv ) 
```

### See Also
[checkReply](checkreply.md)  
[clearLocalInputQueue](clearlocalinputqueue.md)



[filename](./bottom_copyright.md ':include')