import pandas as pd
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

df = pd.read_csv('Matplotlib_data_1.csv')
print(df.head())

ids=df['Responder_id']
language_responses = df['LanguagesWorkedWith']
print(ids[0:5])
print(language_responses[0:5])
    
language_counter=Counter()

for response in language_responses:
     language_counter.update(response.split(';'))


languages = []
popularity = []
print(language_counter.most_common(15))


for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

print(languages)
print(popularity)

plt.figure(figsize=(20, 8))
plt.barh(languages, popularity)
plt.xlabel("Languages")
plt.ylabel('Popularity')
plt.title('Language Popularity')

plt.savefig('figure11.png')
plt.tight_layout()
plt.show()
