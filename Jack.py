days_map={'mon':0,'tue':1,'wed':2,'thur':3,'fri':4,'sat':5,'sun':6}
start_day=input().strip().lower()

first_sunday_in_day=(6 - days_map[start_day])+1
if first_sunday_in_days > n:
    sundays = 0
else:
    remainging_days = n - first_sunday_in_days
    sundays = 1 + (remainging_days // 7)
print(sundays)    
