def gcd(x,y):
    if x%y==0:
        return(y) 
    else:
        return (gcd(y,x%y))
        
        
num1=int(input('enter an integer '))
num2=int(input('enter another integer '))

print('gcd for them is ',gcd(num1,num2))
