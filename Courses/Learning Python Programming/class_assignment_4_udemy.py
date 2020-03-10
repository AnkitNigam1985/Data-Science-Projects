class Contact:
    def __init__(self, name, phonenumber):
        self.__person_name=name
        self.__person_phone = phonenumber

    def get_name(self):
        return self.__person_name

    def get_phonenumber(self):
        return self.__person_phone

    def __str__(self):
        return "Person Name : {0}, Phonenumber : {1}".format(self.__person_name, self.__person_phone)

    def save_file(self, contact_file):
        my_file=open(contact_file, "a")
        my_file.write(self.__person_name + str(self.__person_phone) + "\n")
        my_file.close()
        print("Data saved to file")

def read_file(contact_file):
    end_of_file_error=False

    my_file=open(contact_file, "r")

    while end_of_file_error==False:
        try:
            print(my_file.readline())
        except EOFError:
            end_of_file_error=True
    my_file.close()    


def main():
    filename='Contact_list.txt'
    again='y'

    while again.lower()=='y':
        name=input("Enter the name of the Person to be added:\n")
        number = input("Enter the phone number of the Person to be added:\n")

        contobj=Contact(name, number)

        contobj.save_file(filename)

        again=input("Want to add more(y/n) : ")
    
    read_file(filename)

main()
