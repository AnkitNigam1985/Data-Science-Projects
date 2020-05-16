def main():
    student1="sam"
    student2="emma"
    student3="john"

    my_file=open("student.txt", 'w')

    my_file.write(student1+"\n")
    my_file.write(student2+"\n")
    my_file.write(student3+"\n")
    my_file.write('sarah\n')

    my_file.close()


    print("All data have been saved to the file")

main()