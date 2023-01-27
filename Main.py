from RefineCalculations import calcAll

name = input("Enter your name: ")
x = input(f"Hello {name},  Enter a number: ")
y = input(f"Ok {name} Enter another number: ")

result = calcAll(x,y)
print(result)
