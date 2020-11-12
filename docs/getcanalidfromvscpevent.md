

```clike
unsigned long 
getCANALidFromVSCPevent( const vscpEvent *pEvent )
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
constr_canal_id2 = getCANALidFromVSCPevent( pEvent ); 
if ( 0x0c0a0600 == constr_canal_id2 ) {
    printf("Nickname = %08X\n", constr_canal_id2 );
}
else {
    printf("\aError: getCANALidFromVSCPevent = %08X\n", constr_canal_id2 );
} 
```

### See Also
[getCANALidFromVSCPeventEx](getcanalidfromvscpeventex.md)



[filename](./bottom_copyright.md ':include')