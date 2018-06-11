#coding=utf-8
import datetime

birthday=datetime.date(1994,12,25)
now=datetime.date.today()
age=now-birthday
print(age.days)