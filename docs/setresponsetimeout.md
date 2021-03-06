

```clike
int setResponseTimeout( handle, timeout )
```

### Parameters

#### handle

Handle for the communication channel obtained from a call to [newSession](newsession.md).

#### timeout 
Timeout given in milliseconds. Can be set also before a session is open.

### Return Value
VSCP_ERROR_SUCCESS is returned on success. VSCP_ERROR_INVALID_HANDLE is returned if an invalid handle is given. 

### Description
This is the timeout in seconds used when checking for replies after commands has been sent to the server. It can be changed anytime during a communication session. Default value is 3000 milliseconds. 


### See also
[setAfterCommandSleep](setaftercommandsleep.md)


[filename](./bottom_copyright.md ':include')