import pickle

def add_data(student, keydata, valdata):
    if keydata not in student.keys():
        student[keydata]=valdata
    else:
        print("Already present :", keydata,"->", valdata)

def print_data(student):
    for key, value in student.items():
        print(key, " -> ", value)

def main():
    student=dict()

    again='y'

    while again.lower()=='y':
        choice=int(input("Enter the choice - 1 :add, 2 : print\n"))

        if choice==1:
            student_name=input("Enter the student name:")
            student_marks=int(input("Enter the student marks:"))
            add_data(student, student_name, student_marks)
            my_file=open("student_data.dat","wb")
            pickle.dump(student, my_file)
            my_file.close()
        elif choice==2:
            st=dict()
            my_file = open("student_data.dat", "rb")
            end_of_file=False
            while end_of_file==False:
                try:
                    st=pickle.load(my_file)
                except EOFError:
                    end_of_file=True
            my_file.close()
            print(st)            
        else:
            print("Invalid choice")
        
        again = input("Want to continue:(y/n):")


main()

