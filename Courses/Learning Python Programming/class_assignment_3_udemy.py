class Fruit:
    def __init__(self, name, price):
        self.__fruit_name=name
        self.__fruit_price=price

    def get_name(self):
        return self.__fruit_name

    def get_price(self):
        return self.__fruit_price

    def __str__(self):
        return "Fruit Name : {0}, Price : {1}".format(self.__fruit_name, self.__fruit_price)

def fruit_price():
    return int(input("Enter the price :\n"))


def main():
    my_list=list()
    again='y'

    while again.lower()=='y':
        name=input("Enter the name of the fruit need to be added in the basket:\n")
        price=fruit_price()

        fruit_object=Fruit(name, price)

        my_list.append(fruit_object)

        again=input("Want to add more(y/n) : ")
    
    for fruit in my_list:
        print(fruit)

main()