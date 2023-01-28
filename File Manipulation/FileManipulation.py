file = "C:\\Users\\julio\\Desktop\\Data Structure\\PythonLessons\\File Manipulation\\example.txt"
mode = 'r'

f = open(file, mode)

line = f.readline()
position = f.tell()
print(position)

line = f.readline()
print(line)

f.close()

f = open(file, mode)

line = f.readline()
f.seek(4,0)
line = f.readline()
print(line)

f.close()

f = open(file, "a")
f.write("\nThis is a new line")
f.close()

f = open(file, mode)

lines = f.readlines()
for line in lines:
    print(line)
    
f.close

charByte = f.read(20)
print("The 20 first characters are")
print(charByte)

print("The entire file is")
print(f.read())

f.seek(0)
firstLine = f.readline()
print("The first line is")
print(firstLine)

secondLine = f.readline()
print("The second line is")
print(secondLine)


f.close()