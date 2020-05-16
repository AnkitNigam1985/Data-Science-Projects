import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


df = pd.read_csv(
    "https://raw.githubusercontent.com/CoreyMSchafer/code_snippets/master/Python/Matplotlib/05-Fill_Betweens/data.csv")
print(df.head())

ages=df['Age']
dev_salaries=df['All_Devs']
python_salaries=df['Python']
java_salaries=df['JavaScript']

overall_median=57287

plt.plot(ages, dev_salaries, color='r', linestyle='--', label='All Devs')
plt.plot(ages, python_salaries, color='g', linestyle='-.', label='Python Devs')
plt.plot(ages, java_salaries, color='b', linestyle=':', label='JavaScript Devs')
plt.fill_between(ages, python_salaries, y2=overall_median, where=(python_salaries > overall_median), interpolate=True, alpha=0.10)
plt.fill_between(ages, python_salaries, y2=overall_median, where=(
    python_salaries < overall_median), interpolate=True, alpha=0.10)
plt.title('Median Salary of Developers')
plt.savefig('linereafig.png')
plt.legend()
plt.show()


plt.plot(ages, dev_salaries, color='r', linestyle='--', label='All Devs')
plt.plot(ages, python_salaries, color='g', linestyle='-.', label='Python Devs')
plt.plot(ages, java_salaries, color='b',
         linestyle=':', label='JavaScript Devs')
plt.fill_between(ages, python_salaries, y2=overall_median, where=(
    python_salaries > overall_median), interpolate=True, alpha=0.10)
plt.fill_between(ages, dev_salaries, y2=overall_median, where=(
    python_salaries < dev_salaries), interpolate=True, alpha=0.10)
plt.title('Median Salary of Developers')
plt.savefig('linereafig1.png')
plt.legend()
plt.show()
