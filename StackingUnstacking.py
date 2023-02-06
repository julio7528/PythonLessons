import os
os.system('cls')

#Stacking and Unstacking
stack = []
def push(item):
    stack.append(item)
def pop():
    return stack.pop()
def isEmpty():
    return len(stack) == 0

push(1)
push(2)
push(3)

while not isEmpty():    
    print(pop())


