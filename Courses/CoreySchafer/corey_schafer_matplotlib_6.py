from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from  collections import Counter

plt.style.use('fivethirtyeight')

slices=[120,80, 30, 20]
labels=['Sixty', 'Forty', 'Extra1', 'Extra2']
colors=['blue','red','yellow','green']

plt.pie(slices, labels=labels, wedgeprops={'edgecolor': 'black'}, colors=colors , autopct='%1.1f%%')
plt.title('My Pie chart')
plt.tight_layout()
plt.savefig('piechart_1.png')
plt.show()




df = pd.read_csv('Matplotlib_data_1.csv')
print(df.head())

ids = df['Responder_id']
language_responses = df['LanguagesWorkedWith']
print(ids[0:5])
print(language_responses[0:5])

language_counter = Counter()

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
explode=np.zeros(15)
explode[3]=0.5      #python


plt.pie(popularity, labels=languages, wedgeprops={
        'edgecolor': 'black'}, explode=explode, shadow=True)
plt.title('Pie chart for Language popularity')
plt.tight_layout()
plt.savefig('piechart_2.png')
plt.show()
