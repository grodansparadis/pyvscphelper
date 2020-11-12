


```clike
int pyopenInterface( handle, interface, flags )
```

### Parameters

#### handle
Handle for the communication channel obtained from a call to [newSession](newsession.md).one

#### interface
Pointer to a string with the name of interface to open. The format of this string is

    host;username;password

or

    tcp://host;username;password

where in both cases host is

    host-address:port

#### flags
Flags to use for the interface. Currently not used.


### Return Value
Possible return values are the same as for [Open](open.md)

### Description
Opens a session to the TCP/IP interface of a VSCP server. 

#### C example


### Example

```python
import vscp
import vscphelper as vhlp

print("\n\nConnection in progress...")
rv = vhlp.openInterface(h1,"127.0.0.1:9598;admin;secret")
if vscp.VSCP_ERROR_SUCCESS == rv :
    print("Command success: openInterface on channel 1")
else:
    vhlp.closeSession(h1)
    raise ValueError('Command error: openInterface on channel 1  Error code=%d' % rv )
```

### See Also
[open](open.md)  
[close](close.md)



[filename](./bottom_copyright.md ':include')