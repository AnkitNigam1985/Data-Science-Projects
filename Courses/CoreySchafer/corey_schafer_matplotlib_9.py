import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

ages=[18,19,21,25,26,26,30,32,38,45,55]
plt.hist(ages, bins=5, edgecolor='black')
plt.savefig('hist1.png')
plt.show()


ages = [18, 19, 21, 25, 26, 26, 30, 32, 38, 45, 55]
bins=[10,20,30,40,50,60]
plt.hist(ages, bins=bins, edgecolor='black')
plt.savefig('hist2.png')
plt.show()


df = pd.read_csv(
    "https://raw.githubusercontent.com/CoreyMSchafer/code_snippets/master/Python/Matplotlib/06-Histograms/data.csv")
print(df.head(3))

ids=df['Responder_id']
ages=df['Age']

bin=[10,20,30,40,50,60,70,80,90,100]
median_age=np.median(ages)

plt.hist(ages, bins=bin, edgecolor='black')

plt.xticks(np.arange(10,100,10), labels=bin)
plt.axvline(median_age, color='r', label='Age Median')
plt.savefig('hist3.png')
plt.show()
