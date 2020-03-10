"""
Given a list of integers, return a new list such that each element in the new list is the product of all the numbers in the original list  except the element that in the same position of the new list element
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
"""

new_list=list()
original_list=list()

lst_size=int(input("Enter the size :\n"))
for i in range(lst_size):
    n=int(input())
    original_list.append(n)

print("Original List :", original_list)


for i in range(lst_size)