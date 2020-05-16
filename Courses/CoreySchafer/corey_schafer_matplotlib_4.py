import csv
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

with open('Matplotlib_data_1.csv') as csv_data:
    csv_reader=csv.DictReader(csv_data)

    language_counter=Counter()

    for row in csv_reader:
        language_counter.update(row['LanguagesWorkedWith'].split(';'))
    #row=next(csv_reader)
    #print(row)
    #print(row['LanguagesWorkedWith'].split(';'))

languages=[]
popularity=[]
print(language_counter.most_common(15))

for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

print(languages)
print(popularity)

plt.figure(figsize=(20,8))
plt.barh(languages, popularity)
plt.xlabel("Languages")
plt.ylabel('Popularity')
plt.title('Language Popularity')

plt.savefig('figure11.png')
plt.tight_layout()
plt.show()