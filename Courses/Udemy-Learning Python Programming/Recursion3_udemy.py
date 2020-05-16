my_fibonacci = [0]*8
print('the first 8 fibonacci numebers is:')

for i in range(8):
    if i == 0:
        my_fibonacci[i] = 1
    elif i == 1:
        my_fibonacci[i] = 1
    else:
        my_fibonacci[i] = my_fibonacci[i-1]+my_fibonacci[i-2]
    print(my_fibonacci[i])


def fib(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        return (fib(n-1)+fib(n-2))


def main():
    print('the first 8 numbers in fibonacci is')
    for i in range(8):
        print(fib(i))


main()
