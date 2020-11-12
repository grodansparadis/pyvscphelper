# Document History

*  2017-05-08 AKHE writeVscpDataWithSizeToString added

*  2017-05-08 AKHE setRemoteVariableValue - synonym for setRemoteVariableString getRemoteVariableValue - synonym for getRemoteVariableString added

*  2017-05-08 AKHE All methods with buffer size now have the size in unit **size_t** Methods that did not have a size have it added. 

	
	writeVscpDataToString*
	getVendorString*
	getDriverInfo*
	getRemoteVariableString* 
	getRemoteVariableGUIDString* Added len
	getRemoteVariableDateTime*
	getRemoteVariableDate*
	getRemoteVariableTime*
	getRemoteVariableBlob*
	getRemoteVariableMIME*
	getRemoteVariableHTML*
	getRemoteVariableJavaScript*
	getRemoteVariableLUA*
	getRemoteVariableLUARES*
	getRemoteVariableUX1*
	getRemoteVariableDMROW*
	getRemoteVariableDriver*
	getRemoteVariableUser*
	getRemoteVariableFilter*
	writeGuidToString* + len
	writeGuidToStringEx* + len
	writeGuidToString4Rows*
	writeGuidToString4RowsEx*
	writeGuidArrayToString*
	writeVscpEventToString*
	writeVscpEventExToString*
	getDataCodingString*
	getVSCPMeasurementAsString*
	getVSCPMeasurementFloat64AsString*
	convertEventToJSON*
	convertEventExToJSON*
	convertEventToXML*
	convertEventExToXML*
	convertEventToHTML*
	convertEventExToHTML*



*  2017-04-18 AKHE Added **getTimeString**, **getISOTimeString**, **getDateStringFromEvent**, and **getDateStringFromEventEx** 

*  2017-04-18 AKHE Changed names for **setEventDateTimeBlock** and **setEventDateTimeBlockEx** to **setEventDateTimeBlockToNow** and **setEventExDateTimeBlockToNow**.

*  2017-04-13 AKHE Added **setEventDateTimeBlock** and **setEventDateTimeBlockEx** to set new date/time blocks in events.

*  2017-03-10 AKHE Added missing getters/setter for variables **getRemoteVariableVSCPTimestamp, setRemoteVariableVSCPTimestamp, getRemoteVariableDateTime, setRemoteVariableDateTime, getRemoteVariableDate,setRemoteVariableDate, getRemoteVariableTime, setRemoteVariableTime,getRemoteVariableBlob, setRemoteVariableBlob, getRemoteVariableMIME, setRemoteVariableMIME, getRemoteVariableHTML, setRemoteVariableHTML, getRemoteVariableJavaScript, setRemoteVariableJavaScript, getRemoteVariableLUA, setRemoteVariableLUA, getRemoteVariableLUARES, setRemoteVariableLUARES, getRemoteVariableUX1, setRemoteVariableUX1, getRemoteVariableDMROW, setRemoteVariableDMROW
getRemoteVariableDriver, setRemoteVariableDriver, getRemoteVariableUser
setRemoteVariableUser, getRemoteVariableFilter, setRemoteVariableFilter**

*  2017-03-08 AKHE Added **newVSCPevent**

*  2017-03-08 AKHE Added **deleteVSCPevent_v2**

*  2017-03-08 AKHE From version 2 names has been changed to **xxxxRemoteVariable** instead of **xxxxVariable**

*  2017-03-07 AKHE **setVariableMeasurement** / **getVariableMeasurement** had wrong parameters.

*  2017-01-31 AKHE Added makeLevel2FloatMeasurementEvent and makeLevel2StringMeasurementEvent

*  2017-01-30 AKHE Added convertLevel1MeasuremenToLevel2Double and convertLevel1MeasuremenToLevel2String

*  2017-01-28 AKHE copyVSCPFilter added.

*  2017-01-23 AKHE - Added convertEventToJSON, convertEventExToJSON, convertEventToXML, convertEventExToXML, convertEventToHTML, convertEventExToHTML

*  2017-01-12 AKHE - Added getMeasurementSensorIndex, getMeasurementZone and getMeasurementSubZone

*  2017-01-10 AKHE - Added getMeasurementUnit and isMeasurement

*  2016-10-27 AKHE - Added info about filter string read/write methods. 

*  2015-09-24 AKHE - setResponseTimeout has timeout value changed to millseconds instead of seconds.

*  2015-09-19 AKHE - Added setAfterCommandSleep. Bumped version to 4

*  2015-09-09 AKHE - The string parameter for [readFilterFromString] and [[https://www.vscp.org/docs/vscphelper/doku.php?id=helper_lib_api_helpers#readmaskfromstring](https://www.vscp.org/docs/vscphelper/doku.php?id=helper_lib_api_helpers#readfilterfromstring) can now be empty or just have some of the arguments defined. 


