repeat=True

while repeat==True:
    try:
        print("Enter the number")
        x=int(input())
        if (x%2==0):
            print(svss)
        else:
            print(x/0)  
    except ValueError:
        print("Enter the number in the form (1,3,4)")
    except NameError:
        print("Name Error")
    except:
        repeat=False
        print ("Wrong entry")
