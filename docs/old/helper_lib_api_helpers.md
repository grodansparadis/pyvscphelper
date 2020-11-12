\\
----
\\ \\ 
# VSCP Helper library API - Helpers 

This part of the library describes the many helpers that are available to handle events, GUIDs, etc, etc.

\\ \\ 


# Misc helpers

##  readStringValue

`<code="c">`
long readStringValue( const char * pStrValue )
`</code>`

Convert a string to an integer value. The string can be expressed as a decimal  (10, 00001 ) or a hexadecimal value(0xff).

#####  pStrValue

String representation of value.

#####  Return value 

The converted number.


##### Example

`<code="c">`
long readValue = readStringValue("0x22");
`</code>`


## replaceBackslash

`<code="c">`
int replaceBackslash( const char *pStr )
`</code>`

Replace all backslashes ("\") in a string with forward slashes ("/").

##### pStr

Null terminated string to convert.

#####  Return value

VSCP_ERROR_SUCCESS on success.


\\ \\ 
----
\\ \\ 


## getTimeString

`<code="c">`
int getTimeString( char *buf, size_t buf_len, time_t *t )
`</code>`

Get GMT time (https://www.w3.org/Protocols/rfc2616/rfc2616-sec3.html#sec3.3). 

Example result:  Sun, "06 Nov 1994 08:49:37 GMT"

##### buf

Buffer that will get timestring after a successful call.

##### buf_len

Length of the buffer.

##### t

Pointer to an object of type time_t that contains a time value.
time_t is an alias of a fundamental arithmetic type capable of representing times as returned by function time.

#####  Return value

VSCP_ERROR_SUCCESS on success.


\\ \\ 
----
\\ \\ 

## getISOTimeString

`<code="c">`
int getISOTimeString( char *buf, size_t buf_len, time_t *t )
`</code>`

##### buf

Buffer that will get ISO timestring after a successful call.

Example result:  "2003-11-02T12:23:10Z"

##### buf_len

Length of the buffer.

##### t

Pointer to an object of type time_t that contains a time value.
time_t is an alias of a fundamental arithmetic type capable of representing times as returned by function time.

#####  Return value

VSCP_ERROR_SUCCESS on success.


\\ \\ 
----
\\ \\ 

# Event handling

## copyVSCPEvent

`<code="c">`
int copyVSCPEvent( vscpEvent *pEventTo, 
                              const vscpEvent *pEventFrom )
`</code>`

Copy VSCP event.

#####  pEventTo

VSCP event that will get the result.

#####  pEventFrom 

VSCP event that should be copied

#####  Return value

VSCP_ERROR_SUCCESS on success.


##### Example

`<code="c">`
vscpEvent *pEventFrom = new vscpEvent;
vscpEvent *pEventTo = new vscpEvent;
pEventFrom->head = 0;
pEventFrom->vscp_class = 10;
pEventFrom->vscp_type = 6;
pEventFrom->obid = 0;
pEventFrom->timestamp = 0;
memset( pEventFrom->GUID, 0, 16 );
pEventFrom->sizeData = 2;
pEventFrom->pdata = new unsigned char[2];
pEventFrom->pdata[ 0 ] = 0xAA;
pEventFrom->pdata[ 1 ] = 0x55;

if ( VSCP_ERROR_SUCCESS == copyVSCPEvent( pEventTo, pEventFrom ) ) {
    printf( "OK copyVSCPEvent %02X %02X \n", pEventTo->pdata[0], pEventTo->pdata[1] );
}
else {
    printf( "\aError: copyVSCPEvent\n");
}

// Free the events
deleteVSCPevent( pEventFrom );
deleteVSCPevent( pEventTo );
`</code>`



## writeVscpDataToString

`<code="c">`
int writeVscpDataToString( const vscpEvent *pEvent, 
                                       char *pstr, 
                                       size_t len,
                                       int bUseHtmlBreak )
`</code>`

Write VSCP data in readable form to a possibly multi line string.

#####  pEvent

The event that contains the data to be written

#####  bUseHtmlBreak 

Set to true (non zero) to use "`<br>`" instead of "\n" as linebreak in string. 

#####  Return value

VSCP_ERROR_SUCCESS is returned on success.


##### Example

`<code="c">`
char dataBuf[80];

if ( VSCP_ERROR_SUCCESS == writeVscpDataToString( pEvent, 
                                                            dataBuf, 
                                                            sizeof( dataBuf )-1,
                                                            0 ) ) {
    printf( "OK writeVscpDataToString \n%s \n", dataBuf );
}
else {
    printf( "\aError: writeVscpDataToString\n");
}
`</code>`

## writeVscpDataWithSizeToString

`<code="c">`
int writeVscpDataWithSizeToString( const unsigned char *pdata,
                                              const unsigned short. 
                                              char *pstr, 
                                              size_t len,
                                              int bUseHtmlBreak,
                                              int bBreak )
`</code>`

Write VSCP data in readable form to a possibly multi line string from a data array with size.

#####  pData

Pointer to VSCP data array.

##### size

Number of bytes in data array.

##### pstr

Pointer to string buffer that will receive string.

##### len

Size of string receive buffer.

#####  bUseHtmlBreak 

Set to true (non zero) to use "`<br>`" instead of "\n" as linebreak in string. 

##### bBreak 

Set to true (non zero) to add the break character.

#####  Return value

VSCP_ERROR_SUCCESS is returned on success.


## setVscpDataFromString

`<code="c">`
int setVscpDataFromString( vscpEvent *pEvent, 
                                   const char *pstr )
`</code>`

Set data in VSCP event from a string.

#####  pEvent

VSCP Event which will have its data set.

#####  pstr 

Pointer to null terminated string that contains data on comma separated form.
 
#####  Return value 

VSCP_ERROR_SUCCESS is returned on success.



##### Example

`<code="c">`
vscpEvent e;

if ( VSCP_ERROR_SUCCESS == 
    setVscpDataFromString( e,
                           "1,2,3,4,5,6,0x07,0x55,3,4,0xaa,0xff,0xff" ) ) {
        printf( "OK setVscpDataFromString size=%d Data = \n", e.sizeData );
        for ( int i=0; i<e.sizeData; i++ ) {
            printf("%d ", e.data[i] );
        }
        printf("\n");
}
else {
   printf( "\aError: setVscpDataFromString\n");
}
`</code>`




## writeVscpEventToString

`<code="c">`
int writeVscpEventToString( const vscpEvent *pEvent, char *pstr, size_t len )
`</code>`

Write VSCP event content to a string.

#####  pEvent

The VSCP event which will be written to the string buffer.

#####  pstr

Pointer to string buffer that will receive result.

##### len

Size of buffer.

#####  Return value

VSCP_ERROR_SUCCESS is returned on success.



##### Example

`<code="c">`
char eventBuf[128];
if ( VSCP_ERROR_SUCCESS == writeVscpEventToString( pEvent, eventBuf, sizeof( eventBuf )-1 ) ) {
    printf( "OK writeVscpEventToString Event = %s\n", eventBuf );    
}
else {
    printf( "\aError: writeVscpEventToString\n");
}
`</code>`



## writeVscpEventExToString

`<code="c">`
int writeVscpEventExToString( const vscpEventEx *pEvent, char *pstr, size_t len )
`</code>`

Write VSCP event ex content to a string.

#####  pEvent

The VSCP event which will be written to the string buffer.

#####  pstr

Pointer to string buffer that will receive result.

##### len

Size of buffer.

#####  Return value

VSCP_ERROR_SUCCESS is returned on success.


##### Example

`<code="c">`
char eventBuf[128];
if ( VSCP_ERROR_SUCCESS == writeVscpEventExToString( &ex, 
                                           eventBuf, 
                                           sizeof( eventBuf )-1 ) ) {
    printf( "OK writeVscpEventExToString Event = %s\n", eventBuf );    
}
else {
    printf( "\aError: writeVscpEventExToString\n");
}
`</code>`


##  setVscpEventFromString

`<code="c">`
int setVscpEventFromString( vscpEvent *pEvent, const char *pstr )
`</code>`

Set VSCP event from a string.

#####  pEvent

The VSCP event which will be written to.

#####  pstr

Pointer to string buffer that contain an event in string form 

    head,class,type,obid,timestamp,GUID,data1,data2,data3....

#####  Return value

VSCP_ERROR_SUCCESS is returned on success.


##### Example

`<code="c">`
vscpEvent *pEventString1 = new vscpEvent;
pEventString1->pdata = NULL;

if ( VSCP_ERROR_SUCCESS == setVscpEventFromString( pEventString1,                
       "0,10,6,0,0,FF:FF:FF:FF:FF:FF:FF:00:00:00:00:7F:00:01:01:FD,0x8A,0x00,0x1E" ) ) {
    printf( "OK setVscpEventFromString class=%d Type=%d\n", 
                   pEventString1->vscp_class, pEventString1->vscp_type );
}
else {
    printf( "\aError: setVscpEventFromString\n");
}

// Free the events
deleteVSCPevent( pEventString1 );
`</code>`

## setVscpEventExFromString

`<code="c">`
int setVscpEventExFromString( vscpEventEx *pEvent, const char *pstr )
`</code>`

Set VSCP event ex from a string.

#####  pEvent

The VSCP event ex which will be written to.

#####  pstr

Pointer to string buffer that contain an event in string form 

    head,class,type,obid,timestamp,GUID,data1,data2,data3....

#####  Return value

VSCP_ERROR_SUCCESS is returned on success.


##### Example

`<code="c">`
vscpEventEx ex6;
if ( VSCP_ERROR_SUCCESS == setVscpEventExFromString( &ex6,  
      "0,10,6,0,0,FF:FF:FF:FF:FF:FF:FF:00:00:00:00:7F:00:01:01:FD,0x8A,0x00,0x1E" ) ) 
    printf( "OK setVscpEventExFromString class=%d Type=%d\n", 
                   ex6.vscp_class, ex6.vscp_type );
}
else {
    printf( "\aError: setVscpEventExFromString\n");
}
`</code>`





## getVscpPriority

`<code="c">`
unsigned char getVscpPriority( const vscpEvent *pEvent )
`</code>`

Extract the event priority from a VSCP event. Priority is defined as a value between 0-7 where 0 is the highest priority.

#####  pEvent

VSCP event.

#####  Return value

Priority.



##### Example

`<code="c">`
pEvent = new vscpEvent;
pEvent->head = 0;
pEvent->vscp_class = 10;
pEvent->vscp_type = 6;
pEvent->obid = 0;
pEvent->timestamp = 0;
memset( pEvent->GUID, 0, 16 );
pEvent->sizeData = 3;
pEvent->pdata = new unsigned char[3];
pEvent->pdata[ 0 ] = 138;
pEvent->pdata[ 1 ] = 0;
pEvent->pdata[ 2 ] = 30;
    
unsigned char eventPriority;
if ( 0 == ( eventPriority = getVscpPriority( pEvent ) ) ) {
    printf("Event priority = %d\n", eventPriority );
}
else {
    printf("\aError: Event priority = %d\n", eventPriority );
}

// Free the event
deleteVSCPevent( pEvent );
`</code>`


## getVscpPriorityEx

`<code="c">`
unsigned char getVscpPriorityEx( const vscpEventEx *pEvent )
`</code>`

Extract the event priority from a VSCP event. Priority is defined as a value between 0-7 where 0 is the highest priority.

#####  pEvent

VSCP event.

#####  Return value

Priority.



##### Example

`<code="c">`
vscpEventEx ex3;
ex3.head = 0;
ex3.vscp_class = 10;
ex3.vscp_type = 6;
ex3.obid = 0;
ex3.timestamp = 0;
memset( ex3.GUID, 0, 16 );
ex3.sizeData = 3;
ex3.data[ 0 ] = 138;
ex3.data[ 1 ] = 0;
ex3.data[ 2 ] = 30;
    
unsigned char eventPriority;
if ( 0 == ( eventPriority = getVscpPriorityEx( &ex3 ) ) ) {
    printf("EventEx priority = %d\n", eventPriority );
}
else {
    printf("\aError: EventEx priority = %d\n", eventPriority );
}
`</code>`
## setVscpPriority

`<code="c">`
void setVscpPriority( vscpEvent *pEvent, unsigned char priority )
`</code>`

Set Event priority. Priority is defined as a value between 0-7 where 0 is the highest priority.

#####  pEvent

VSCP event.

#####   priority

Priority to set.


##### Example

`<code="c">`
pEvent = new vscpEvent;
pEvent->head = 0;
pEvent->vscp_class = 10;
pEvent->vscp_type = 6;
pEvent->obid = 0;
pEvent->timestamp = 0;
memset( pEvent->GUID, 0, 16 );
pEvent->sizeData = 3;
pEvent->pdata = new unsigned char[3];
pEvent->pdata[ 0 ] = 138;
pEvent->pdata[ 1 ] = 0;
pEvent->pdata[ 2 ] = 30;

unsigned char eventPriority;
setVscpPriority( pEvent, VSCP_PRIORITY_NORMAL );
if ( VSCP_PRIORITY_NORMAL == ( eventPriority = getVscpPriority( pEvent ) ) ) {
    printf("Event priority = %d\n", eventPriority );
}
else {
    printf("\aError: Set Event priority = %d\n", eventPriority );
}

// Free the event
deleteVSCPevent( pEvent );
`</code>`


## setVscpPriorityEx

`<code="c">`
unsigned char eventPriority;
void setVscpPriorityEx( vscpEventEx *pEvent, unsigned char priority )
`</code>`

Set Event priority. Priority is defined as a value between 0-7 where 0 is the highest priority.

#####  pEvent

VSCP ex event.

#####   priority

Priority to set.


##### Example

`<code="c">`
vscpEventEx ex3;
ex3.head = 0;
ex3.vscp_class = 10;
ex3.vscp_type = 6;
ex3.obid = 0;
ex3.timestamp = 0;
memset( ex3.GUID, 0, 16 );
ex3.sizeData = 3;
ex3.data[ 0 ] = 138;
ex3.data[ 1 ] = 0;
ex3.data[ 2 ] = 30;
    
unsigned char eventPriority;
setVscpPriorityEx( &ex3, VSCP_PRIORITY_LOW );
if ( VSCP_PRIORITY_LOW == ( eventPriority = getVscpPriorityEx( &ex3 ) ) ) {
    printf("Event priority = %d\n", eventPriority );
}
else {
    printf("\aError: Set EventEx priority = %d\n", eventPriority );
}
`</code>`

## getVSCPheadFromCANALid

`<code="c">`
unsigned unsigned char getVSCPheadFromCANALid( const unsigned long id ))
`</code>`

