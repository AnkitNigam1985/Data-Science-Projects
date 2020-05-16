class BankAcc:

    def __init__(self, account_type):
        self.__account_type_atr=account_type
        self.__amount_add=0

    def add_money(self, p_amount_add):
        self.__amount_add+=p_amount_add

    def show_type(self):
        return  self.__account_type_atr

    def show_amount(self):
        return self.__amount_add

    def __str__(self):
        return self.__account_type_atr +" in your account"
    
    def __repr__(self):
        return self.__account_type_atr + " in your bank account"


print("What type of account : 1 - saving, 2  - current")
actype=int(input())
if actype==1:
    account_type='Saving'
elif actype==2:
    account_type='Current'

my_account=BankAcc(account_type)

print("Add money in the account")
my_account.add_money(20)
print("Account type : ", my_account.show_type() )
print("Balance in the account : ", my_account.show_amount())
print(my_account)
