


```python
c_long newSession()
```

### Parameters
none

### Return Value
A session handle or zero if a session could not be created. 

### Description

Opens a new communication session. This is the first function that should be called before a tcp/ip connection can be established. 

### Example 

Open a new session using Python.

```python
h1 = vhlp.newSession()
if (0 == h1):
    vhlp.closeSession(h1)
    raise ValueError('Unable to open a new vscphelp library session')
```

### See also
[closeSession](closesession.md)



[filename](./bottom_copyright.md ':include')