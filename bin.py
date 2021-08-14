n=input("enter the no assigned to your day")
day=int(n)
holiday=input ("enter the no of days on holiday")
leave=int(holiday)
retday=(day+leave)%7 
#u go on a day and spend holiday ..this gives the the day of return
print ("your return day is ",retday)