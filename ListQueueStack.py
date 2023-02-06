#Insert in List
def insertList(lst, index, value):
    lst.append(None)
    for i in range(len(lst)-1, index, -1):
        lst[i] = lst[i-1]
    lst[index] = value
    return lst

# lst = [1, 2, 3, 4, 5]
# lst = insertList(lst, 2, 10)
# print(lst)

#Find in list
def findList(lst, value):
    for i in range(len(lst)):
        if lst[i] == value:
            return i
    return -1

# lst = [1, 2, 3, 4, 5]

# value = findList(lst, 3)

# if value != -1:
#     print("Found at index", value)
# else:
#     print("Not found")

#Remove from List
def removeList(lst, index):
    for i in range(index, len(lst)-1):
        lst[i] = lst[i+1]
    lst.pop()
    return lst

lst = [1, 2, 3, 4, 5]
lst = removeList(lst, 2)
print(lst)

