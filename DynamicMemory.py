listVar = [1,2,3,4,5]
listHeterous = [1,2,3,4,5, "Hello", True, 3.14]
newList = listVar

del listVar

anotherList = newList
anotherList.append(6)

print(id(newList))
print(id(anotherList))



