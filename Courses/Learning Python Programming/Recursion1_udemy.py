def get_factorial(number):
    if number==0 or number==1:
        return 1
    
    return number*get_factorial(number-1)


def main():

    print(get_factorial(4))

main()