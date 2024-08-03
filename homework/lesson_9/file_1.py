import datetime

a = "Jan 15, 2023 - 12:05:33"
python_date = datetime.datetime.strptime(a, '%b %d, %Y - %H:%M:%S', )
print(python_date)
print(python_date.strftime('%b'))
print(python_date.strftime('"%d.%m.%Y, %H:%M"'))
