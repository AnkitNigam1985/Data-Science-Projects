def main():
    my_file=open('student.txt','r')
    line1=my_file.readline()
    line2=my_file.readline()
    line3 = my_file.readline()

    my_file.close()


    line1=line1.rstrip("\n")
    line2=line1.rstrip("\n")
    line3 = line1.rstrip("\n")
    print('The data have been retrieved')
    print('Here is list of data')
    print(line1)
    print(line2)
    print(line3)

main()
