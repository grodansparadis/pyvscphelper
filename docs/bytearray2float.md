

```python
byteArray2Float(ba)
```

### Parameters

* **ba** - Byte array with floating point value stored in four bytes on big-endian/network byte order

### Return Value

A floating point value.

### Description

Convert floating point value in a big endian bytearray to a floating point value

### Example 

```python
import vscphelp as vhlp

value = 3.14
ba = vhlp.float2ByteArray(value)
f = vhlp.byteArray2Float(ba)
print(f)
```

### See also

* [float2ByteArray](float2bytearray.md)
* [double2ByteArray](double2bytearray.md)
* [[byteArray2Double](bytearray2double.md)]


[filename](./bottom_copyright.md ':include')