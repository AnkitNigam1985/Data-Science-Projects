"""
You Given a list of numbers, you also given another number named (K), create a function which returns true wehenever any two numbers from the list add up to k.
For example, if you given [10, 9,8 , 7] and k of 16, return true since 9 + 7 is 16. 
[1,4,6] and k = 18, return False, because no such two number that their sum equals 18
"""

def check_list(my_list, k, n):
    if len(my_list)<2:
        return ("Need list of atleast 2 numbers")
    j=0
    if n==len(my_list):
        return False
    for i in range(n+1, len(my_list)):
        if my_list[n]+my_list[i]==k:
            j=1
            break
    if j==1:
        return True
    
    return check_list(my_list, k, n+1)

def main():
    k=int(input("Enter the number k : "))
    again='y'
    my_list=list()

    while again=='y':
        print("Enter the number")
        n=int(input())
        my_list.append(n)
        print("Need to add more?")
        again=input()
    print("The list is : ", my_list)
    print("The number is k :", k)
    print(check_list(my_list, k, 0))

main()