"""
You have array of integers, find the first missing positive integer (find the lowest positive integer that does not exist in the array). The array can contain duplicates and negative numbers as well.
For example, the input [9, 5, -2, 1] should give 2. The input [1, 2, 3] should give 4.
You can modify the input array in-place.
"""

print('how many item in the list')
lst_size = int(input())
lst = []

for i in range(lst_size):
    num = int(input('enter the '+str(i+1)+' item: '))
    lst.append(num)

lst.sort()

print(lst)
end = 1
for i in range(lst_size):
    if end == 0:
        break
    if lst[i] >= 0:
        a = lst[i]+1

        for j in range(i+1, lst_size):
            if lst[j] == a:
                a += 1
                continue
            else:
                print('the first missing positive integer is', a)
                end = 0
                break
