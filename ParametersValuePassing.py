# #Parameters and Value Passing
# def add_numbers(a, b):
#     return a + b

# result = add_numbers(1, 2)
# print(result)

# #Value passing
# def update_list(lst):
#     lst[0] = 'First Value'

# orginal_list = ['First', 'Second', 'Third']

# update_list(orginal_list)
# print(orginal_list)

# #Local Variables

# def printMessage():
#     message = "Hello World!"
#     print(message)

# try:
#     printMessage()
#     print(message)
# except NameError as e:
#     print("Error: " + str(e))

# #Global Variables
# message = "Hello World!"

# def printMessage():
#     global message
#     print(message)

# printMessage()

#Formal Parameters
def add_numbers(a, b):
    return a + b

returnValue = add_numbers(1, 2)
print(returnValue)










# #Global Variables
# message = "Hello World!"
# def greet():
#   print(message)
  
# greet()
# print(message)

# #Formal Parameters
# def greet(message):
#   print(message)
  
# greet("Hello World!") # Prints "Hello World!"