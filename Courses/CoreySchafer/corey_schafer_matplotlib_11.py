import pandas as pd
from datetime import datetime,timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

plt.style.use('seaborn')
dates=[

    datetime(2019, 5, 24),
    datetime(2019, 5, 25),
    datetime(2019, 5, 26),
    datetime(2019, 5, 27),
    datetime(2019, 5, 28),
    datetime(2019, 5, 29),
    datetime(2019, 5, 30)
]
y=[0,1,3,4,6,5,7]

plt.plot_date(dates, y)
plt.tight_layout()
plt.savefig('dateplot1.png')
plt.show()

plt.plot_date(dates, y, linestyle='solid')
plt.tight_layout()
plt.savefig('dateplot2.png')
plt.show()


plt.plot_date(dates, y, linestyle='solid')
plt.gcf().autofmt_xdate()
plt.tight_layout()
plt.savefig('dateplot3.png')
plt.show()


date_format=mpl_dates.DateFormatter('%b, %d %Y')
plt.gca().xaxis.set_major_formatter(date_format)
plt.plot_date(dates, y, linestyle='solid')
plt.gcf().autofmt_xdate()
plt.tight_layout()
plt.savefig('dateplot4.png')
plt.show()


df = pd.read_csv(
    "https://raw.githubusercontent.com/CoreyMSchafer/code_snippets/master/Python/Matplotlib/08-TimeSeries/data.csv")
print(df.head(2))
df['Date']=pd.to_datetime(df['Date'])
df.sort_values('Date', inplace=True)

price_date=df['Date']
price_close=df['Close']

plt.plot_date(price_date, price_close, linestyle='solid')
plt.gcf().autofmt_xdate()
plt.tight_layout()
plt.savefig('dateplot5.png')
plt.show()
