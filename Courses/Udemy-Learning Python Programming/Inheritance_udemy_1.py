class Car:
    def __init__(self, p_make, p_mileage):
        self.__make=p_make
        self.__mileage=p_mileage

    def get_make(self):
        return self.__make

    def get_mileage(self):
        return self.__mileage

    def __str__(self):
        return super().__str__()

class Toyota(Car):

    def __init__(self, p_make, p_mileage, p_model, p_price):
        Car.__init__(self, p_make, p_mileage)
        self.__model=p_model
        self.__price=p_price
        self.__company='Toyota'

    def get_car_info(self):
        print("Company : ", self.__company)
        print("Model : ", self.__model)
        print("Make : ", super().get_make())
        print("Mileage : ", super().get_mileage())
        print("Price : ", self.__price)

class Maruti(Car):
    
    def __init__(self, p_make, p_mileage, p_model, p_price):
        Car.__init__(self, p_make, p_mileage)
        self.__model=p_model
        self.__price=p_price
        self.__company='Maruti'

    def get_car_info(self):
        print("Company : ", self.__company)
        print("Model : ", self.__model)
        print("Make : ", super().get_make())
        print("Mileage : ", super().get_mileage())
        print("Price : ", self.__price)

def main():
    p_mileage=int(input("Enter the mileage :\n"))
    p_make=int(input("Enter the make :\n"))
    p_model=input("Enter the model :\n")
    p_price=int(input("Enter the price :\n"))

    used_toyota = Toyota(p_make, p_mileage, p_model, p_price)

    p_mileage = int(input("Enter the mileage :\n"))
    p_make = int(input("Enter the make :\n"))
    p_model = input("Enter the model :\n")
    p_price = int(input("Enter the price :\n"))

    used_maruti = Maruti(p_make, p_mileage, p_model, p_price)

    used_toyota.get_car_info()
    used_maruti.get_car_info()

main()
