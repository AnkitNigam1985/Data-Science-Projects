import datetime
import pytz 

tday=datetime.date.today()
print(tday)
print(tday.day)
print(tday.weekday())
print(tday.isoweekday())

tdelta=datetime.timedelta(days=7)

print(tday+tdelta)
print(tday-tday)

bday=datetime.date(2020, 9, 8)
till_bday=bday-tday
print(till_bday)




t=datetime.time(9, 30, 45, 40)
print(t)
print(t.hour)
print(t.minute)

dt=datetime.datetime(2020, 9, 8, 21, 30, 45, 40)
tdelta=datetime.timedelta(days=7)
print(dt+tdelta)

dt_today=datetime.datetime.today()
dt_now=datetime.datetime.now()
dt_utcnow=datetime.datetime.utcnow()

print(dt_today, dt_now, dt_utcnow)

dt = datetime.datetime(2020, 9, 8, 21, 30, 45, 40, tzinfo=pytz.UTC)
print(dt)
dt_now = datetime.datetime.now(tz=pytz.UTC)
print(dt_now)


#for tz in pytz.all_timezones:
 #   print(tz)

dt_east = datetime.datetime.now().astimezone(pytz.timezone('Asia/Calcutta'))
print(dt_east)

dt_mtn = datetime.datetime.now(tz=pytz.timezone('Asia/Calcutta'))
print(dt_mtn.strftime('%B %d, %Y'))


dt_str='July 26, 2016'

dt=datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)