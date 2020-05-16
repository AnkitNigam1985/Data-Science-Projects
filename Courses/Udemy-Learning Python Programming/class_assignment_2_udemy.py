class Car:
    def __init__(self, model, year):
        super().__init__()

        prius={2014:10000, 2015:12000, 2016:13000, 2017:20000, 2018:28000}
        camry={2014:13000, 2015:16000, 2016:20000, 2017:23000, 2018:28000}
        highlander={2014:15000, 2015:19000, 2016:22000, 2017:26000, 2018:32000}

        self.__year = year
        if model==1:
            self.__price = prius[year]
            self.__model = "prius"
        elif model==2:
            self.__price=camry[year]
            self.__model = "camry"
        else:
            self.__price=highlander[year]
            self.__model = "highlander"

    def __str__(self):
        return "Model {0}, Price {1}, Year {2}".format(self.__model, self.__price, self.__year)


def main():

    print("Enter the model, 1- Prius, 2 - Camry, 3 - Highlander\n")
    model=int(input())

    print("Enter the year between 2014 to 2018\n")
    year=int(input())

    my_car=Car(model, year) 
    print(my_car)


main()