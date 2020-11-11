# string2ByteArray


```python
string2ByteArray(str)
```

### Parameters

* **str** - String with that should be converted to a byte array. Typically a floating point value on string form.

### Return Value

A byte array with the individual bytes for each character in the string. A null terminating character is added at the end.

### Description

Convert a string to a bytearray and put a terminating zero at the end. Typically used for VSCP events where the data is in string form.

### Example 

```python
import vscphelp as vhlp

ba = vhlp.string2ByteArray("412.45")
print([ "0x%02x" % b for b in ba ])
```

### See also

* [byteArrayToPos](bytearray2pos.md)


[filename](./bottom_copyright.md ':include')