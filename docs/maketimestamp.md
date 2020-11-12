

```clike
unsigned long makeTimeStamp( void )
```

### Parameters

#### handle
Handle for the communication channel obtained from a call to [newSession](newsession.md).

### Return Value
Timestamp in microseconds.

### Description
Get new VSCP timestamp. 

#### C example

```clike
printf( "makeTimeStamp  %04X\n", makeTimeStamp() );
```



[filename](./bottom_copyright.md ':include')