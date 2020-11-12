

```python
double2ByteArray(val)
```

### Parameters

* **val** - A floating point value

### Return Value

A byte array that consist of the four bytes of the floating point value in big-endian/network byte order.

### Description

Convert floating point value to byte array (four bytes). Note that VSCP stores and transfer everything MSB first. This translation is
done by the function if needed, that is the target machine is a little-endian machine.

### Example 

```python
import vscphelp as vhlp

ba = vhlp.double2ByteArray(value)
print([ "0x%02x" % b for b in ba ])
assert ba[0] == 0x40
assert ba[1] == 0x09
assert ba[2] == 0x1e
assert ba[3] == 0xb8
assert ba[4] == 0x51
assert ba[5] == 0xeb
assert ba[6] == 0x85
assert ba[7] == 0x1f
```

### See also
 * [float2ByteArray](float2bytearray.md)
 * [[byteArray2Float](bytearray2float.md)]
 * [[byteArray2Double](bytearray2double.md)]



[filename](./bottom_copyright.md ':include')