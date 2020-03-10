my_set1=set('abc')
print(my_set1)
print(len(my_set1))

my_set2 = set([1,2,4,'abc'])
print(my_set2)
print(len(my_set2))


my_set2.add(27)
print(my_set2)

my_set2.add(27)
print(my_set2)


#my_set2.update(5)
#print(my_set2)

my_set2.update([1,3,4,5,7,8,9])
print(my_set2)


#my_set1.remove(5)

my_set2.discard(12)


x=my_set1.union(my_set2)
print(x)