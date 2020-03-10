
student={'john':90, 'sam':75, 'hanna':85}
try:
    print(student['john'])
    print(student['sara'])
except KeyError as e:
    print("Error for key is :",e.__str__())
    student[e.__str__()]=0
    print(student[e.__str__()])



for key, value in student.items():
    print (key, value)




x={'a':[1,2,3],'b':4, (1,2,3,4,5):[4,7,8]}
for i,j in x.items():
    print(i, "->")
    if isinstance(j, list):
        for z in j:
            print(z)
    else:
        print(j)


my_dict1={'abc':1, 'xyz':2}
print(my_dict1.get('abc', "Not found"))
print(my_dict1.get('def', "Not found"))



my_dict2={'abc':[1,2,3,4,5], 'def':"Ankit", 'pqr':6}
for i in my_dict2.keys():
    print(my_dict2[i])

for k in my_dict2.values():
    print(k)