Get the VSCP head from a CANAL message id.  The VSCP head is defined  as shown in the [vscp.h header file](https///github.com/grodansparadis/vscp_software/blob/master/src/vscp/common/vscp.h).

#####  id

Extended 29-bit CAN id to get head from.

#####  Return value

VSCP head byte.


##### Example

`<code="c">`
unsigned char vscphead;
unsigned long canalid = 0x0c0a0601;
vscphead = getVSCPheadFromCANALid( canalid );
if ( 96 == vscphead ) {  // Priority == 3 Not hard coded
    printf("VSCP head = %d\n", vscphead );
}
else {
   printf("\aError: getVSCPheadFromCANALid = %d\n", vscphead );
}
`</code>`



## getVSCPclassFromCANALid

`<code="c">`
unsigned short getVSCPclassFromCANALid( unsigned long id )
`</code>`

Get the VSCP class from a CANAL message id.

#####  id

Extended 29-bit CANAL id to get head from.

#####  Return value

VSCP class.


##### Example

`<code="c">`
unsigned long canalid = 0x0c0a0601;
unsigned short can_vscpclass = getVSCPclassFromCANALid( canalid );
if ( 10 == can_vscpclass ) {
    printf("VSCP Class = %d\n", can_vscpclass );
}
else {
    printf("\aError: getVSCPclassFromCANAALid = %d\n", can_vscpclass );
}
`</code>`



## getVSCPtypeFromCANALid

`<code="c">`
unsigned short getVSCPtypeFromCANANALid( const unsigned long id )
`</code>`

Get the VSCP type from a a CANAL message id (CAN id).

#####  id

Extended 29-bit CANAL id to get head from.

#####  Return value

VSCP type.


##### Example

`<code="c">`
unsigned long cananalid = 0x0c0a0601;

unsigned short canal_vscptype = getVSCPtypeFromCANALid( canalid );
if ( 6 == canal_vscptype ) {
    printf("VSCP Type = %d\n", canal_vscptype );
}
else {
    printf("\aError: getVSCPtypeFromCANALid = %d\n", canal_vscptype );
}
`</code>`



## getVSCPnicknameFromCANALid

`<code="c">`
unsigned short getVSCPnicknameFromCANALid( unsigned long id )
`</code>`

Get the VSCP 8-bit nickname from a a CANAL message id.

#####  id

Extended 29-bit CAN id to get head from.

#####  Return value

VSCP 8-bit nickname.


##### Example

`<code="c">`
unsigned long canalid = 0x0c0a0601;
unsigned char canal_nickname = getVSCPnicknameFromCANALid( canalid );
if ( 1 == canal_nickname ) {
    printf("VSCP Type = %d\n", canal_vscptype );
}
else {
    printf("\aError: getVSCPnicknameFromCANALid = %d\n", canal_nickname );
}
`</code>`



## getCANALidFromVSCPdata

`<code="c">`
unsigned long getCANALidFromVSCPdata( unsigned char priority, 
                                                unsigned short vscp_class, 
                                                unsigned short vscp_type )
`</code>`

Construct a CANAL id (CAN id ) from a VSCP event.

#####  priority

VSCP event priority (0-7).

#####  vscp_class

VSCP Class.

#####  vscp_type

VSCP type.

#####  Return value

CANAL (CAN) id.


##### Example

`<code="c">`
unsigned long constr_canal_id2 = getCANALidFromVSCPdata( 3, 10, 6 ); 
if ( 0x0c0a0600 == constr_canal_id2 ) {
    printf("Nickname = %08X\n", constr_canal_id2 );
}
else {
   printf("\aError: getVSCPnicknameFromCANALid = %08X\n", constr_canal_id2 );
} 
`</code>`


## getCANALidFromVSCPevent

`<code="c">`
unsigned long getCANALidFromVSCPevent( const vscpEvent *pEvent )
`</code>`

Get CANAL id (CAN id) from VSCP event.

#####  pEvent

VSCP event.

#####  Return value

CANAL (CAN) id.


##### Example

`<code="c">`
constr_canal_id2 = getCANALidFromVSCPevent( pEvent ); 
if ( 0x0c0a0600 == constr_canal_id2 ) {
    printf("Nickname = %08X\n", constr_canal_id2 );
}
else {
    printf("\aError: getCANALidFromVSCPevent = %08X\n", constr_canal_id2 );
}  
`</code>`

## getCANALidFromVSCPeventEx

`<code="c">`
unsigned long getCANALidFromVSCPeventEx( const vscpEventEx *pEvent )
`</code>`

Get CANAL id (CAN id) from VSCP event.

#####  pEvent

VSCP event.

#####  Return value

CANAL (CAN) id.


##### Example

`<code="c">`
constr_canal_id2 = getCANALidFromVSCPeventEx( &ex ); 
if ( 0x0c0a0600 == constr_canal_id2 ) {
    printf("Nickname = %08X\n", constr_canal_id2 );
}
else {
    printf("\aError: getCANALidFromVSCPeventEx = %08X\n", constr_canal_id2 );
}  
`</code>`
## calc_crc_Event

`<code="c">`
short calc_crc_Event ( vscpEvent *pEvent, int bSet )
`</code>`

Calculate VSCP CRC and optionally set it.

##### pEvent==  

VSCP event.

##### bSet==  

If true (non zero) write the CRC into the event structure crc member.

#####  Return value

VSCP CRC.

##### Example

`<code="c">`
unsigned short crc = calc_crc_Event( pEvent, false );
printf("CRC = %04X\n", crc );
`</code>`

## calc_crc_EventEx

`<code="c">`
short calc_crc_EventEx( vscpEvent *pEvent, int bSet )
`</code>`

Calculate VSCP CRC and optionally set it.

##### pEvent==  

VSCP event.

##### bSet==  

If true (non zero) write the CRC into the event structure crc member.

#####  Return value

VSCP CRC.

##### Example

`<code="c">`
unsigned short crc = calc_crc_EventEx( pEvent, false );
printf("CRC = %04X\n", crc );
`</code>`

## convertVSCPtoEx

`<code="c">`
int convertVSCPtoEx( vscpEventEx *pEventEx, 
                              const vscpEvent *pEvent )
`</code>`

Convert VSCP standard event form to ex form.

##### pEventEx==  

VSCP event ex to convert to

##### pEvent==  

VSCP event to convert to.

#####  Return value

VSCP_ERROR_SUCCESS on success.


##### Example

`<code="c">`
vscpEventEx ex4;
if ( VSCP_ERROR_SUCCESS != convertVSCPtoEx( &ex4, pEvent ) ) {
    printf( "\aError: getGuidFromStringToArray\n");
}
`</code>`



## convertVSCPfromEx

`<code="c">`
int convertVSCPfromEx( vscpEvent *pEvent, 
                                        const vscpEventEx *pEventEx )
`</code>`

Convert VSCP ex. event form to standard form.

#####  pEvent

VSCP event to convert to.

#####  pEventEx

VSCP event ex to convert from.

#####  Return value

VSCP_ERROR_SUCCESS on success.

##### Example

`<code="c">`
if ( VSCP_ERROR_SUCCESS != convertVSCPfromEx( pEvent, &ex4 ) ) {
    printf( "\aError: convertVSCPfromEx\n");
}
`</code>`


## newVSCPevent

`<code="c">`
bool newVSCPevent( vscpEvent **ppEvent )
`</code>`

Creates a new VSCP event.

#### pEvent

Pointer to pointer to a VSCP event.

#### Return value

Return VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure.


#### Example

`<code="c">`
vscpEvent *pEvent;
newVSCPevent( &pEvent );
`</code>`

## deleteVSCPevent

`<code="c">`
void deleteVSCPevent( vscpEvent *pEvent )
`</code>`

Delete VSCP event.

#####  pEvent

VSCP event.


##### Example

`<code="c">`
deleteVSCPevent( pEvent );
`</code>`


## deleteVSCPevent_v2

`<code="c">`
void deleteVSCPevent_v2( vscpEvent **ppEvent )
`</code>`

Delete VSCP event and set to NULL.

#####  pEvent

Pointer to pointer to a valid VSCP event.


##### Example

`<code="c">`
deleteVSCPevent_v2( pEvent );
`</code>`
## deleteVSCPeventEx

`<code="c">`
void deleteVSCPeventEx( vscpEventEx *pEventEx )
`</code>`

Delete VSCP event ex.

#####  pEventEx

VSCP event ex.


##### Example

`<code="c">`
deleteVSCPeventEx( &ex )
`</code>`


## convertCanalToEvent

`<code="c">`
int convertCanalToEvent( vscpEvent *pvscpEvent,
                                    const canalMsg *pcanalMsg,
                                    unsigned char *pGUID )
`</code>`

Convert CANAL message to VSCP event.

#####  pvscpEvent

VSCP event that will hold the conversion result.

#####  pcanalMsg

CANAL message that should be converted.

#####  pGUID

GUID for event.

#####  Return value

VSCP_ERROR_SUCCESS on success.

##### Example

`<code="c">`
canalMsg canalMsg;
canalMsg.id = 0x0c0a0601;
canalMsg.sizeData = 3;
canalMsg.data[0] = 138;
canalMsg.data[1] = 0;
canalMsg.data[2] = 30;
if ( VSCP_ERROR_SUCCESS == convertCanalToEvent( pEvent,
                                                          &canalMsg,
                                                          GUID2 ) ) {
    printf( "OK convertCanalToEvent VSCP class=%d Type=%d\n", 
                   pEvent->vscp_class, pEvent->vscp_type );
}
else {
    printf( "\aError: convertCanalToEvent\n");
}
`</code>`


## convertCanalToEventEx

`<code="c">`
int convertCanalToEventEx( vscpEvent *pvscpEvent, 
                                      const canalMsg *pcanalMsg, 
                                      unsigned char *pGUID )
`</code>`

Convert CANAL message to VSCP ex event.

#####  pvscpEvent

VSCP event ex that will hold the conversion result.

#####  pcanalMsg

CANAL message that should be converted.

#####  pGUID

GUID for event.

#####  Return value

VSCP_ERROR_SUCCESS on success.


##### Example

`<code="c">`
canalMsg canalMsg;
canalMsg.id = 0x0c0a0601;
canalMsg.sizeData = 3;
canalMsg.data[0] = 138;
canalMsg.data[1] = 0;
canalMsg.data[2] = 30;

vscpEventEx ex5;
if ( VSCP_ERROR_SUCCESS == convertCanalToEventEx( &ex5,
                                                            &canalMsg,
                                                            GUID2 ) ) {
    printf( "OK convertCanalToEventEx VSCP class=%d Type=%d\n",
                       ex5.vscp_class, ex5.vscp_type );
}
else {
    printf( "\aError: convertCanalToEvent\n");
}
`</code>`
## convertEventToCanal

`<code="c">`
bool convertEventToCanal( canalMsg *pcanalMsg, 
                                  const vscpEvent *pvscpEvent )
`</code>`
Convert VSCP event to CANAL message.

#####  pcanalMsg

CANAL message that will hold result.

#####  pvscpEvent

VSCP event that will be converted.

#####  Return value

VSCP_ERROR_SUCCESS on succes.


##### Example

`<code="c">`
if ( VSCP_ERROR_SUCCESS == convertEventToCanal( &canalMsg, pEvent ) ) {
    printf( "OK convertEventToCanal id=%08X\n", canalMsg.id );
}
else {
    printf( "\aError: convertEventToCanal\n");
}
`</code>`


## convertEventExToCanal

`<code="c">`
bool convertEventExToCanal( canalMsg *pcanalMsg, 
                                       const vscpEventEx *pvscpEvent )
`</code>`
Convert VSCP event ex to CANAL message.

#####  pcanalMsg

CANAL message that will hold result.

#####  pvscpEvent

VSCP ex event that will be converted.

#####  Return value

VSCP_ERROR_SUCCESS on succes.


##### Example

`<code="c">`
if ( VSCP_ERROR_SUCCESS == convertEventExToCanal( &canalMsg, &ex5 ) ) {
    printf( "OK convertEventExToCanal id=%08X\n", canalMsg.id );
}
else {
    printf( "\aError: convertEventExToCanal\n");
}
`</code>`




## vscphlp makeTimeStamp

`<code="c">`
unsigned long makeTimeStamp( void )
`</code>`

Get new VSCP timestamp.

#####  Return value

Timestamp in microseconds.

##### Example

`<code="c">`
printf( "makeTimeStamp  %04X\n", makeTimeStamp() );
`</code>`

\\ \\ 
----
\\ \\  

## setEventDateTimeBlockToNow

`<code="c">`
int setEventDateTimeBlockToNow( vscpEvent *pEvent )
`</code>`

Get date/time block for an event.

#####  Return value

VSCP_ERROR_SUCCESS is returned on success.

##### Example

`<code="c">`
vscpEvent *pEvent;
setEventDateTimeBlockToNow( pEvent );
`</code>`

\\ \\ 
----
\\ \\  

## setEventExDateTimeBlockToNow

`<code="c">`
int setEventExDateTimeBlockToNow( vscpEventEx *pEventEx )
`</code>`

Get date/time block for an ex event.

#####  Return value

VSCP_ERROR_SUCCESS is returned on success.

##### Example

`<code="c">`
vscpEventEx *pEventEx;
setEventExDateTimeBlockToNow( pEventEx );
`</code>`

\\ \\ 
----
\\ \\  



## getDateStringFromEvent

`<code="c">`
int getDateStringFromEvent( char *buf, size_t buf_len, vscpEvent *pEvent )
`</code>`

##### buf

Buffer that will get datestring from event

Example result:  "2003-11-02T12:23:10Z"

##### buf_len

Length of the buffer.

##### pEvent

Event to get datestring from.

#####  Return value

VSCP_ERROR_SUCCESS on success.


\\ \\ 
----
\\ \\ 



## getDateStringFromEventEx

`<code="c">`
int getDateStringFromEventEx( char *buf, size_t buf_len, vscpEventEx *pEventEx )
`</code>`

##### buf

Buffer that will get datestring from event ex.

Example result:  "2003-11-02T12:23:10Z"

##### buf_len

Length of the buffer.

##### pEventEx

Event to get datestring from.

#####  Return value

VSCP_ERROR_SUCCESS on success.


\\ \\ 
----
\\ \\ 

# Filter handling

## clearVSCPFilter

`<code="c">`
void clearVSCPFilter( vscpEventFilter *pFilter )
`</code>`

Clear VSCP filter.

#####  pFilter

Pointer to VSCP filter structure.

##### Example

`<code="c">`
clearVSCPFilter( pFilter )
`</code>`


## copyVSCPFilter

`<code="c">`
void copyVSCPFilter( vscpEventFilter *pToFilter, const vscpEventFilter *pFromFilter )
`</code>`

Copy VSCP filter from one to another.

#####  pToFilter

Pointer to VSCP filter structure that will receive data.

#####  pFromFilter

Pointer to VSCP filter structure that data will be copied from.

##### Example

`<code="c">`
clearVSCPFilter( pFilter )
`</code>`

## readFilterFromString

`<code="c">`
int readFilterFromString( vscpEventFilter *pFilter, 
                                   char *strFilter )
`</code>`

Read a filter from a string. If strFilter is an empty string all elements in filter will be set to zero. Arguments is
        priority,class,type,GUID 
and all is optional but if given must be given in order.

#####  pFilter

Filter structure to write filter to. 

##### strFilter==  

Filter in string form 

   filter-priority, filter-class, filter-type, filter-GUID

as in this example

    1,0x0000,0x0006,ff:ff:ff:ff:ff:ff:ff:01:00:00:00:00:00:00:00:00
    
and all is optional but if given must be given in order. This means

    1,0x0000,0x0006

for example is OK setting GUID to all zeros.
    
##### Return value 

VSCP_ERROR_SUCCESS on success.

##### Example

`<code="c">`
if ( VSCP_ERROR_SUCCESS != readFilterFromString( &filter, 
                "1,0x0000,0x0006,ff:ff:ff:ff:ff:ff:ff:01:00:00:00:00:00:00:00:00" ) ) {
    printf( "\aError: readFilterFromString\n");   
}
`</code>`

## writeFilterToString

`<code="c">`
    bool vscp_writeFilterToString(vscpEventFilter *pFilter, char * strFilter);
`</code>`

Write a filter on comma separated form to a string (//priority,class,type,GUID//).

#####  pFilter

Filter structure to write filter to. 

##### strFilter== 

Will get the filter in string form *priority,class,type,GUID*. Must be at least 65 bytes.

    filter-priority, filter-class, filter-type, filter-GUID

##### Return value 

VSCP_ERROR_SUCCESS on success.

##### Example

`<code="c">`
if ( VSCP_ERROR_SUCCESS != writeFilterToString( &filter, str ) ) {
    printf( "\aError: writeFilterToString\n");   
}
`</code>`
## readMaskFromString

`<code="c">`
int readMaskFromString( vscpEventFilter *pFilter, 
                                   const char * strMask )
`</code>`

Read a mask from a string. If strMask is an empty string elements in mask will be set to zero.

#####  pFilter

Filter structure to write mask to. 

#####  strMask

Mask in string form 

    mask-priority, mask-class, mask-type, mask-GUID

as in this example

    1,0x00ff,0x00ff,ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff  

and all is optional but if given must be given in order.This means that

    1,0x00ff

will be interpreted as

    1,0x00ff,0x0000,00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00  

#####  Return value

VSCP_ERROR_SUCCESS on success.


##### Example

`<code="c">`
if ( VSCP_ERROR_SUCCESS != readMaskFromString( &filter, 
                "1,0x0000,0x0006,ff:ff:ff:ff:ff:ff:ff:01:00:00:00:00:00:00:00:00" ) ) {
    printf( "\aError: readMaskFromString\n");   
}
`</code>`

## writeMaskToString

`<code="c">`
int writeMaskToString( vscpEventFilter *pFilter, 
                                   char * strMask )
`</code>`

Write the mask in comma separated form to  a string. If strMask is an empty string elements in mask will be set to zero.

#####  pFilter

Filter structure to write mask from. 

#####  strMask

String that will get mask in comma separated string form. Must be at least 65 bytes.

    mask-priority, mask-class, mask-type, mask-GUID

#####  Return value

VSCP_ERROR_SUCCESS on success.


##### Example

`<code="c">`
if ( VSCP_ERROR_SUCCESS != writeMaskToString( &filter, 
                "1,0x0000,0x0006,ff:ff:ff:ff:ff:ff:ff:01:00:00:00:00:00:00:00:00" ) ) {
    printf( "\aError: writeMaskToString\n");   
}
`</code>`


## doLevel2Filter 

`<code="c">`
int doLevel2Filter( const vscpEvent *pEvent, 
                             const vscpEventFilter *pFilter )
`</code>`
Check VSCP filter condition.

#####  Return value

Return true (non-zero) if the event is accepted by the filter.


##### Example

`<code="c">`
if ( doLevel2Filter( pEvent, &filter ) ) {
    printf( "Event pass:  doLevel2Filter\n");
}
else {
   printf( "Event does NOT pass:  doLevel2Filter\n");
}
`</code>`


\\ \\ 
----
\\ \\  


# GUID Handling


## getGuidFromString

`<code="c">`
int getGuidFromString( vscpEvent *pEvent, const char * pGUID )
`</code>`

Write GUID into VSCP event from a string.

##### pEvent==  

VSCP event.

##### pGUID==  

Pointer to GUID in string form.

#####  Return value

VSCP_ERROR_SUCCESS on success.


##### Example

`<code="c">`
char strguid[64], strguid2[64];

if ( VSCP_ERROR_SUCCESS == getGuidFromString( pEvent, strguid ) )  { 
    writeGuidToString( pEvent, strguid2, sizeof( strguid2 )-1 );
    printf( "GUID=%s\n", strguid2 );
}
else {
    printf( "\aError: writeGuidArrayToString\n");
}
`</code>`

## getGuidFromStringEx

`<code="c">`
int getGuidFromStringEx( vscpEvent *pEvent, const char * pGUID )
`</code>`

Write GUID into VSCP event ex from a string.

##### pEvent==  

VSCP event ex.

##### pGUID==  

Pointer to GUID in string form.

#####  Return value

VSCP_ERROR_SUCCESS on success.


##### Example

`<code="c">`
char strguid[64], strguid2[64];

if ( VSCP_ERROR_SUCCESS == getGuidFromStringEx( &ex3, strguid ) ) {        
    writeGuidToStringEx( &ex3, strguid2, sizeof( strguid2 )-1 );
    printf( "GUID=%s\n", strguid2 );
}
else {
    printf( "\aError: writeGuidArrayToString\n");
}
`</code>`
## getGuidFromStringToArray

`<code="c">`
int getGuidFromStringToArray( uint8_t *pGUID, const char * pStr )
`</code>`

Write GUID from string into array.

##### pGUID==  

Pointer to VSCP GUID array to fill.

##### pStr==  

Pointer to GUID in string form. 

#####  Return value

VSCP_ERROR_SUCCESS on success.


##### Example

`<code="c">`
if ( VSCP_ERROR_SUCCESS == getGuidFromStringToArray( GUID2, strguid ) ) {
    writeGuidArrayToString( GUID2, strguid2, sizeof( strguid2 )-1 );
    printf( "GUID  after reverse = %s\n", strguid2 );
}
else {
    printf( "\aError: getGuidFromStringToArray\n");
}
`</code>`


## writeGuidToString

`<code="c">`
int writeGuidToString( const vscpEvent *pEvent, char *pStr, size_t len )
`</code>`

Write GUID from VSCP event to string.

##### pEvent==  

VSCP event.

##### pStr==  

Pointer to GUID in string form. 

##### len

Size of string buffer.

#####  Return value

VSCP_ERROR_SUCCESS on success.


##### Example

`<code="c">`
if ( VSCP_ERROR_SUCCESS == getGuidFromString( pEvent, strguid ) ) {
   writeGuidToString( pEvent, strguid2, sizeof( strguid2 )-1 );
   printf( "GUID=%s\n", strguid2 );
}
else {
    printf( "\aError: writeGuidArrayToString\n");
}
`</code>`

## writeGuidToStringEx

`<code="c">`
int writeGuidToStringEc( const vscpEventEx *pEvent, char *pStr, size_t len )
`</code>`

Write GUID from VSCP event to string.

##### pEvent==  

VSCP event.

##### pStr==  

Pointer to GUID in string form. 

##### len

Size of string buffer.

#####  Return value

VSCP_ERROR_SUCCESS on success.


##### Example

`<code="c">`
if ( VSCP_ERROR_SUCCESS == getGuidFromStringEx( &ex3, strguid ) ) {
    writeGuidToStringEx( &ex3, strguid2, sizeof( strguid2 )-1 );
    printf( "GUID=%s\n", strguid2 );
}
else {
    printf( "\aError: writeGuidArrayToString\n");
}
`</code>`
## writeGuidToString4Rows

`<code="c">`
int writeGuidToString4Rows( const vscpEvent *pEvent, 
                                      char *strGUID,
                                      size_t len )
`</code>`

Write GUID from VSCP event to string with four bytes on each row separated by “\r\n”. 

##### pEvent==  

VSCP event.

##### strGUID==  

String that get formatted GUID.

##### len

Size of string buffer.

#####  Return value

VSCP_ERROR_SUCCESS on success.


##### Example

`<code="c">`
if ( VSCP_ERROR_SUCCESS == writeGuidToString4Rows( pEvent, strguid2, sizeof( strguid2 )-1 ) ) {
    printf( "GUID\n%s\n", strguid2 );
}
else {
    printf( "Error: writeGuidArrayToString\n");
}
`</code>`

## writeGuidToString4RowsEx

`<code="c">`
int writeGuidToString4RowsEx( const vscpEventEx *pEvent, 
                                          char *strGUID,
                                          size_t len )
`</code>`

Write GUID from VSCP event to string with four bytes on each row separated by “\r\n”. 

##### pEvent==  

VSCP event.

##### strGUID==  

String that get formatted GUID.

##### len

Size of string buffer.

#####  Return value

VSCP_ERROR_SUCCESS on success.


##### Example

`<code="c">`
if ( VSCP_ERROR_SUCCESS == writeGuidToString4RowsEx( &ex3, strguid2, sizeof( strguid2 )-1 ) ) {
    printf( "GUID\n%s\n", strguid2 );
}
else {
    printf( "Error: writeGuidArrayToString\n");
}
`</code>`
## writeGuidArrayToString

`<code="c">`
int writeGuidArrayToString( const unsigned char * pGUID, 
                                     char *strGUID,
                                     size_t len )
`</code>`
Write GUID from byte array to string.

#####  pGUID

A 16 byte GUID array.

#####  strGUID

Pointer to buffer that can hold the GUID in string form.

##### len

Size of string buffer. 

#####  Return value

VSCP_ERROR_SUCCESS on success.


##### Example

`<code="c">`
if ( VSCP_ERROR_SUCCESS == writeGuidArrayToString( GUID2, strguid2, sizeof( strguid2 )-1 ) ) {
    printf( "GUID=%s\n", strguid2 );
}
else {
    printf( "Error: writeGuidArrayToString\n");
}
`</code>`


## isGUIDEmpty

`<code="c">`
int isGUIDEmpty( unsigned char *pGUID )
`</code>`

Check if GUID is empty (all nulls).

#####  pGUID

xxx

#####  Return value

True (non-zero) if GUID are empty.


##### Example

`<code="c">`
unsigned char emptyGUID[16];
memset( emptyGUID,0, 16 );
if ( isGUIDEmpty( emptyGUID ) ) {
    printf( "isGUIDEmpty  - GUID is detected as empty as it should be\n" );    
}
else {
    printf( "\aError: isGUIDEmpty\n");
}

if ( isGUIDEmpty( GUID2 ) ) {
    printf( "\aError: isGUIDEmpty\n");    
}
else {
    printf( "isGUIDEmpty  - GUID is detected as NOT empty as it should be\n" );
}
`</code>`


## isSameGUID

`<code="c">`
int isSameGUID( const unsigned char *pGUID1, 
                         const unsigned char *pGUID2 )
`</code>`

Check if two GUID's is equal to each other.

#####  pGUID1

GUID1 to compare.

##### pGUID2

GUID2 to compare.
 
#####  Return value 

True (non-zero) if GUIDs are the same.

##### Example

`<code="c">`
if ( isSameGUID( emptyGUID, GUID2) ) {
    printf( "\aError: isSameGUID\n");
}
else {
    printf( "isSameGUID  - Correct, GUIDs are not the same.\n" );
}
`</code>`


##  reverseGUID

`<code="c">`
int reverseGUID(unsigned char *pGUID)
`</code>`

Reverse a GUID array.

#####  pGUID1

GUID array to be reversed.
 
#####  Return value 

Return VSCP_ERROR_SUCCESS on success.

##### Example

`<code="c">`
writeGuidArrayToString( GUID2, strguid2, sizeof( strguid2 )-1 );
printf( "GUID before reverse = %s\n", strguid2 );
if ( VSCP_ERROR_SUCCESS == reverseGUID( GUID2 ) ) {
    writeGuidArrayToString( GUID2, strguid2, sizeof( strguid2 )-1 );
    printf( "GUID  after reverse = %s\n", strguid2 );
}
else {
    printf( "\aError: reverseGUID\n");
}
`</code>`
##  calcCRC4GUIDArray

`<code="c">`
unsigned char calcCRC4GUIDArray( unsigned char *pguid )
`</code>`

Calculate 8-bit crc for a GUID array.

#####  pguid

Array of sixteen bytes containing GUID on MSB->LSB order.

 
#####  Return value 

8-bit CRC for GUID.

##### Example

`<code="c">`
// Calculate CRC for GID array
unsigned char GUID2[16];
memset( GUID2, 0, 16 );
for ( int i=0;i<16; i++ ) {
    GUID2[i] = i;
}
unsigned char crc8 = calcCRC4GUIDArray( GUID2 );
printf("CRC = %02X\n", crc8 );
`</code>`

##  calcCRC4GUIDString

`<code="c">`
unsigned char calcCRC4GUIDString( unsigned char *strguid)
`</code>`

Calculate 8-bit crc for a GUID string.

##### strguid== 

String containing GUID on standard string form.

 
#####  Return value 

8-bit CRC for GUID.

##### Example

`<code="c">`
// Calculate GUID for GUID string
char strguid[64];
strcpy( strguid, "FF:FF:FF:FF:FF:FF:FF:00:00:00:00:7F:00:01:01:FD" );
crc8 = calcCRC4GUIDString( strguid);
printf("CRC = %02X\n", crc8 )
`</code>`




\\ \\ 
----
\\ \\  


# Measurement helpers

##  getMeasurementDataCoding

`<code="c">`
unsigned char getMeasurementDataCoding( const vscpEvent *pEvent )
`</code>`

Get the [measurement data coding byte](https://www.vscp.org/docs/vscpspec/doku.php?id=data_coding) from an event. The measurement data coding byte specifies how the data in the event should be interpreted.

##### pEvent

Event that the data coding is fetched from.

##### Return value

Data coding

##### Example

`<code="c">`
pEvent = new vscpEvent;
pEvent->head = 0;
pEvent->vscp_class = 10;
pEvent->vscp_type = 6;
pEvent->obid = 0;
pEvent->timestamp = 0;
memset( pEvent->GUID, 0, 16 );
pEvent->sizeData = 3;
pEvent->pdata = new unsigned char[3];
pEvent->pdata[ 0 ] = 138;
pEvent->pdata[ 1 ] = 0;
pEvent->pdata[ 2 ] = 30;
    
unsigned char dataCoding = getMeasurementDataCoding( pEvent );
if ( dataCoding = 138 ) {
    printf("Data Coding = %d\n", dataCoding );
}
else {
    printf("Error: Data Coding = %d\n", dataCoding );
}
`</code>`


## getDataCodingBitArray

`<code="c">`
unsigned long long getDataCodingBitArray( const unsigned char *pNorm,
                                                    int size)
`</code>`

Get measurement data that is coed as bits as a unsigned 64-bit value.

#####  pNorm

Pointer to the data coding byte of event measurement data.

#####  size

Number of bytes the measurement data consist of including the initial data coding byte.

##### Return value

A 64-bit unsigned integer is returned. The bits in the measurement data array are in MSB - LSB order and this is preserved in the unsigned 64-bit integer.

##### Example

`<code="c">`
unsigned char bitarry[3];
bitarry[0] = VSCP_DATACODING_BIT; // Data cding byte. Default unit, sensoridx=0
bitarry[1] = 0x55;
bitarry[2] = 0xAA;
unsigned long long bitarray64 = getDataCodingBitArray( bitarry, sizeof( bitarry ) )
`</code>`


##  getDataCodingInteger

`<code="c">`
unsigned long long getDataCodingInteger(const unsigned char *pCode, 
                                                   int size )
`</code>`

Get measurement data that is coded as a aigned  integer (1-7 bytes) as a 64-bit integer.

#####  pCode

A pointer to the data coding byte of the measurement data.

#####  size

The size of the measurement data including the data coding byte.

##### Return value

A double precision floating point value that is the decimal representation of the measurement data.

##### Example

`<code="c">`
unsigned char normarry[4];
normarry[0] = 0x60; // Data coding byte:integer, unit=0, sensoridx=0
normarry[1] = 0xFF;
normarry[2] = 0xFF;
normarry[3] = 0xFF;
double value =  getDataCodingInteger (normarry, sizeof( normarry ) );
if ( 3.1 == value ) {
    printf("OK - getDataCodingInteger value = %f \n", value );
}
else {
    printf("Error - getDataCodingNormalizedInteger value = %f \n", value );
}
`</code>`




##  getDataCodingNormalizedInteger

`<code="c">`
double getDataCodingNormalizedInteger(const unsigned char *pCode, 
                                                 int size )
`</code>`

Get measurement data that is coded as a normalized integer as a floating point value.

#####  pCode

A pointer to the data coding byte of the measurement data.

#####  size

The size of the measurement data including the data coding byte.

##### Return value

A double precision floating point value that is the decimal representation of the measurement data.

##### Example

`<code="c">`
unsigned char normarry[4];
normarry[0] = 0x89; // Data coding byte: Normalized integer, unit=1, sensoridx=1
normarry[1] = 0x02;
normarry[2] = 0x01;
normarry[3] = 0x36;
double value =  getDataCodingNormalizedInteger (normarry, sizeof( normarry ) );
if ( 3.1 == value ) {
    printf("OK - getDataCodingNormalizedInteger value = %f \n", value );
}
else {
    printf("Error - getDataCodingNormalizedInteger value = %f \n", value );
}
`</code>`



## getDataCodingString

`<code="c">`
int getDataCodingString(const unsigned char *pData,
                                   unsigned char dataLength, 
                                   char *strResult,
                                   size_t len )
`</code>`

#####  pData

Pointer to the data coding byte of the data.

#####  dataLength

Total length of the data including the data coding byte.

#####  strResult

Pointer to the buffer that will receive the resulting string.

##### len

Size of the supplied buffer (strResult). Max size of the string is 7 bytes + the terminating zero so the supplied size should be 8 bytes or larger.

##### Return value

VSCP_ERROR_SUCCESS is returned on success.

##### Example

`<code="c">`
unsigned char stringarry[6];
stringarry[0] = VSCP_DATACODING_STRING; // Data cding byte. Default unit, sensoridx=0
stringarry[1] = 0x32;
stringarry[2] = 0x33;
stringarry[3] = 0x34;
stringarry[4] = 0x2E;
stringarry[5] = 0x35;
char stringbuf[32];
if ( VSCP_ERROR_SUCCESS == getDataCodingString( stringarry,
                                                           sizeof( stringarry ), 
                                                           stringbuf,
                                                           sizeof( stringbuf ) ) ) {
    printf("OK - getDataCodingString value = %s \n", stringbuf );
}
else {
    printf("Error - getDataCodingString value = %s \n", stringbuf );
}
`</code>`


##  getVSCPMeasurementAsString

`<code="c">`
int getVSCPMeasurementAsString( const vscpEvent *pEvent, 
                                           char *pResult, 
                                           size_t len )
`</code>`

This method returns a string representing the measurement data. It recognize all data coding forms and give sensible output back.

#####  pEvent

The event the measurement string should be collected from.

##### pResult

The resulting measurement in string form.

##### len

Size for the buffer in which the resulting string is written.

##### Return value

VSCP_ERROR_SUCCESS is return on success.

##### Example

`<code="c">`
vscpEvent *pEventMeasurement = new vscpEvent;
pEventMeasurement->head = 0;
pEventMeasurement->vscp_class = 10;
pEventMeasurement->vscp_type = 6;
pEventMeasurement->obid = 0;
pEventMeasurement->timestamp = 0;
memset( pEventMeasurement->GUID, 0, 16 );
pEventMeasurement->sizeData = 4;
pEventMeasurement->pdata = new unsigned char[ pEventMeasurement->sizeData ];
pEventMeasurement->pdata[0] = 0x89;
pEventMeasurement->pdata[1] = 0x02;
pEventMeasurement->pdata[2] = 0x00;
pEventMeasurement->pdata[3] = 0xF1;

if ( VSCP_ERROR_SUCCESS == getVSCPMeasurementAsString( pEventMeasurement, 
                                                              stringbuf, 
                                                              sizeof( stringbuf ) ) ) {
    printf("OK - getVSCPMeasurementAsString value = %s \n", stringbuf );
}
else {
    printf("Error - getVSCPMeasurementAsString value = %s \n", stringbuf );
}

pEventMeasurement->pdata[0] = 0x89;
pEventMeasurement->pdata[1] = 0x02;
pEventMeasurement->pdata[2] = 0xFF;
pEventMeasurement->pdata[3] = 0xF1;

if ( VSCP_ERROR_SUCCESS == getVSCPMeasurementAsString( pEventMeasurement, 
                                                              stringbuf, 
                                                              sizeof( stringbuf ) ) ) {
    printf("OK - getVSCPMeasurementAsString value = %s \n", stringbuf );
}
else {
    printf("Error - getVSCPMeasurementAsString value = %s \n", stringbuf );
}

// Free the event
deleteVSCPevent( pEventMeasurement );
`</code>`



## getVSCPMeasurementAsDouble

`<code="c">`
int getVSCPMeasurementAsDouble( const vscpEvent *pEvent, 
                                           double *pvalue)
`</code>`

This method returns a double representing the measurement data. It recognize all data coding forms and give sensible output back.

#####  pEvent

The event that contain the measurement data.

##### pvalue

A pointer to a double that will get the measurement result.

##### Return value

VSCP_ERROR_SUCCESS is returned on success.

##### Example

`<code="c">`
pEventMeasurement->pdata[0] = VSCP_DATACODING_INTEGER;
pEventMeasurement->pdata[1] = 0xFF;
pEventMeasurement->pdata[2] = 0xFF;
pEventMeasurement->pdata[3] = 0xFF;

if ( VSCP_ERROR_SUCCESS == getVSCPMeasurementAsDouble( pEventMeasurement, &value ) ) {
    printf("OK - getVSCPMeasurementAsDouble value = %lf\n", value );
}
else {
    printf("Error - getVSCPMeasurementAsDouble value = %slf \n", value );
}
`</code>`



## getVSCPMeasurementFloat64AsString

`<code="c">`
int getVSCPMeasurementFloat64AsString(const vscpEvent *pEvent, 
                                                 char *pStrResult, 
                                                 size_t len )
`</code>`

This method displays data stored in 32-bit floating point form ([IEEE 754](https://en.wikipedia.org/wiki/IEEE_floating_point)) as a string

#####  pEvent

The event that contain the measurement data.

##### pStrResult

Buffer that will get the string result as a null terminated string.

##### len

The size of the buffer.

##### Return value

VSCP_ERROR_SUCCESS is returned on success.

##### Example

`<code="c">`
vscpEvent *pEventfloat = new vscpEvent;
pEventfloat->head = 0;
pEventfloat->vscp_class = 10;
pEventfloat->vscp_type = 6;
pEventfloat->obid = 0;
pEventfloat->timestamp = 0;
memset( pEventfloat->GUID, 0, 16 );
pEventfloat->sizeData = 8;
pEventfloat->pdata = new unsigned char[ pEventfloat->sizeData ];
pEventfloat->pdata[0] = 234;
pEventfloat->pdata[1] = 46;
pEventfloat->pdata[2] = 68;
pEventfloat->pdata[3] = 84;
pEventfloat->pdata[4] = 251;
pEventfloat->pdata[5] = 33;
pEventfloat->pdata[6] = 9;
pEventfloat->pdata[7] = 64;

if ( VSCP_ERROR_SUCCESS == 
       getVSCPMeasurementFloat64AsString( pEventfloat, 
                                                    stringbuf,
                                                    sizeof( stringbuf ) ) ) {
    printf("OK - getVSCPMeasurementFloat64AsString value = %s \n", stringbuf );
}
else {
    printf("Error - getVSCPMeasurementFloat64AsString value = %s \n", stringbuf );
}

// Free the event
deleteVSCPevent( pEventfloat );
`</code>`


## convertFloatToNormalizedEventData

`<code="c">`
int convertFloatToNormalizedEventData( 
                                   unsigned char *pdata,                                                        
                                   unsigned short *psize,    
                                   double value, 
                                   unsigned char unit,
                                   unsigned char sensoridx )
`</code>`

Write a 64-bit floating point value as event measurement data.

#####  pdata

Pointer to data buffer that will get the result. The buffer should be large enough to hold the normalized data. That is bigger than eight bytes.

#####  psize

The size of the written data will be returned here.

#####  psize

Floating point value to write as a 64-bit double.

#####  unit

A unit value 0-3

#####  sensoridx

A sensor index value 0-7

##### Return value

VSCP_ERROR_SUCCESS is returned on success.

##### Example

`<code="c">`
Example will be added.
`</code>`


##  convertFloatToFloatEventData

`<code="c">`
int convertFloatToFloatEventData( unsigned char *pdata,
                                              unsigned short *psize, 
                                              float value,
                                              unsigned char unit,
                                              unsigned char sensoridx )
`</code>`

Write a 32-nit floating point value as measurement event data.

#####  pdata

Pointer to data buffer that will get the result. The buffer should be large enough to hold the normalized data. That is bigger than eight bytes.

#####  psize

The size of the written data will be returned here.

#####  value

Floating point value to write as a 32-bit float.

#####  unit

A unit value 0-3

#####  sensoridx

A sensor index value 0-7


##### Return value

VSCP_ERROR_SUCCESS is returned on success.

##### Example

`<code="c">`
Example will be added.
`</code>`


## convertIntegerToNormalizedEventData

`<code="c">`
int convertIntegerToNormalizedEventData( unsigned char *pdata,
                                                    unsigned short *psize,
                                                    unsigned long long val64,
                                                    unsigned char unit,
                                                    unsigned char sensoridx )
`</code>`

Write an integer value as measurement event data in normalized integer form.

#####  pdata

Pointer to data buffer that will get the result. The buffer should be large enough to hold the normalized data. That is bigger than eight bytes.

#####  psize

The size of the written data will be returned here.

#####  value

Floating point value to write as a 64-bit float.

#####  unit

A unit value 0-3

#####  sensoridx

A sensor index value 0-7

##### Return value

VSCP_ERROR_SUCCESS is returned on success.

##### Example

`<code="c">`
Example will be added.
`</code>`

## makeFloatMeasurementEvent

`<code="c">`
int makeFloatMeasurementEvent( vscpEvent *pEvent, 
                                          float value,
                                          unsigned char unit,
                                          unsigned char sensoridx )
`</code>`

#####  pEvent

Pointer to a VSCP event that will get the result as it's data.

#####  psize

The size of the written data will be returned here.

#####  value

Floating point value to write as a 32-bit float.

#####  unit

A unit value 0-3

#####  sensoridx

A sensor index value 0-7


##### Return value

VSCP_ERROR_SUCCESS is returned on success.

##### Example

`<code="c">`
Example will be added.
`</code>`


## makeFloatMeasurementEvent

`<code="c">`
int makeFloatMeasurementEvent( vscpEvent *pEvent, 
                                          float value,
                                          unsigned char unit,
                                          unsigned char sensoridx )
`</code>`

Construct a floating point (32-bit) measurement VCSP event.

#####  pEvent

Pointer to a VSCP event that will get the result as it's data.

#####  psize

The size of the written data will be returned here.

#####  value

Floating point value to write as a 32-bit float.

#####  unit

A unit value 0-3

#####  sensoridx

A sensor index value 0-7


##### Return value

VSCP_ERROR_SUCCESS is returned on success.

##### Example

`<code="c">`
Example will be added.
`</code>`


##  getMeasurementAsFloat

`<code="c">`
int getMeasurementAsFloat(const unsigned char *pData, 
                                     unsigned char length,
                                     float *pResult )
`</code>`

This event is yet to be defined. Do not use.


##### Return value

VSCP_ERROR_SUCCESS is returned on success.

##  getMeasurementUnit

`<code="c">`
int getMeasurementUnit( const vscpEvent *pEvent )
`</code>`

Get unit for a measurement event. Some events does not have a unit defined and for then zero is always returned as it is understood that the default unit should be used.

##### Return value

Unit is returned as 0-3 for a Level I event and as 0-255 for a level II event.  


##  getMeasurementSensorIndex

`<code="c">`
int getMeasurementSenzorIndex( const vscpEvent *pEvent )
`</code>`

Get the sensor index for a measurement event. Some events does not have a sensor index defined and for them zero is always returned.

##### Return value

Sensor index is returned as 0-7 for a Level I event and as 0-255 for a level II event. 1 is returned if the event is not a measurement event or is invalid. 

##  getMeasurementZone

`<code="c">`
int getMeasurementZone( const vscpEvent *pEvent )
`</code>`

Get zone for a measurement event. Some events does not have a zone defined and for them zero is always returned.

##### Return value

Zone is returned as 0-255 where 255 means "all zones". 1 is returned if the event is not a measurement event or is invalid. 

##  getMeasurementSubZone

`<code="c">`
int getMeasurementSubZone( const vscpEvent *pEvent )
`</code>`

Get subzone for a measurement event.

##### Return value

Zone is returned as 0-255 where 255 means "all zones". -1 is returned if the event is not a measurement event or is invalid. Some events does not have a subzone defined and for them zero is always returned.  
## isMeasurement

`<code="c">`
int isMeasurement( const vscpEvent *pEvent )
`</code>`

Check if an event is a measurement.

##### Return value

VSCP_ERROR_SUCCESS is returned if the event is a measurement, VSCP_ERROR_ERROR is returned if the event is not a measurement.


## convertLevel1MeasuremenToLevel2Double

`<code="c">`
int convertLevel1MeasuremenToLevel2Double( vscpEvent *pEvent )
`</code>`

Convert Level I measurement to a Level II float measurement event ([CLASS2.MEASUREMENT_FLOAT](https://docs.vscp.org/spec/latest/#/./class2.measurement_float)).

##### Return value

VSCP_ERROR_SUCCESS is returned if the measurement event is converted correctly, VSCP_ERROR_ERROR is returned if not.


## convertLevel1MeasuremenToLevel2String

`<code="c">`
int convertLevel1MeasuremenToLevel2String( vscpEvent *pEvent )
`</code>`

Convert Level I measurement to a Level II string measurement event ([CLASS2.MEASUREMENT_STRING](https://docs.vscp.org/spec/latest/#/./class2.measurement_str)).

##### Return value

VSCP_ERROR_SUCCESS is returned if the measurement event is converted correctly, VSCP_ERROR_ERROR is returned if not.


## makeLevel2FloatMeasurementEvent

`<code="c">`
int makeLevel2FloatMeasurementEvent( vscpEvent *pEvent, 
                                                uint16_t type,
                                                double value,
                                                uint8_t unit,
                                                uint8_t sensoridx,
                                                uint8_t zone,
                                                uint8_t subzone )
`</code>`

Note that the GUID must be set externally.

#####  pEvent

Pointer to event that data should be written to. 

##### type

The VSCP type for the event. Must be one of the types in [CLASS1.MEASUREMENT](https://docs.vscp.org/spec/latest/#/./class1.measurement)

##### value

Floating point measurement value.

##### unit

Unit (0-255) for the measurement.

##### sensoridx

Sensor index (0-255) for the measurement.

##### zone

Zone (0-255) for the measurement.

##### subzone

Sub zone (0-255) for the measurement.

Construct a Level II floating point measurement event from supplied data.

##### Return value

VSCP_ERROR_SUCCESS is returned if the measurement event is constructed correctly, VSCP_ERROR_ERROR is returned if not.

## makeLevel2StringMeasurementEvent

`<code="c">`
int makeLevel2StringMeasurementEvent( vscpEvent *pEvent, 
                                                uint16_t type,
                                                double value,
                                                uint8_t unit,
                                                uint8_t sensoridx,
                                                uint8_t zone,
                                                uint8_t subzone )
`</code>`

Note that the GUID must be set externally.

#####  pEvent

Pointer to event that data should be written to. 

##### type

The VSCP type for the event. Must be one of the types in [CLASS1.MEASUREMENT](https://docs.vscp.org/spec/latest/#/./class1.measurement)

##### value

Floating point measurement value.

##### unit

Unit (0-255) for the measurement.

##### sensoridx

Sensor index (0-255) for the measurement.

##### zone

Zone (0-255) for the measurement.

##### subzone

Sub zone (0-255) for the measurement.

Construct a Level II string measurement event from supplied data.

##### Return value

VSCP_ERROR_SUCCESS is returned if the measurement event is constructed correctly, VSCP_ERROR_ERROR is returned if not.

## convertEventToJSON

`<code="c">`
int convertEventToJSON( vscpEvent *pEvent, char *pBuffer, size_t len );
`</code>`

Write VSCP event on JSON format to string. Format is specified in [vscp.h](https///github.com/grodansparadis/vscp/blob/master/src/vscp/common/vscp.h).

##### pEvent

Pointer to event.

##### pBuffer

Buffer that will receive string result ==

##### len

Size of string buffer.

##### Return value

VSCP_ERROR_SUCCESS is returned on success, VSCP_ERROR_BUFFER_TO_SMALL is returned if the size of the supplied buffer is to small.

## convertEventExToJSON

`<code="c">`
int convertEventExToJSON( vscpEventEx *pEventEx, char *pBuffer, size_t len );
`</code>`

Write VSCP event-ex on JSON format to string. Format is specified in [vscp.h](https///github.com/grodansparadis/vscp/blob/master/src/vscp/common/vscp.h).

##### pEventEx

Pointer to eventex.

##### pBuffer

Buffer that will receive string result ==

##### len

Size of string buffer.

##### Return value

VSCP_ERROR_SUCCESS is returned on success, VSCP_ERROR_BUFFER_TO_SMALL is returned if the size of the supplied buffer is to small.

## convertEventToXML

`<code="c">`
int convertEventToXML( vscpEvent *pEvent, char *pBuffer, size_t len );
`</code>`

Write VSCP event on XML format to string. Format is specified in [vscp.h](https///github.com/grodansparadis/vscp/blob/master/src/vscp/common/vscp.h).

##### pEvent

Pointer to event.

##### pBuffer

Buffer that will receive string result ==

##### len

Size of string buffer.

##### Return value

VSCP_ERROR_SUCCESS is returned on success, VSCP_ERROR_BUFFER_TO_SMALL is returned if the size of the supplied buffer is to small.

## convertEventExToXML

`<code="c">`
int convertEventExToXML( vscpEventEx *pEventEx, char *pBuffer, size_t len );
`</code>`

Write VSCP event-ex on XML format to string. Format is specified in [vscp.h](https///github.com/grodansparadis/vscp/blob/master/src/vscp/common/vscp.h).

##### pEventEx

Pointer to eventex.

##### pBuffer

Buffer that will receive string result ==

##### len

Size of string buffer.

##### Return value

VSCP_ERROR_SUCCESS is returned on success, VSCP_ERROR_BUFFER_TO_SMALL is returned if the size of the supplied buffer is to small.

## convertEventToHTML

`<code="c">`
int convertEventToHTML( vscpEvent *pEvent, char *pBuffer, size_t len );
`</code>`

Write VSCP event on HTML format to string. Format is specified in [vscp.h](https///github.com/grodansparadis/vscp/blob/master/src/vscp/common/vscp.h).

##### pEvent

Pointer to event.

##### pBuffer

Buffer that will receive string result ==

##### len

Size of string buffer.

##### Return value

VSCP_ERROR_SUCCESS is returned on success, VSCP_ERROR_BUFFER_TO_SMALL is returned if the size of the supplied buffer is to small.

## convertEventExToHTML

`<code="c">`
int convertEventExToHTML( vscpEventEx *pEventEx, char *pBuffer, size_t len );
`</code>`

Write VSCP event-ex on HTML format to string. Format is specified in [vscp.h](https///github.com/grodansparadis/vscp/blob/master/src/vscp/common/vscp.h).

##### pEventEx

Pointer to eventex.

##### pBuffer

Buffer that will receive string result ==

##### len

Size of string buffer.

##### Return value

VSCP_ERROR_SUCCESS is returned on success, VSCP_ERROR_BUFFER_TO_SMALL is returned if the size of the supplied buffer is to small.

\\ 
----
Copyright (c) 2000-2019 [Åke Hedman](mailto/akhe@grodansparadis.com), [Paradise of the Frog / Grodans Paradis AB](https://www.grodansparadis.com)
