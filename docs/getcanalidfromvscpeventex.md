

```clike
unsigned long 
getCANALidFromVSCPeventEx( const vscpEventEx *pEvent )
```
### Parameters

#### pEvent
VSCP event.

### Return Value
CANAL (CAN) id.

### Description
Get CANAL id (CAN id) from VSCP event. 

#### C example

```clike
constr_canal_id2 = getCANALidFromVSCPeventEx( &ex ); 
if ( 0x0c0a0600 == constr_canal_id2 ) {
    printf("Nickname = %08X\n", constr_canal_id2 );
}
else {
    printf("\aError: getCANALidFromVSCPeventEx = %08X\n", constr_canal_id2 );
} 
```

### See Also
[getCANALidFromVSCPevent](getcanalidfromvscpevent.md)



[filename](./bottom_copyright.md ':include')