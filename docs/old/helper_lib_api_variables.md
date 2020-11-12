# VSCP Helper library API - Variable handling 

Most functionality for handling variables on the VSCP daemon is supported by the library. The API is described here. Variables and there use is discussed [here](https://docs.vscp.org/vscpd/latest/#/decision_matrix)

**note** From version 2 names has been changed to **xxxxRemoteVariable** instead of **xxxxVariable**

## createRemoteVariable

`<code="c">`
int createRemoteVariable( long handle, 
                                    const char *pName,
                                    const char* pType,
                                    const char* pValue,
                                    int bPersistent ) 
`</code>`

Create a variable of a specific type. All the write methods below also create a variable if it does not exist but this method also allows to set the persistence.

#### handle

Handle for the communication channel obtained from a call to [newSession](./newsession.md).

#### pName

Pointer to a string containing the name of the variable. This name should have a character a-z as its first character and is not case sensitive. 

#### pType

Pointer to the type of the variable either as its symbolic name "string", "long" etc or to it's numerical code "1", "6".  Note that the numerical types are also in string form. The different variable types is described [here](https://docs.vscp.org/vscpd/13.1/#/./remote_variables?id=variable_types).

####  pValue

Pointer to string that contains the value of the string variable. 

#### bPersistent

If non zero the variable will be set to be persistent. This means that is will be saved to disk and will be available also in the future as long as it is not deleted.

#### Example

`<code="c">`

// Create a variable
char strBuf[32];
if ( VSCP_ERROR_SUCCESS == 
       (rv = createRemoteVariable( handle1, 
                                      "test_of_create_variable",
                                      "string",
                                      "Carpe Diem",
                                      1 ) ) )  {
    printf( "Command success: createRemoteVariable on channel 1\n" );
}
else {
    printf("\aCommand error: createRemoteVariable on channel 1  Error code=%d\n", rv);
}

if ( VSCP_ERROR_SUCCESS == 
        ( rv = getRemoteVariableString( handle1, 
                                             "test_of_create_variable", 
                                             strBuf, 
                                             sizeof( strBuf )-1 ) ) ) {
    printf( "Command success: getRemoteVariableString on channel 1\n" );
    printf(" Value = %s\n", strBuf );
}
else {
    printf("\aCommand error: getRemoteVariableString on channel 1  Error code=%d\n", rv);
}
`</code>`


## deleteRemoteVariable

`<code="c">`
int deleteRemoteVariable( long handle, const char *pName ) 
`</code>`

Delete a remote variable.

####  handle

Handle for the communication channel obtained from a call to [newSession](./newsession.md).

####  pName

Pointer to a string containing the name of the variable. This name should have a character a-z as its first character and is not case sensitive.

#### Example

`<code="C">`
// Delete a variable
if ( VSCP_ERROR_SUCCESS == 
      ( rv = deleteRemoteVariable( handle1, 
                                       "test_of_create_variable" ) ) )  {
    printf( "Command success: deleteRemoteVariable on channel 1\n" );
}
else {
    printf("\aCommand error: deleteRemoteVariable on channel 1  Error code=%d\n", rv);
}
`</code>`


## saveRemoteVariablesToDisk

`<code="c">`
int saveRemoteVariablesToDisk( long handle ) 
`</code>`

Saves variables marked as persistent to disk.

####  handle

Handle for the communication channel obtained from a call to [newSession](./newsession.md).

#### Example

`<code="C">`
// Save variables marked as persistent
if ( VSCP_ERROR_SUCCESS == 
       ( rv = saveRemoteVariablesToDisk( handle1 ) ) )  {
    printf( "Command success: saveRemoteVariablesToDisk on channel 1\n" );
}
else {
    printf("\aCommand error: saveRemoteVariablesToDisk on channel 1  Error code=%d\n", rv);
}
`</code>`

## getRemoteVariableString

`<code="c">`
int getRemoteVariableString( const char *pName, char *pValue, size_t len ) 
`</code>`

get value of string variable.

####  handle

Handle for the communication channel obtained from a call to [newSession](./newsession.md).

####  pName

Pointer to a string containing the name of the variable. This name should have a character a-z as its first character and is not case sensitive. 

####  pValue

Pointer to string that gets the value of the string variable. 

#### len

Size of supplied buffer that will receive the value.

####  Return value

Return VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while in a receive loop.


#### Example

`<code="c">`
// Read a value from a string variable
char strBuf[32];

if ( VSCP_ERROR_SUCCESS == 
        ( rv = getRemoteVariableString( handle1, "test_string_variable", strBuf, sizeof( strBuf )-1 ) ) ) {
    printf( "Command success: getRemoteVariableString on channel 1\n" );
    printf(" Value = %s\n", strBuf );
}
else {
    printf("\aCommand error: getRemoteVariableString on channel 1  Error code=%d\n", rv);
}
`</code>`

## getRemoteVariableValue

This function calls **getRemoteVariableValue**


## setRemoteVariableString

`<code="c">`
int setRemoteVariableString( long handle, const char *pName, char *pValue ) 
`</code>`

Write a value to a string variable. If the variable does not exist it will be created.

####  handle

Handle for the communication channel obtained from a call to [newSession](./newsession.md).

####  pName

Pointer to a string containing the name of the variable. This name should have a character a-z as its first character and is not case sensitive.

####  pValue

Pointer to string that contains the value to be written to the string. 

####  Return value

Return VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while in a receive loop.


#### Example

`<code="c">`
// Write a value to a string variable
if ( VSCP_ERROR_SUCCESS == 
        (rv = setRemoteVariableString( handle1, 
                            "test_sting_variable", 
                            "this is the value of the string variable" )  ) ) {
    printf( "Command success: setRemoteVariableString on channel 1\n" );
}
else {
    printf("Command error: setRemoteVariableString on channel 1  Error code=%d\n", rv);
}
`</code>`

## setRemoteVariableValue

This function calls **setRemoteVariableString**


## getRemoteVariableBool

`<code="c">`
int getRemoteVariableBool( long handle, const char *pName, bool *bValue ) 
`</code>`

Get variable value from boolean variable 

####  handle

Handle for the communication channel obtained from a call to [newSession](./newsession.md).

####  pName

Pointer to a string containing the name of the variable. This name should have a character a-z as its first character and is not case sensitive.

####  bValue

Pointer to boolean variable that get the value of the string variable.


#### Example

`<code="c">`
// Read a value from a boolean variable
int valBool;
if ( VSCP_ERROR_SUCCESS == 
        ( rv = getRemoteVariableBool( handle1, "test_bool_variable", &valBool ) ) ) {
    printf( "Command success: getRemoteVariableBool on channel 1\n" );
    printf(" Value = %s\n", valBool ? "true" : "false" );
}
else {
    printf("\aCommand error: getRemoteVariableBool on channel 1  Error code=%d\n", rv);
}
`</code>`



####  Return value

Return VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while in a receive loop.

## setRemoteVariableBool

`<code="c">`
int setRemoteVariableBool( long handle, const char *pName, bool bValue ) 
`</code>`

Get variable value from boolean variable

####  handle

Handle for the communication channel obtained from a call to [newSession](./newsession.md).

####  pName

Pointer to a string containing the name of the variable. This name should have a character a-z as its first character and is not case sensitive.

####  bValue

Pointer to boolean variable that get the value of the string variable.

####  Return value

Return VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while in a receive loop.


#### Example

`<code="c">`
// Write a value (false) to a boolean variable
if ( VSCP_ERROR_SUCCESS == 
        ( rv = setRemoteVariableBool( handle1, "test_bool_variable", 0 )  ) ) {
    printf( "Command success: setRemoteVariableBool on channel 1\n" );
}
else {
    printf("\aCommand error: setRemoteVariableBool on channel 1  Error code=%d\n", rv);
}
`</code>`



## getRemoteVariableInt

`<code="c">`
int getRemoteVariableInt( long handle, const char *pName, int *value ) 
`</code>`
Get variable value from integer variable 

####  handle

Handle for the communication channel obtained from a call to [newSession](./newsession.md).

####  pName

Pointer to a string containing the name of the variable. This name should have a character a-z as its first character and is not case sensitive.

####  value

Pointer to integer variable that get the value of the string variable. 

####  Return value

Return VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while in a receive loop.


#### Example

`<code="c">`
// Read a value from a int variable
int intValue;
if ( VSCP_ERROR_SUCCESS == 
            (rv = getRemoteVariableInt( handle1, "test_integer_variable", &intValue ) ) ) {
    printf( "Command success: getRemoteVariableInt on channel 1\n" );
    printf(" Value = %d\n", intValue );
}
else {
    printf("\aCommand error: getRemoteVariableInt on channel 1  Error code=%d\n", rv);
}
`</code>`



## setRemoteVariableInt

`<code="c">`
int setRemoteVariableInt( long handle, const char *pName, int value ) 
`</code>`
Get variable value from integer variable 

####  handle

Handle for the communication channel obtained from a call to [newSession](./newsession.md).

####  pName

Pointer to a string containing the name of the variable. This name should have a character a-z as its first character and is not case sensitive.

####  value

Pointer to integer variable that get the value of the string variable. 

####  Return value

Return VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while in a receive loop.


#### Example

`<code="c">`
// Write a value to an int variable
if ( VSCP_ERROR_SUCCESS == 
       ( rv = setRemoteVariableInt( handle1, "test_integer_variable", 777666 )  ) ) {
    printf( "Command success: setRemoteVariableInt on channel 1\n" );
}
else {
    printf("\aCommand error: setRemoteVariableInt on channel 1  Error code=%d\n", rv);
}
`</code>`



## getRemoteVariableLong

`<code="c">`
int getRemoteVariableLong( long handle, const char *pName, long *value ) 
`</code>`
Get variable value from long variable 

####  handle

Handle for the communication channel obtained from a call to [newSession](./newsession.md).

####  pName

Pointer to a string containing the name of the variable. This name should have a character a-z as its first character and is not case sensitive.

####  value

Pointer to long variable that get the value of the string variable. 

####  Return value

Return VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while in a receive loop.


#### Example

`<code="c">`
// Read a value from a long variable
long longValue;
if ( VSCP_ERROR_SUCCESS == 
         ( rv = getRemoteVariableLong( handle1, "test_long_variable", &longValue ) ) ) {
    printf( "Command success: getRemoteVariableLong on channel 1\n" );
    printf(" Value = %lu\n", longValue );
}
else {
    printf("\aCommand error: getRemoteVariableLong on channel 1  Error code=%d\n", rv);
}
`</code>`



## setRemoteVariableLong

`<code="c">`
int setRemoteVariableLong( long handle, const char *pName, long value ) 
`</code>`
Get variable value from long variable

####  handle

Handle for the communication channel obtained from a call to [newSession](./newsession.md).

####  pName

Pointer to a string containing the name of the variable. This name should have a character a-z as its first character and is not case sensitive. 

####  value

Pointer to long variable that get the value of the string variable. 

####  Return value

Return VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while in a receive loop.


#### Example

`<code="c">`
// Write a value to an long variable
if ( VSCP_ERROR_SUCCESS == 
    ( rv = setRemoteVariableLong( handle1, "test_long_variable", 123456780 )  ) ) {
    printf( "Command success: setRemoteVariableLong on channel 1\n" );
}
else {
    printf("\aCommand error: setRemoteVariableLong on channel 1  Error code=%d\n", rv);
}
`</code>`



## getRemoteVariableDouble

`<code="c">`
int getRemoteVariableDouble( long handle, const char *pName, double *value ) 
`</code>`
Get variable value from double variable 

####  handle

Handle for the communication channel obtained from a call to [newSession](./newsession.md).

####  pName

Pointer to a string containing the name of the variable. This name should have a character a-z as its first character and is not case sensitive. 

####  value

Pointer to double variable that get the value of the string variable. 

####  Return value

Return VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while in a receive loop.


#### Example

`<code="c">`
// Read a value from a float variable
double floatValue;
if ( VSCP_ERROR_SUCCESS == 
        ( rv = getRemoteVariableDouble( handle1, "test_float_variable", &floatValue ) ) ) {
    printf( "Command success: getRemoteVariableDouble on channel 1\n" );
    printf(" Value = %f\n", floatValue );
}
else {
    printf("\aCommand error: getRemoteVariableDouble on channel 1  Error code=%d\n", rv);
}
`</code>`



## setRemoteVariableDouble

`<code="c">`
int setRemoteVariableDouble( long handle, const char *pName, double value ) 
`</code>`
Get variable value from double variable 

####  handle

Handle for the communication channel obtained from a call to [newSession](./newsession.md).

####  pName

Pointer to a string containing the name of the variable. This name should have a character a-z as its first character and is not case sensitive. 

####  value

Pointer to double variable that get the value of the string variable. 

####  Return value

Return VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while in a receive loop.


#### Example

`<code="c">`
// Write a value to an float variable
if ( VSCP_ERROR_SUCCESS == 
        ( rv = setRemoteVariableDouble( handle1, "test_float_variable", 1.2345001 )  ) ) {
    printf( "Command success: setRemoteVariableDouble on channel 1\n" );
}
else {
    printf("\aCommand error: setRemoteVariableDouble on channel 1  Error code=%d\n", rv);
}
`</code>`


## getRemoteVariableMeasurement

`<code="c">`
int getRemoteVariableMeasurement( long handle, 
                                          const char *pName, 
                                          double *pvalue,
                                          int *punit,
                                          int *psensoridx,
                                          int *pzone,
                                          int *psubzone ) 
`</code>`
Get variable value, unit, sensor index, zone, subzone from a named measurement variable. 

####  handle

Handle for the communication channel obtained from a call to [newSession](./newsession.md).

####  pName

Pointer to a string containing the name of the variable. This name should have a character a-z as its first character and is not case sensitive.

####  pvalue

A double that get the value of the measurement. 

#### punit

Pointer to an integer that will get the unit for a measurement. For Level I this is a value between 0-3 and for Level II a value between 0-255.

#### psensoridx

Pointer to an integer that will get the sensor index for a measurement. For Level I this is a value between 0-7 and for Level II a value between 0-255.

#### pzone

Pointer to an integer that will get the zone for a measurement. This is a value between 0-255 where 255 is ALL zones. Some events does not have a zone defined for measurements and in this case the value 255 should be used.

#### psubzone

Pointer to an integer that will get the sub zone for a measurement. This is a value between 0-255 where 255 is ALL sub zones. Some events does not have a sub zone defined for measurements and in this case the value 255 should be used.

####  Return value

Return VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while in a receive loop.


#### Example

`<code="c">`
// Read a value from a measurement variable 
if ( VSCP_ERROR_SUCCESS == 
       ( rv = getRemoteVariableMeasurement( handle1, "test_measurement_variable", strBuf, sizeof(strBuf)-1  ) ) ) {
    printf( "Command success: getRemoteVariableMeasurement on channel 1\n" );
    printf(" Value = %s\n", strBuf );
}
else {
    printf("\aCommand error: getRemoteVariableMeasurement on channel 1  Error code=%d\n", rv);
}
`</code>`



## setRemoteVariableMeasurement

`<code="c">`
int setRemoteVariableMeasurement( long handle, 
                                        const char *pName, 
                                        double value,
                                        int unit,
                                        int sensoridx,
                                        int zone, 
                                        int subzone ) 
`</code>`
Set variable value, unit sensor index, zone and sub zone for a measurement variable 

####  handle

Handle for the communication channel obtained from a call to [newSession](./newsession.md).

####  pName

Pointer to a string containing the name of the variable. This name should have a character a-z as its first character and is not case sensitive.

####  value

Double that contain the value of a measurement. 

#### unit

Integer that contain the unit for a measurement. This should be a value between 0-3 for Level I and 0-255 for Level II.

#### sensoridx

Integer that contain the sensor index for a measurement. This should be a value between 0-7 for Level I and 0-255 for Level II.

#### zone

Integer that contain the zone for a measurement. This should be a value between 0-255 where 255 means ALL zones. Use 255 if no zone is specified as is the case for most Level I measurement events.

#### subzone

Integer that contain the sub zone for a measurement. This should be a value between 0-255 where 255 means ALL sub zones. Use 255 if no sub zone is specified as is the case for most Level I measurement events.

####  Return value

Return VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while in a receive loop.


#### Example

`<code="c">`
// Write a value to an measurement variable
if ( VSCP_ERROR_SUCCESS == 
       ( rv = setRemoteVariableMeasurement( handle1, "test_measurement_variable", "138,0,23" )  ) ) {
    printf( "Command success: setRemoteVariableMeasurement on channel 1\n" );
}
else {
    printf("\aCommand error: setRemoteVariableMeasurement on channel 1  Error code=%d\n", rv);
}
`</code>`



## getRemoteVariableEvent

`<code="c">`
int getVariableEvent( long handle, const char *pName, vscpEvent *pEvent ) 
`</code>`
Get variable value from event variable 

####  handle

Handle for the communication channel obtained from a call to [newSession](./newsession.md).

####  pName

Pointer to a string containing the name of the variable. This name should have a character a-z as its first character and is not case sensitive.

####  pEvent

Pointer to event variable that get the value of the string variable. 

####  Return value

Return VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while in a receive loop.


#### Example

`<code="c">`
pEvent = new vscpEvent;

// Read a value from a event variable 
if ( VSCP_ERROR_SUCCESS == 
        ( rv = getRemoteVariableEvent( handle1, "test_event_variable", pEvent  ) ) ) {
    printf( "Command success: getRemoteVariableEvent on channel 1\n" );
    printf(" Event: class=%d Type=%d sizeData=%d\n", 
                        pEvent->vscp_class,
                        pEvent->vscp_type,
                        pEvent->sizeData );
    if ( pEvent->sizeData && ( NULL != pEvent->pdata ) ) {
         printf("Data = ");
         for ( int i=0; i`<pEvent->`sizeData; i++ ) {
             printf("%d ", pEvent->pdata[i] );
         }
         printf("\n");
    }
}
else {
    printf("\aCommand error: getRemoteVariableEvent on channel 1  Error code=%d\n", rv);
}

// Free the event
deleteVSCPevent( pEvent );
`</code>`



## setRemoteVariableEvent

`<code="c">`
int setRemoteVariableEvent( long handle, const char *pName, vscpEvent *pEvent ) 
`</code>`
Get variable value from event variable 

#####  handle

Handle for the communication channel obtained from a call to [newSession](./newsession.md).

####  pName

Pointer to a string containing the name of the variable. This name should have a character a-z as its first character and is not case sensitive. 

####  pEvent

Pointer to event variable that get the value of the string variable. 

####  Return value

Return VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while in a receive loop.

#### Example

`<code="c">`
// Write a value to an event variable
pEvent = new vscpEvent;
pEvent->head = 0;
pEvent->vscp_class = 10;
pEvent->vscp_type = 6;
pEvent->obid = 0;
pEvent->timestamp = 0;
memset( pEvent->GUID, 0, 16 );
pEvent->sizeData = 4;
pEvent->pdata = new unsigned char[4];
pEvent->pdata[ 0 ] = 10;
pEvent->pdata[ 1 ] = 20;
pEvent->pdata[ 2 ] = 30;
pEvent->pdata[ 3 ] = 40;
    
if ( VSCP_ERROR_SUCCESS == 
        ( rv = setRemoteVariableEvent( handle1, "test_event_variable", pEvent )  ) ) {
    printf( "Command success: setVariableEvent on channel 1\n" );
}
else {
    printf("\aCommand error: setRemoteVariableEvent on channel 1  Error code=%d\n", rv);
}

// Free the event
deleteVSCPevent( pEvent );
`</code>`



## getRemoteVariableEventEx

`<code="c">`
int getRemoteVariableEventEx( long handle, const char *pName, vscpEventEx *pEvent ) 
`</code>`
Get variable value from event variable 

####  handle

Handle for the communication channel obtained from a call to [newSession](./newsession.md).

####  pName

Pointer to a string containing the name of the variable. This name should have a character a-z as its first character and is not case sensitive. 

####  pEvent

Pointer to event variable that get the value of the string variable. 

####  Return value

Return VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while in a receive loop.


#### Example

`<code="c">`
// Read a value from a event variable 
vscpEventEx ex1;
if ( VSCP_ERROR_SUCCESS == 
         ( rv = getRemoteVariableEventEx( handle1, "test_eventex_variable", &ex1  ) ) ) {
    printf( "Command success: getVariableEventEx on channel 1\n" );
    printf(" Event: class=%d Type=%d sizeData=%d\n", 
                        ex1.vscp_class,
                        ex1.vscp_type,
                        ex1.sizeData );
    if ( ex1.sizeData ) {
        printf("Data = ");
        for ( int i=0; i<ex1.sizeData; i++ ) {
            printf("%d ", ex1.data[i] );
        }
        printf("\n");
    }
}
else {
    printf("\aCommand error: getRemoteVariableEvent on channel 1  Error code=%d\n", rv);
}
`</code>`



## setRemoteVariableEventEx

`<code="c">`
int setRemoteVariableEventEx( long handle, const char *pName, vscpEventEx *pEvent ) 
`</code>`
Get variable value from event variable 

####  handle

Handle for the communication channel obtained from a call to [newSession](./newsession.md).

####  pName

Pointer to a string containing the name of the variable. This name should have a character a-z as its first character and is not case sensitive.

####  pEvent

Pointer to event variable that get the value of the string variable.

####  Return value

Return VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while in a receive loop.


#### Example

`<code="c">`
// Write a value to an event variable
vscpEventEx ex1;
ex1.head = 0;
ex1.vscp_class = 50;
ex1.vscp_type = 22;
ex1.obid = 0;
ex1.timestamp = 0;
memset( ex1.GUID, 0, 16 );
ex1.sizeData = 4;
ex1.data[ 0 ] = 40;
ex1.data[ 1 ] = 30;
ex1.data[ 2 ] = 20;
ex1.data[ 3 ] = 10;
    
if ( VSCP_ERROR_SUCCESS == 
        ( rv = setRemoteVariableEventEx( handle1, "test_eventex_variable", &ex1 )  ) ) {
    printf( "Command success: setRemoteVariableEventEx on channel 1\n" );
}
else {
    printf("\aCommand error: setRemoteVariableEventEx on channel 1  Error code=%d\n", rv);
}

// Read a value from a event variable 
if ( VSCP_ERROR_SUCCESS == 
     ( rv = getRemoteVariableEventEx( handle1, "test_eventex_variable", &ex1  ) ) ) {
    printf( "Command success: getRemoteVariableEventEx on channel 1\n" );
    printf(" Event: class=%d Type=%d sizeData=%d\n", 
                        ex1.vscp_class,
                        ex1.vscp_type,
                        ex1.sizeData );
    if ( ex1.sizeData ) {
         printf("Data = ");
         for ( int i=0; i<ex1.sizeData; i++ ) {
              printf("%d ", ex1.data[i] );
         }
         printf("\n");
    }
}
else {
     printf("\aCommand error: getRemoteVariableEvent on channel 1  Error code=%d\n", rv);
}
`</code>`



## getRemoteVariableGUIDString

`<code="c">`
int getRemoteVariableGUIDString( long handle, 
                                            const char *pName, 
                                            const char *pGUID, size_t len ) 
`</code>`

Get variable value from GUID variable 

####  handle

Handle for the communication channel obtained from a call to [newSession](./newsession.md).

####  pName

Pointer to a string containing the name of the variable. This name should have a character a-z as its first character and is not case sensitive.

####  pGUID

Pointer to event variable that get the value of the GUID variable. 

#### len

Size of buffer for GUID.

####  Return value

Return VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while in a receive loop.


#### Example

`<code="c">`
// Read a value from a GUID variable - string type
if ( VSCP_ERROR_SUCCESS == 
         ( rv = getRemoteVariableGUIDString( handle1, "test_guidstr_variable", strGUID, sizeof(strGUID)-1 )  ) )  {
    printf( "Command success: getRemoteVariableGUIDString on channel 1\n" );
    printf(" Value = %s\n", strGUID );
}
else {
    printf("\aCommand error: getRemoteVariableGUIDString on channel 1  Error code=%d\n", rv);
}
`</code>`



## setRemoteVariableGUIDString

`<code="c">`
int getRemoteVariableGUID( long handle, const char *pName, const char * pGUID ) 
`</code>`

Set the value for GUID variable.

####  handle

Handle for the communication channel obtained from a call to [newSession](./newsession.md).

####  pName

Pointer to a string containing the name of the variable. This name should have a character a-z as its first character and is not case sensitive. 

####  pGUID

Pointer to a string that contains the GUID on the string form 
"FF:FF:FF:FF:FF:FF:FF:FF:FF:FF:FF:FF:FF:FF:FF:FF"

####  Return value

Return VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while in a receive loop.


#### Example

`<code="c">`
// Write a value to an GUID variable - string type
char strGUID[64];
strcpy( strGUID, "FF:FF:FF:FF:FF:FF:FF:00:00:00:00:7F:00:01:01:FD" );

if ( VSCP_ERROR_SUCCESS == 
        ( rv = setRemoteVariableGUIDString( handle1, "test_guidstr_variable", strGUID ) ) ) {
    printf( "Command success: setRemoteVariableGUIDString on channel 1\n" );
}
else {
     printf("\aCommand error: setRemoteVariableGUIDString on channel 1  Error code=%d\n", rv);
}
`</code>`


## getRemoteVariableGUIDArray

`<code="c">`
int getRemoteVariableGUIDArray( long handle, const char *pName, const char * pGUID ) 
`</code>`

Get variable value from GUID variable. Array type. 

####  handle

Handle for the communication channel obtained from a call to [newSession](./newsession.md).

####  pName

Pointer to a string containing the name of the variable. This name should have a character a-z as its first character and is not case sensitive.

####  pGUID

Pointer to an array forming a 16-byte GUID.  

####  Return value

Return VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while in a receive loop.


#### Example

`<code="c">`
// Read a value from a GUID variable - array type
if ( VSCP_ERROR_SUCCESS == 
      ( rv = getRemoteVariableGUIDArray( handle1, "test_guidarray_variable", GUID  ) ) )  {
    printf( "Command success: getRemoteVariableGUIDArray on channel 1\n" );
    printf(" Value = " );
    for ( int i=0; i<16; i++ ) {
        printf("%d ", GUID[i] );    
    }
    printf("\n");
}
else {
    printf("\aCommand error: getRemoteVariableGUIDArray on channel 1  Error code=%d\n", rv);
}
`</code>`



## setRemoteVariableGUIDArray

`<code="c">`
int getRemoteVariableGUIDArray( long handle, const char *pName, const char * pGUID ) 
`</code>`

Get variable value from GUID variable. This is a variant where the GUID is stored in an array.

####  handle

Handle for the communication channel obtained from a call to [newSession](./newsession.md).

####  pName

Pointer to a string containing the name of the variable. This name should have a character a-z as its first character and is not case sensitive. 

####  pGUID

Pointer to an array forming a 16-byte GUID. 

####  Return value

Return VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while in a receive loop.


#### Example

`<code="c">`
// Write a value to an GUID variable - array type
unsigned char GUID[16];
memset( GUID, 0, 16 );
for ( int i=0;i<16; i++ ) {
    GUID[i] = i;
}

if ( VSCP_ERROR_SUCCESS == 
         ( rv = setRemoteVariableGUIDArray( handle1, "test_guidarray_variable", GUID ) ) ) {
    printf( "Command success: setRemoteVariableGUIDArray on channel 1\n" );
}
else {
    printf("\aCommand error: setRemoteVariableGUIDArray on channel 1  Error code=%d\n", rv);
}
`</code>`

## getRemoteVariableVSCPdata

`<code="c">`
int getRemoteVariableVSCPdata( long handle, const char *pName, uint16_t *psizeData, uint8_t *pData ) 
`</code>`

Get variable value from VSCP data variable 

####  handle

Handle for the communication channel obtained from a call to [newSession](./newsession.md).

####  pName

Pointer to a string containing the name of the variable. This name should have a character a-z as its first character and is not case sensitive. 

####  psizeData

Pointer to variable that will hold the size of the data array 

####  pData

Pointer to VSCP data array variable (unsigned char [8] ) that get the value of the string variable. 

####  Return value

Return VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while in a receive loop.



#### Example

`<code="c">`
unsigned short size;
memset( dataArray, 0, sizeof( dataArray ) );
   
// Read a value from a data variable 
if ( VSCP_ERROR_SUCCESS == 
        ( rv = getRemoteVariableVSCPData( handle1, "test_dataarray_variable", dataArray, &size  ) ) )  {
    printf( "Command success: getRemoteVariableVSCPData on channel 1\n" );
    printf(" Value = " );
    for ( int i=0; i<size; i++ ) {
        printf("%d ", dataArray[i] );    
    }
    printf("\n");
}
else {
    printf("\aCommand error: getRemoteVariableVSCPData on channel 1  Error code=%d\n", rv);
}
`</code>`



## setRemoteVariableVSCPdata

`<code="c">`
int setRemoteVariableVSCPdata( long handle, 
                                  const char *pName, 
                                  uint16_t sizeData, 
                                  uint8_t *pData ) 
`</code>`

Get variable value from VSCP data variable 

####  handle

Handle for the communication channel obtained from a call to [newSession](./newsession.md).

####  pName

Pointer to a string containing the name of the variable. This name should have a character a-z as its first character and is not case sensitive.

####  sizeData

Pointer to variable that will hold the size of the data array 

####  pData

Pointer to VSCP data array variable (unsigned char [8] ) that get the value of the string variable. 

####  Return value

Return VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while in a receive loop.


#### Example

`<code="c">`
unsigned char dataArray[10];
memset( dataArray, 0, sizeof(dataArray) );
for ( int i=0; i<sizeof(dataArray); i++ ) {
    dataArray[ i ] = i;    
}

if ( VSCP_ERROR_SUCCESS == 
        ( rv = setRemoteVariableVSCPData( handle1, "test_dataarray_variable", dataArray, sizeof( dataArray ) ) ) ) {
    printf( "Command success: setRemoteVariableVSCPData on channel 1\n" );
}
else {
    printf("\aCommand error: setRemoteVariableVSCPData on channel 1  Error code=%d\n", rv);
}
`</code>`



## getRemoteVariableVSCPclass

`<code="c">`
int getRemoteVariableVSCPclass( long handle, 
                                    const char *pName, 
                                    uint16_t *vscp_class ) 
`</code>`
Get variable value from class variable 

####  handle

Handle for the communication channel obtained from a call to [newSession](./newsession.md).

####  pName

Pointer to a string containing the name of the variable. This name should have a character a-z as its first character and is not case sensitive.

####  vscp_class

Pointer to int that get the value of the class variable. 

####  Return value

Return VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while in a receive loop.



#### Example

`<code="c">`
unsigned short vscpclass;

// Read a value from aVSCP class type
if ( VSCP_ERROR_SUCCESS == 
        ( rv = getRemoteVariableVSCPClass( handle1, "test_vscp_class_variable", &vscpclass ) ) )  {
    printf( "Command success: getRemoteVariableVSCPClass on channel 1\n" );
    printf(" Value = %d\n", vscpclass );
}
else {
    printf("\aCommand error: getRemoteVariableVSCPClass on channel 1  Error code=%d\n", rv);
}
`</code>`



## setRemoteVariableVSCPclass

`<code="c">`
int setRemoteVariableVSCPclass( long handle, 
                                     const char *pName, 
                                     unsigned short vscp_class ) 
`</code>`

Get variable value from class variable 

####  handle

Handle for the communication channel obtained from a call to [newSession](./newsession.md).

####  pName

Pointer to a string containing the name of the variable. This name should have a character a-z as its first character and is not case sensitive.

####  vscp_class

Pointer to int that get the value of the class variable. 

####  Return value

Return VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while in a receive loop.


#### Example

`<code="c">`
// Write a value for VSCP class type
if ( VSCP_ERROR_SUCCESS == 
        ( rv = setRemoteVariableVSCPClass( handle1, "test_vscp_class_variable", 10 ) ) ) {
    printf( "Command success: setRemoteVariableVSCPClass on channel 1\n" );
}
else {
    printf("\aCommand error: setRemoteVariableVSCPClass on channel 1  Error code=%d\n", rv);
}
`</code>`



## getRemoteVariableVSCPtype

`<code="c">`
int getRemoteVariableVSCPtype( long handle, 
                                   const char *pName, 
                                   unsigned short *vscp_type ) 
`</code>`

Get variable value from type variable 

####  handle

Handle for the communication channel obtained from a call to [newSession](./newsession.md).

####  pName

Pointer to a string containing the name of the variable. This name should have a character a-z as its first character and is not case sensitive.

####  vscp_type

Pointer to int that get the value of the type variable. 

####  Return value

Return VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while in a receive loop.


#### Example

`<code="c">`
unsigned short vscptype;

// Read a value from aVSCP type type
if ( VSCP_ERROR_SUCCESS == 
        ( rv = getRemoteVariableVSCPType( handle1, "test_vscp_type_variable", &vscptype ) ) )  {
    printf( "Command success: getRemoteVariableVSCPType on channel 1\n" );
    printf(" Value = %d\n", vscptype );
}
else {
    printf("\aCommand error: getRemoteVariableVSCPType on channel 1  Error code=%d\n", rv);
}
`</code>`



## setRemoteVariableVSCPtype

`<code="c">`
int setRemoteVariableVSCPtype( long handle, 
                                    const char *pName, 
                                    unsigned short vscp_type ) 
`</code>`

Get variable value from type variable 

####  handle

Handle for the communication channel obtained from a call to [newSession](./newsession.md).

####  pName

Pointer to a string containing the name of the variable. This name should have a character a-z as its first character and is not case sensitive.

####  vscp_type

Pointer to int that get the value of the type variable. 

####  Return value

Return VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while in a receive loop.



#### Example

`<code="c">`
// Write a value for VSCP type type
if ( VSCP_ERROR_SUCCESS == 
      ( rv = setRemoteVariableVSCPType( handle1, "test_vscp_type_variable", 22 ) ) ) {
    printf( "Command success: setRemoteVariableVSCPType on channel 1\n" );
}
else {
    printf("\aCommand error: setRemoteVariableVSCPType on channel 1  Error code=%d\n", rv);
}
`</code>`

## getRemoteVariableVSCPTimestamp

`<code="c">`
int getRemoteVariableVSCPTimestamp( long handle, 
                                                const char *pName, 
                                                unsigned long *vscp_timestamp ) 
`</code>`

Get variable value from VSCP timestamp variable 

####  handle

Handle for the communication channel obtained from a call to [newSession](./newsession.md).

####  pName

Pointer to a string containing the name of the variable. This name should have a character a-z as its first character and is not case sensitive.

#### vscp_timestamp

Pointer to string that will get the value of the VSCP timestamp variable.

####  Return value

Return VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while in a receive loop.



#### Example

`<code="c">`

`</code>`

## setRemoteVariableVSCPTimestamp

`<code="c">`
setRemoteVariableVSCPTimestamp( long handle, 
                                            const char *pName, 
                                            unsigned long vscp_timestamp ) 
`</code>`

Set variable value from VSCP timstamp

####  handle

Handle for the communication channel obtained from a call to [newSession](./newsession.md).

####  pName

Pointer to a string containing the name of the variable. This name should have a character a-z as its first character and is not case sensitive.

####  vscp_timestamp

Pointer to unsigned long that holds the VSCP timestamp to set variable to. 

####  Return value

Return VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while in a receive loop.



#### Example

`<code="c">`
`</code>`


## getRemoteVariableDateTime

`<code="c">`
getRemoteVariableDateTime( long handle, 
                                    const char *pName, 
                                    char *pValue, 
                                    size_t len ) 
`</code>`

Get variable value from datetime variable. The returned value is on ISO form "YYYY-MM-DDTHH:MM:SS" 

####  handle

Handle for the communication channel obtained from a call to [newSession](./newsession.md).

####  pName

Pointer to a string containing the name of the variable. This name should have a character a-z as its first character and is not case sensitive.

#### pValue

Pointer to string buffer that will get the value of the datetime variable.

#### len

Size of string buffer.

####  Return value

Return VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while in a receive loop.



#### Example

`<code="c">`
`</code>`

## setRemoteVariableDateTime

`<code="c">`
int setRemoteVariableDateTime( long handle, 
                                        const char *pName, 
                                        char *pValue ) 
`</code>`

Set variable value from dattime on ISO form "YYYY-MM-DDTHH:MM:SS"

####  handle

Handle for the communication channel obtained from a call to [newSession](./newsession.md).

####  pName

Pointer to a string containing the name of the variable. This name should have a character a-z as its first character and is not case sensitive.

####  pValue

Pointer to string that contains the value the variable should be set to. 

####  Return value

Return VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while in a receive loop.



#### Example

`<code="c">`
`</code>`


## getRemoteVariableDate

`<code="c">`
getRemoteVariableDate( long handle, 
                                 const char *pName, 
                                 char *pValue, 
                                 size_t len ) 
`</code>`

Get variable value from date variable. The returned value is on ISO form "YYYY-MM-DD" 

####  handle

Handle for the communication channel obtained from a call to [newSession](./newsession.md).

####  pName

Pointer to a string containing the name of the variable. This name should have a character a-z as its first character and is not case sensitive.

#### pValue

Pointer to string buffer that will get the value of the date variable.

#### len

Size of string buffer.

####  Return value

Return VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while in a receive loop.



#### Example

`<code="c">`

`</code>`

## setRemoteVariableDate

`<code="c">`
int setRemoteVariableDate( long handle, 
                                        const char *pName, 
                                        char *pValue ) 
`</code>`

Set variable value from dattime on ISO form "YYYY-MM-DD"

####  handle

Handle for the communication channel obtained from a call to [newSession](./newsession.md).

####  pName

Pointer to a string containing the name of the variable. This name should have a character a-z as its first character and is not case sensitive.

####  pValue

Pointer to string that contains the value the variable should be set to. 

####  Return value

Return VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while in a receive loop.



#### Example

`<code="c">`
`</code>`


## getRemoteVariableTime

`<code="c">`
getRemoteVariableTime( long handle, 
                                 const char *pName, 
                                 char *pValue, 
                                 size_t len ) 
`</code>`

Get variable value from time variable. The returned value is on ISO form "HH:MM:SS" 

####  handle

Handle for the communication channel obtained from a call to [newSession](./newsession.md).

####  pName

Pointer to a string containing the name of the variable. This name should have a character a-z as its first character and is not case sensitive.

#### pValue

Pointer to string buffer that will get the value of the date variable.

#### len

Size of string buffer.

####  Return value

Return VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while in a receive loop.



#### Example

`<code="c">`

`</code>`

## setRemoteVariableTime

`<code="c">`
int setRemoteVariableTime( long handle, 
                                        const char *pName, 
                                        char *pValue ) 
`</code>`

Set variable value from time on ISO form "HH:MM:SS"

####  handle

Handle for the communication channel obtained from a call to [newSession](./newsession.md).

####  pName

Pointer to a string containing the name of the variable. This name should have a character a-z as its first character and is not case sensitive.

####  pValue

Pointer to string that contains the value the variable should be set to. 

####  Return value

Return VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while in a receive loop.



#### Example

`<code="c">`
`</code>`


## getRemoteVariableBlob

`<code="c">`
getRemoteVariableBlob( long handle, 
                                 const char *pName, 
                                 char *pValue, 
                                 size_t len ) 
`</code>`

Get variable value from blob variable. The returned value is BASE64 encoded. 

####  handle

Handle for the communication channel obtained from a call to [newSession](./newsession.md).

####  pName

Pointer to a string containing the name of the variable. This name should have a character a-z as its first character and is not case sensitive.

#### pValue

Pointer to string buffer that will get the value of the date variable.

#### len

Size of string buffer.

####  Return value

Return VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while in a receive loop.



#### Example

`<code="c">`

`</code>`

## setRemoteVariableBlob

`<code="c">`
int setRemoteVariableBlob( long handle, 
                                        const char *pName, 
                                        char *pValue ) 
`</code>`

Set variable value for a blob variable. The value is always expected to be BASE64 encoded.

####  handle

Handle for the communication channel obtained from a call to [newSession](./newsession.md).

####  pName

Pointer to a string containing the name of the variable. This name should have a character a-z as its first character and is not case sensitive.

####  pValue

Pointer to string that contains the value the variable should be set to. 

####  Return value

Return VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while in a receive loop.



#### Example

`<code="c">`
`</code>`

## getRemoteVariableMIME

`<code="c">`
getRemoteVariableMIME( long handle, 
                                 const char *pName, 
                                 char *pValue, 
                                 size_t len ) 
`</code>`

Get variable value from MIME variable. The returned value is BASE64 encoded. 

####  handle

Handle for the communication channel obtained from a call to [newSession](./newsession.md).

####  pName

Pointer to a string containing the name of the variable. This name should have a character a-z as its first character and is not case sensitive.

#### pValue

Pointer to string buffer that will get the value of the date variable.

#### len

Size of string buffer.

####  Return value

Return VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while in a receive loop.



#### Example

`<code="c">`

`</code>`

## setRemoteVariableMIME

`<code="c">`
int setRemoteVariableMIME( long handle, 
                                     const char *pName, 
                                     char *pValue ) 
`</code>`

Set variable value for a MIME variable. The value is always expected to be BASE64 encoded.

####  handle

Handle for the communication channel obtained from a call to [newSession](./newsession.md).

####  pName

Pointer to a string containing the name of the variable. This name should have a character a-z as its first character and is not case sensitive.

####  pValue

Pointer to string that contains the value the variable should be set to. 

####  Return value

Return VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while in a receive loop.



#### Example

`<code="c">`
`</code>`

## getRemoteVariableHTML

`<code="c">`
getRemoteVariableHTML( long handle, 
                                 const char *pName, 
                                 char *pValue, 
                                 size_t len ) 
`</code>`

Get variable value from HTML variable. The returned value is BASE64 encoded. 

####  handle

Handle for the communication channel obtained from a call to [newSession](./newsession.md).

####  pName

Pointer to a string containing the name of the variable. This name should have a character a-z as its first character and is not case sensitive.

#### pValue

Pointer to string buffer that will get the value of the date variable.

#### len

Size of string buffer.

####  Return value

Return VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while in a receive loop.



#### Example

`<code="c">`

`</code>`

## setRemoteVariableHTML

`<code="c">`
int setRemoteVariableHTML( long handle, 
                                        const char *pName, 
                                        char *pValue ) 
`</code>`

Set variable value for a HTML variable. The value is always expected to be BASE64 encoded.

####  handle

Handle for the communication channel obtained from a call to [newSession](./newsession.md).

####  pName

Pointer to a string containing the name of the variable. This name should have a character a-z as its first character and is not case sensitive.

####  pValue

Pointer to string that contains the value the variable should be set to. 

####  Return value

Return VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while in a receive loop.

#### Example

`<code="c">`
`</code>`

## getRemoteVariableJavaScript

`<code="c">`
getRemoteVariableJavaScript( long handle, 
                                    const char *pName, 
                                    char *pValue, 
                                    size_t len ) 
`</code>`

Get variable value from JavaScript variable. The returned value is BASE64 encoded. 

####  handle

Handle for the communication channel obtained from a call to [newSession](./newsession.md).

####  pName

Pointer to a string containing the name of the variable. This name should have a character a-z as its first character and is not case sensitive.

#### pValue

Pointer to string buffer that will get the value of the date variable.

#### len

Size of string buffer.

####  Return value

Return VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while in a receive loop.



#### Example

`<code="c">`

`</code>`

## setRemoteVariableJavaScript

`<code="c">`
int setRemoteVariableJavaScript( long handle, 
                                        const char *pName, 
                                        char *pValue ) 
`</code>`

Set variable value for a JavaScript variable. The value is always expected to be BASE64 encoded.

####  handle

Handle for the communication channel obtained from a call to [newSession](./newsession.md).

####  pName

Pointer to a string containing the name of the variable. This name should have a character a-z as its first character and is not case sensitive.

####  pValue

Pointer to string that contains the value the variable should be set to. 

####  Return value

Return VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while in a receive loop.

#### Example

`<code="c">`
`</code>`

## getRemoteVariableLUA

`<code="c">`
getRemoteVariableLUA( long handle, 
                                const char *pName, 
                                char *pValue, 
                                size_t len ) 
`</code>`

Get variable value from LUA script variable. The returned value is BASE64 encoded. 

####  handle

Handle for the communication channel obtained from a call to [newSession](./newsession.md).

####  pName

Pointer to a string containing the name of the variable. This name should have a character a-z as its first character and is not case sensitive.

#### pValue

Pointer to string buffer that will get the value of the date variable.

#### len

Size of string buffer.

####  Return value

Return VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while in a receive loop.



#### Example

`<code="c">`

`</code>`

## setRemoteVariableLUA

`<code="c">`
int setRemoteVariableLUA( long handle, 
                                        const char *pName, 
                                        char *pValue ) 
`</code>`

Set variable value for a LUA script variable. The value is always expected to be BASE64 encoded.

####  handle

Handle for the communication channel obtained from a call to [newSession](./newsession.md).

####  pName

Pointer to a string containing the name of the variable. This name should have a character a-z as its first character and is not case sensitive.

####  pValue

Pointer to string that contains the value the variable should be set to. 

####  Return value

Return VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while in a receive loop.



#### Example

`<code="c">`
`</code>`


## getRemoteVariableLUARES

`<code="c">`
getRemoteVariableLUARES( long handle, 
                                    const char *pName, 
                                    char *pValue, 
                                    size_t len ) 
`</code>`

Get variable value from LUARES variable. The returned value is BASE64 encoded. 

####  handle

Handle for the communication channel obtained from a call to [newSession](./newsession.md).

####  pName

Pointer to a string containing the name of the variable. This name should have a character a-z as its first character and is not case sensitive.

#### pValue

Pointer to string buffer that will get the value of the date variable.

#### len

Size of string buffer.

####  Return value

Return VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while in a receive loop.



#### Example

`<code="c">`

`</code>`

## setRemoteVariableLUARES

`<code="c">`
int setRemoteVariableLUARES( long handle, 
                                        const char *pName, 
                                        char *pValue ) 
`</code>`

Set variable value for a LUARES variable. The value is always expected to be BASE64 encoded.

####  handle

Handle for the communication channel obtained from a call to [newSession](./newsession.md).

####  pName

Pointer to a string containing the name of the variable. This name should have a character a-z as its first character and is not case sensitive.

####  pValue

Pointer to string that contains the value the variable should be set to. 

####  Return value

Return VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while in a receive loop.



#### Example

`<code="c">`
`</code>`


## getRemoteVariableUX1

`<code="c">`
getRemoteVariableUX1( long handle, 
                                const char *pName, 
                                char *pValue, 
                                size_t len ) 
`</code>`

Get variable value from UX1 (User interface version 1) variable. The returned value is BASE64 encoded. 

####  handle

Handle for the communication channel obtained from a call to [newSession](./newsession.md).

####  pName

Pointer to a string containing the name of the variable. This name should have a character a-z as its first character and is not case sensitive.

#### pValue

Pointer to string buffer that will get the value of the date variable.

#### len

Size of string buffer.

####  Return value

Return VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while in a receive loop.



#### Example

`<code="c">`

`</code>`

## setRemoteVariableUX1

`<code="c">`
int setRemoteVariableUX1( long handle, 
                                        const char *pName, 
                                        char *pValue ) 
`</code>`

Set variable value for a UX1 (User interface version 1) variable. The value is always expected to be BASE64 encoded.

####  handle

Handle for the communication channel obtained from a call to [newSession](./newsession.md).

####  pName

Pointer to a string containing the name of the variable. This name should have a character a-z as its first character and is not case sensitive.

####  pValue

Pointer to string that contains the value the variable should be set to. 

####  Return value

Return VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while in a receive loop.



#### Example

`<code="c">`
`</code>`

## getRemoteVariableDMROW

`<code="c">`
getRemoteVariableDMROW( long handle, 
                                  const char *pName, 
                                  char *pValue, 
                                  size_t len ) 
`</code>`

Get variable value from a DM row variable. The returned value is BASE64 encoded. 

####  handle

Handle for the communication channel obtained from a call to [newSession](./newsession.md).

####  pName

Pointer to a string containing the name of the variable. This name should have a character a-z as its first character and is not case sensitive.

#### pValue

Pointer to string buffer that will get the value of the date variable.

#### len

Size of string buffer.

####  Return value

Return VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while in a receive loop.



#### Example

`<code="c">`

`</code>`

## setRemoteVariableDMROW

`<code="c">`
int setRemoteVariableDMROW( long handle, 
                                        const char *pName, 
                                        char *pValue ) 
`</code>`

Set variable value for a DM row variable. The value is always expected to be BASE64 encoded.

####  handle

Handle for the communication channel obtained from a call to [newSession](./newsession.md).

####  pName

Pointer to a string containing the name of the variable. This name should have a character a-z as its first character and is not case sensitive.

####  pValue

Pointer to string that contains the value the variable should be set to. 

####  Return value

Return VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while in a receive loop.



#### Example

`<code="c">`
`</code>`

## getRemoteVariableDriver

`<code="c">`
getRemoteVariableDriver( long handle, 
                                   const char *pName, 
                                   char *pValue, 
                                   size_t len ) 
`</code>`

Get variable value from a driver variable. The returned value is BASE64 encoded. 

####  handle

Handle for the communication channel obtained from a call to [newSession](./newsession.md).

####  pName

Pointer to a string containing the name of the variable. This name should have a character a-z as its first character and is not case sensitive.

#### pValue

Pointer to string buffer that will get the value of the date variable.

#### len

Size of string buffer.

####  Return value

Return VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while in a receive loop.



#### Example

`<code="c">`

`</code>`

## setRemoteVariableDriver

`<code="c">`
int setRemoteVariableDriver( long handle, 
                                        const char *pName, 
                                        char *pValue ) 
`</code>`

Set variable value for a driver variable. The value is always expected to be BASE64 encoded.

####  handle

Handle for the communication channel obtained from a call to [newSession](./newsession.md).

####  pName

Pointer to a string containing the name of the variable. This name should have a character a-z as its first character and is not case sensitive.

####  pValue

Pointer to string that contains the value the variable should be set to. 

####  Return value

Return VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while in a receive loop.



#### Example

`<code="c">`
`</code>`

## getRemoteVariableUser

`<code="c">`
getRemoteVariableUser( long handle, 
                                    const char *pName, 
                                    char *pValue, 
                                    size_t len ) 
`</code>`

Get variable value from a user variable. The returned value is BASE64 encoded. 

####  handle

Handle for the communication channel obtained from a call to [newSession](./newsession.md).

####  pName

Pointer to a string containing the name of the variable. This name should have a character a-z as its first character and is not case sensitive.

#### pValue

Pointer to string buffer that will get the value of the date variable.

#### len

Size of string buffer.

####  Return value

Return VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while in a receive loop.



#### Example

`<code="c">`

`</code>`

## setRemoteVariableUser

`<code="c">`
int setRemoteVariableUser( long handle, 
                                        const char *pName, 
                                        char *pValue ) 
`</code>`

Set variable value for a user variable. The value is always expected to be BASE64 encoded.

####  handle

Handle for the communication channel obtained from a call to [newSession](./newsession.md).

####  pName

Pointer to a string containing the name of the variable. This name should have a character a-z as its first character and is not case sensitive.

####  pValue

Pointer to string that contains the value the variable should be set to. 

####  Return value

Return VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while in a receive loop.



#### Example

`<code="c">`
`</code>`


## getRemoteVariableFilter

`<code="c">`
getRemoteVariableFilter( long handle, 
                                    const char *pName, 
                                    char *pValue, 
                                    size_t len ) 
`</code>`

Get variable value from a filter variable. The returned value is BASE64 encoded. 

####  handle

Handle for the communication channel obtained from a call to [newSession](./newsession.md).

####  pName

Pointer to a string containing the name of the variable. This name should have a character a-z as its first character and is not case sensitive.

#### pValue

Pointer to string buffer that will get the value of the date variable.

#### len

Size of string buffer.

####  Return value

Return VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while in a receive loop.



#### Example

`<code="c">`

`</code>`

## setRemoteVariableFilter

`<code="c">`
int setRemoteVariableFilter( long handle, 
                                        const char *pName, 
                                        char *pValue ) 
`</code>`

Set variable value for a filter variable. The value is always expected to be BASE64 encoded.

####  handle

Handle for the communication channel obtained from a call to [newSession](./newsession.md).

####  pName

Pointer to a string containing the name of the variable. This name should have a character a-z as its first character and is not case sensitive.

####  pValue

Pointer to string that contains the value the variable should be set to. 

####  Return value

Return VSCP_ERROR_SUCCESS on success, VSCP_ERROR_ERROR on failure. If the connection is closed VSCP_ERROR_CONNECTION is returned. VSCP_ERROR_PARAMETER is returned if called while in a receive loop.



#### Example

`<code="c">`
`</code>`



\\ 
----
Copyright (c) 2000-2019 [Åke Hedman](mailto/akhe@grodansparadis.com), [Paradise of the Frog / Grodans Paradis AB](https://www.grodansparadis.com)
