import array
a = array.array('i',[10,20,30,40,50])

print("Original array:",a.tolist())

a.append(122)
print("After append : ",a)

a.insert(1,13)
print("After inserting in an array : ",a)

a.remove(20)
print("After removal : ",a)

a.pop()
print("After pop: ",a)

print("Index of 40",a.index(40))

print("Count elements :",a.count(20))

a.reverse()
print("After reverse: ",a)

a.extend([89,99])
print('After extendeing : ',a)

print("Array as list : ",a.tolist())

print("Buffer Information : ", a.buffer_info())