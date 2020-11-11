# byteArrayToPos


```python
byteArrayToPos(ba_to, pos, ba_from)
```

### Parameters

* **ba_to** - Receiving byte array
* **pos** - Position where data should be inserted
* **ba_from** - Byte array from which data is inserted


### Return Value

The resulting byte array with new data inserted.

### Description

Copy the content of a byte array into a larger byte array. Typically used to insert binary data in to a VSCP event data array.

### Example 

```python
import vscphelp as vhlp

ba1 = bytearray([0,1,2,3,4,5,6,7,8,9])
ba2 = bytearray([11,22,33])
print(len(ba1))
ba = vhlp.byteArrayToPos(ba1,3,ba2)
print([ "0x%02x" % b for b in ba ])
print([ "0x%02x" % b for b in ba1 ])
```

### See also

* [string2ByteArray](string2bytearray.md)


[filename](./bottom_copyright.md ':include')