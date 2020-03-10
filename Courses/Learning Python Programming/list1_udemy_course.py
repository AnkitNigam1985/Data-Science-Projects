my_list1=[1,2,3,4,'ab',"data"]
my_list2=list()
my_list3=list(range(10))
my_list4=list('4')


print(my_list1)
print(my_list2)
print(my_list3)
print(my_list4)


print(my_list3[-4])
print(len(my_list1))

for i in my_list1:
    print(i)


num_days=int(input("Enter number of days:"))
#sales_list=[0]*num_days
sales_list =list()

for i in range(num_days):
    print('Enter the sales for day', i+1)
    s=int(input())
    sales_list.append(s)


print("Sales :", sales_list)