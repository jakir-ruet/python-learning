myFile = open("data.txt", "r")
textShow = myFile.read()
print(textShow)
textShowByte = myFile.read(5) # here 5 means read the 5 byte
print(textShowByte)
textShowLine = myFile.readline() # read the a line
print(textShowLine)