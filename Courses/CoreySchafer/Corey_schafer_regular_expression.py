import re

print("\tTAB")      #normal string
print(r"\tTAB")     #raw string


text_to_search='''
abcdefghijklpqnrpmdpamfpofjpsdjf
abc89000
ABCDEFGHJIKLNMBVGSHJDHFIEDFIDJDCJFJF
12345678890

Ha HAHAHAHAHHAHAH

Metacharacters need to be escaped :
. ^ $ * + ? { } [ ] \ | ( )
ankit082006@gmail.com
'''
pattern=re.compile(r'abc')
matches=pattern.finditer(text_to_search)

print(pattern)
for k in matches:
    print(k)

pattern = re.compile(r'ankit082006\@gmail\.com')
matches = pattern.finditer(text_to_search)

print(pattern)
for k in matches:
    print(k)

"""
\d matches digit (0-9)
"""
pattern = re.compile(r'\d')
matches = pattern.finditer(text_to_search)

print(pattern)
for k in matches:
    print(k)

"""
\D matches not a digit (0-9)
"""
pattern = re.compile(r'\D')
matches = pattern.finditer(text_to_search)

print(pattern)
for k in matches:
    print(k)

"""
\w matches word case character(upper & lower) and number
"""
pattern = re.compile(r'\w')
matches = pattern.finditer(text_to_search)

print(pattern)
for k in matches:
    print(k)


"""
\s matches spaces and tabs
"""
pattern = re.compile(r'\s')
matches = pattern.finditer(text_to_search)

print(pattern)
for k in matches:
    print(k)

"""
\b matches word boundary
"""
pattern = re.compile(r'\bHa')
matches = pattern.finditer(text_to_search)

print(pattern)
for k in matches:
    print(k)

"""
\d\d\d - matches 3 continuos digits
"""
sentence="Ha ha ha  12bgn 54iioo, 123-56767-9250985025 133-345-789  567.890.567"

pattern = re.compile(r'\d\d\d')
matches = pattern.finditer(sentence)

print(pattern)
for k in matches:
    print(k)

pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d')
matches = pattern.finditer(sentence)

print(pattern)
for k in matches:
    print(k)


pattern = re.compile(r'\d{3}\d{3}')  #only numeric
matches = pattern.finditer(sentence)

print(pattern)
for k in matches:
    print(k)

sentence="Mr. Ankit Nigam   Mr XXX,  Mr. VBVBB"
pattern = re.compile(r'Mr\.?\s[A-Z]')  # only numeric
matches = pattern.finditer(sentence)

print(pattern)
for k in matches:
    print(k)

#Email search
sentence="ajfpsjhfwpjgfpwjgpwhgwe0rhg ankit082006@gmail.com   bnhmhg@hotmail.com"
pattern = re.compile(r'[a-zA-Z0-9]+@[a-zA-Z]+\.[a-zA-Z]{3}')  # only email
matches = pattern.finditer(sentence)

print(pattern)
for k in matches:
    print(k)
