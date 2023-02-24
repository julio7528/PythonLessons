# def factorial(n):
#     if n == 0:
#         print(n)
#         return 1
#     else:
#         print(n * factorial(n-1))
#         return n * factorial(n-1)

# factorial(1)

def nested_list_sum(nested_list):
    total_sum = 0
    for item in nested_list:
        if isinstance(item, list):
            total_sum += nested_list_sum(item)  # recursive call for nested list
            print(total_sum)
        else:
            total_sum += item
            print(total_sum)
    return total_sum

nested_list_sum([1, 2, 3])