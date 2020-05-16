nums=[1,2,3,4,5,6]

my_list=[n for n in nums]
print(my_list)

my_list2=[n*n for n in nums]
print(my_list2)


my_list3=[n for n in nums if n%2==0]
print(my_list3)

#Using filter+lambda
my_list4=list(filter(lambda n: n%2==0, nums))
print(my_list4)


my_list5=[(letter,num) for letter in 'abcd' for num in range(4)]
print(my_list5)

names=['Bruce','Clark','Peter','Logan','Wade']
alias=['Batman','Superman','Spiderman','Wolverne','Deadpool']
print (list(zip(names, alias)))

my_dict={name:hero for name,hero in zip(names, alias)}
print(my_dict)


nums=[1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9]
#my_set=set()
#for n in nums:
 #   my_set.add(n)
#print(my_set)

my_set={n for n in nums}
print(my_set)

#Generator function
#def gen_func(nums):
 #   for n in nums:
  #      yield n*n

#my_gen=gen_func(nums)

#for i in my_gen:
 #   print(i)

my_gen=(n*n for n in nums)
for i in my_gen:
    print(i)