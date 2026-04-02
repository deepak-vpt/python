def findlist(lst, num):
    if num in lst:
        return f"{num} is present in the list."
    else:
        return f"{num} is not in the list."

# Example
my_list = [1, 2, 3, 4, 5]
number = 3
print(findlist(my_list, number))
