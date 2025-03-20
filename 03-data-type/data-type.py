# not changeable/immutable
MyBytes = [1, 2, 3, 4, 6, 7, 8, 9]
BytesVar = bytes(MyBytes)
print(type(BytesVar))

# changeable/mutable
MyBytesArray = [2, 1, 3, 5, 6, 7, 9, 8]
BytesArrayVar = bytearray(MyBytesArray)
print(type(BytesArrayVar))

BytesArrayVar[1] = 250
print(BytesArrayVar[1])