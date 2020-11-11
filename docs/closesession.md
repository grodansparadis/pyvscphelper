

```python
closeSession(handle)
```

#### handle
Handle for the communication channel obtained from a call to [newsession](newsession.md).


### Return Value
Nothing

### Description
Close an open session. This is the last operation that should be done after you are done with a tcp/ip session or other work with te library. 


### Example
There is no Python sample yet

```python    
    import vscp
    import vscphelper as vhlp

    # Create new session
    h1 = vhlp.newSession()
    if (0 == h1):
        print("Failed to open new session")

    # Open a connection to a remote VSCP server    
    rv = vhlp.open(h1,"127.0.0.1:9598","admin","secret")
    if (rv != vscp.VSCP_ERROR_SUCCESS):
        vhlp.closeSession(h1)
        raise ValueError('Unable to connect to remote server')

    # Do no-operation command    
    rv = vhlp.noop(h1)
    if (rv != vscp.VSCP_ERROR_SUCCESS):
        vhlp.closeSession(h1)
        raise ValueError('Unable to perform noop command')

    # Close remote server connection
    vhlp.close(h1)

    # Give back session handle
    vhlp.closeSession(h1)
```



### See Also

[newSession](newsession.md)



[filename](./bottom_copyright.md ':include')