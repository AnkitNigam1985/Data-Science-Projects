with open('test.txt', 'w') as f:
    f.write('Ankit\n')
    f.write('Nigam\n')
    f.write('Rohini\n')
    f.write('Delhi\n')

with open('test.txt', 'r') as f:
    print(f.readlines())
    f.seek(0)
    print(f.readlines())