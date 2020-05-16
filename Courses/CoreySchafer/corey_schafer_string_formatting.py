for i in range(1,11):
    sentence='The value is {:03}'.format(i)
    print(sentence)

pi=3.14159265

sentence='Pi is equal to {:.4f}'.format(pi)
print(sentence)

sentence='1 MB is equal to {:,} bytes'.format(1000**2)
print(sentence)

sentence = '1 MB is equal to {:,.2f} bytes'.format(1000**2)
print(sentence)
