* Overview

  * [The VSCP helper library](README.md)
  * [Language Bindings](bindings.md)

* Using the library

  * [Using the library](using.md)
  * [Return values and error handling](error_handling.md)

* Functions in library

  * Initialization and configuration

    * [newSession](newsession.md)
    * [closeSession](closesession.md)
    * [setResponseTimeout](setresponsetimeout.md)
    * [setAfterCommandSleep](setaftercommandsleep.md)

  * Tcp/ip communication link methods

    * [isConnected](isconnected.md)
    * [doCommand](docommand.md)
    * [checkReply](checkreply.md)
    * [clearLocalInputQueue](clearlocalinputqueue.md)
    * [open](open.md)
    * [openInterface](openinterface.md)
    * [close](close.md)
    * [noop](noop.md)
    * [clearDaemonEventQueue](cleardaemoneventqueue.md)
    * [sendEvent](sendevent.md)
    * [sendEventEx](sendeventex.md)
    * [isDataAvailable](isdataavailable.md)
    * [enterReceiveLoop](enterreceiveloop.md)
    * [quitReceiveLoop](quitreceiveloop.md)
    * [blockingReceiveEvent](blockingreceiveevent.md)
    * [blockingReceiveEventEx](blockingreceiveeventex.md)
    * [setFilter](setfilter.md)
    * [getStatistics](getstatistics.md)
    * [getStatus](getstatus.md)
    * [getVersion](getversion.md)
    * [getDLLVersion](getdllversion.md)
    * [getVendorString](getvendorstring.md)
    * [getDriverInfo](getdriverinfo.md)
    * [doCmdShutDown](docmdshutdown.md)

  * GUID handling

    * [getGuidFromString](getguidfromstring.md)
    * [getGuidFromStringEx](getguidfromstringex.md)
    * [getGuidFromStringToArray](getguidfromstringtoarray.md)
    * [writeGuidToString](writeguidtostring.md)
    * [writeGuidToStringEx](writeguidtostringex.md)
    * [writeGuidToString4Rows](writeguidtostring4rows.md)
    * [writeGuidToString4RowsEx](writeguidtostring4rowsex.md)
    * [writeGuidArrayToString](writeguidarraytostring.md)
    * [isGUIDEmpty](isguidempty.md)
    * [isSameGUID](issameguid.md)
    * [reverseGUID](reverseguid.md)
    * [calcCRC4GUIDArray](calccrc4guidarray.md)
    * [calcCRC4GUIDString](calccrc4guidstring.md)

  * Filter handling

    * [clearVSCPFilter](clearvscpfilter.md)
    * [copyVSCPFilter](copyvscpFilter.md)
    * [readFilterFromString](readfilterfromstring.md)
    * [writeFilterToString](writefiltertostring.md)
    * [readMaskFromString](readmaskfromstring.md)
    * [writeMaskToString](writemasktostring.md)
    * [doLevel2Filter](doLevel2filter.md)

  * Event helpers and conversions

    * [copyVSCPEvent](copyvscpevent.md)
    * [getVscpPriority](getvscppriority.md)
    * [getVscpPriorityEx](getvscppriorityex.md)
    * [setVscpPriority](setvscppriority.md)
    * [setVscpPriorityEx](setvscppriorityex.md)
    * [convertVSCPtoEx](convertvscptoex.md)
    * [convertVSCPfromEx](convertvscpfromex.md)
    * [newVSCPevent](newvscpevent.md)
    * [deleteVSCPevent](deletevscpevent.md)
    * [deleteVSCPevent_v2](deletevscpevent_v2.md)
   
    * VSCP data

      * [writeVscpDataToString](writevscpdatatostring.md)
      * [writeVscpDataWithSizeToString](writevscpdatawithsizetostring.md)
      * [setVscpDataFromString](setvscpdatafromstring)
   
    * CANAL conversions

      * [convertCanalToEvent](convertcanaltoevent.md)
      * [convertCanalToEventEx](convertcanaltoeventex.md)
      * [convertEventToCanal](converteventtocanal.md)
      * [convertEventExToCanal](converteventextocanal.md)

    * Date/Time

      * [setEventDateTimeBlockToNow](seteventdatetimeblocktonow.md)
      * [setEventExDateTimeBlockToNow](seteventexdatetimeblocktonow.md)
  
    * String

      * [writeVscpEventToString](writevscpeventtostring.md)
      * [writeVscpEventExToString](writevscpeventextostring.md)
      * [setVscpEventFromString](setvscpeventfromstring.md)
      * [setVscpEventExFromString](setvscpeventexfromstring.md)
      * [getDateStringFromEvent](getdatestringfromevent.md)
      * [getDateStringFromEventEx](getdatestringfromeventex.md) 
      * [convertStringToEvent](convertStringToEvent.md)
      * [convertStringToEventEx](convertStringToEventEx.md)

    * JSON

      * [convertEventToJSON](converteventtojson.md)
      * [convertEventExToJSON](converteventextojson.md)
   
    * XML

      * [convertEventToXML](converteventtoxml.md)
      * [convertEventExToXML](converteventextoxml.md)

    * HTML

      * [convertEventToHTML](converteventtohtml.md)
      * [convertEventExToHTML](converteventextohtml.md)

  * CANAL helpers and conversions

    * [getVSCPheadFromCANALid](getvscpheadfromcanalid.md)
    * [getVSCPclassFromCANALid](getvscpclassfromcanalid.md)
    * [getVSCPtypeFromCANALid](getvscptypefromcanalid.md)
    * [getVSCPnicknameFromCANALid](getvscpnicknamefromcanalid.md)
    * [getCANALidFromVSCPdata](getcanalidfromvscpdata.md)
    * [getCANALidFromVSCPevent](getcanalidfromvscpevent.md)
    * [getCANALidFromVSCPeventEx](getcanalidfromvscpeventex.md)
    * [calc_crc_Event](calc_crc_event.md)
    * [calc_crc_EventEx](calc_crc_eventex.md)

    * Conversions

      * [convertCanalToEvent](convertcanaltoevent.md)
      * [convertCanalToEventEx](convertcanaltoeventex.md)
      * [convertEventToCanal](converteventtocanal.md)
      * [convertEventExToCanal](converteventextocanal.md)

  * Measurements

    * [getMeasurementDataCoding](getmeasurementdatacoding.md)
    * [getDataCodingBitArray](getdatacodingbitarray.md)
    * [getDataCodingInteger](getdatacodinginteger.md)
    * [getDataCodingNormalizedInteger](getdatacodingnormalizedinteger.md)
    * [getDataCodingString](getdatacodingstring.md)
    * [getVSCPMeasurementAsString](getvscpmeasurementasstring.md)
    * [getVSCPMeasurementAsDouble](getvscpmeasurementasdouble.md)
    * [getVSCPMeasurementFloat64AsString](getvscpmeasurementfloat64asstring.md)
    * [convertFloatToNormalizedEventData](convertfloattonormalizedeventdata.md)
    * [convertFloatToFloatEventData](convertfloattofloateventdata.md)
    * [convertIntegerToNormalizedEventData](convertintegertonormalizedeventdata.md)
    * [makeFloatMeasurementEvent](makefloatmeasurementevent.md)
    * [getMeasurementAsFloat](getmeasurementasfloat.md)
    * [getMeasurementUnit](getmeasurementunit.md)
    * [getMeasurementSensorIndex](getmeasurementsensorindex.md)
    * [getMeasurementZone](getmeasurementzone.md)
    * [getMeasurementSubZone](getmeasurementSubzone.md)
    * [isMeasurement](ismeasurement.md)
    * [convertLevel1MeasuremenToLevel2Double](convertlevel1measurementolevel2double.md)
    * [convertLevel1MeasuremenToLevel2String](convertlevel1measurementolevel2string.md)
    * [makeLevel2FloatMeasurementEvent](makelevel2floatmeasurementevent.md)
    * [makeLevel2StringMeasurementEvent](makelevel2stringmeasurementevent.md)

  * General helpers

    * [readStringValue](readstringvalue.md)
    * [replaceBackslash](replacebackslash.md)
    * [getTimeString](gettimestring.md)
    * [getISOTimeString](getisotimestring.md)
    * [convertCanalToEvent](convertcanaltoevent.md)
    * [convertCanalToEventEx](convertcanaltoeventex.md)
    * [convertEventToCanal](converteventtocanal.md)
    * [convertEventExToCanal](converteventextocanal.md)
    * [makeTimeStamp](maketimestamp.md)
   
  * Python specific helpers

    * [float2ByteArray](float2bytearray.md)
    * [double2ByteArray](double2bytearray.md)
    * [byteArray2Float](bytearray2float.md)
    * [byteArray2Double](bytearray2double.md)
    * [string2ByteArray](string2bytearray.md)
    * [byteArrayToPos](bytearray2pos.md)

  * Encryption and Password handling
  
    * [getEncryptionTokenFromCode](getEncryptionTokenFromCode.md)
    * [getEncryptionFrameSizeFromEvent](getEncryptionFrameSizeFromEvent.md)
    * [getEncryptionFrameSizeFromEventEx](getEncryptionFrameSizeFromEventEx.md)
    * [writeEventToEncryptionFrame](writeEventToEncryptionFrame.md)
    * [writeEventExToEncryptionFrame](writeEventExToEncryptionFrame.md)
    * [getEventFromEncryptionFrame](getEventFromEncryptionFrame.md)
    * [getEventExFromEncryptionFrame](getEventExFromEncryptionFrame.md)
    * [encryptFrame](encryptFrame.md)
    * [decryptFrame](decryptFrame.md)
    * [md5](vscphlphlp_md5.md)
    * [byteArray2HexStr](byteArray2HexStr.md)
    * [hexStr2ByteArray](hexStr2ByteArray.md)
    * [getHashPasswordComponents](getHashPasswordComponents.md)
    * [makePasswordHash](makePasswordHash.md)
    * [isPasswordValid](isPasswordValid.md)
    * [getSalt](getSalt.md)
    * [getSaltHex](getSaltHex.md)

* Other documentation
  * [VSCP documentation portal](https://docs.vscp.org)





