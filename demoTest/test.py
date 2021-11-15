import datetime

a = "10月30日"

year = datetime.datetime.now().strftime('%Y')

print(year)
b_time = a.replace('月', '-').replace('日', '')

a_time = year + "-" + b_time + " 00:00:00"
print((a_time))

dateTime_p = datetime.datetime.strptime(a_time,'%Y-%m-%d %H:%M:%S')
print((dateTime_p)) # 2019-01-30 15:29:08
