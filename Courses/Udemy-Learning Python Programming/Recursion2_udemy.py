def enter_choice():
    choice = int(input())

    if choice != 1 and choice != 2:
        print('wrong entry!!!')
        print('enter either 1 or 2')
    return choice


def batch_sum(a, b, batch_list):
    #recursive case
    if b >= a:
        return batch_list[b]+batch_sum(a, b-1, batch_list)
    #base case
    elif b < a:
        return 0


def main():
    choice = 0
    batch_list = []
    #ask from the user what to do
    while choice != 1 and choice != 2:
        print('enter the number that corresponds to your choice')
        print('1. add money batches to your account')
        print('2. transfer money batches from your account')
        choice = enter_choice()

        if choice == 1:

            print('how many batches you want to add')
            batch_num = int(input())

            #ask for each batch amount
            for i in range(batch_num):
                print('enter the', i+1, 'batch amount')
                n = int(input())
                #add the batches to the account (list)
                batch_list.append(n)
            print('all batches have been added to your account')
            print()
            #ask from user if he is willing
            #to transfer the batches
            print('would like to  transfer batches?')
            print('enter y for yes or n for no')
            again = input()

            if again.lower() == 'y':
                choice = 2
        if choice == 2:
            print('all batches between the start batch ')
            print('to the end batch will be transfered')
            print('including the start and the last batch')
            print()
            print('enter the start batch ')
            start_batch = int(input())
            print()
            print('enter the end batch ')
            last_batch = int(input())
            start_batch -= 1
            last_batch -= 1

            total = batch_sum(start_batch, last_batch, batch_list)
            print('the sum of all the transfered batches is $',
                  format(total, ',d'), sep='')


main()
