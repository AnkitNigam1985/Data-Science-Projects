class Animal:
    def show_info(self):
        print("This is regular Animal")

class Cat(Animal):
    def show_info(self):
        print("This is a Cat")


class Dog(Animal):
    def show_info(self):
        print("This is a Dog")


def main():
    my_animal=Animal()
    my_cat=Cat()
    my_dog=Dog()

    my_animal.show_info()
    my_cat.show_info()
    my_dog.show_info()

main()