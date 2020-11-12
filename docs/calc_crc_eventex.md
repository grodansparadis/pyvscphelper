

```clike
short calc_crc_Event( vscpEvent *pEvent, 
                                int bSet )
```

### Parameters

#### pEvent
VSCP event.

#### bSet
If true (non zero) write the CRC into the event structure crc member.

### Return Value
VSCP CRC. 

### Description
Calculate VSCP CRC and optionally set it. 

#### C example

```clike
unsigned short crc = calc_crc_Event( pEvent, false );
printf("CRC = %04X\n", crc );
```

### See Also
[calc_crc_Event](calc_crc_event.md)



[filename](./bottom_copyright.md ':include')