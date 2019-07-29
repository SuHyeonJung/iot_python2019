import time

real_year, now_day, now_time = time.strftime('%Y %x %X', time.localtime(time.time())).split(" ")

print(real_year)
print(type(real_year))
print(now_day)
now_day_modify = now_day[:5]
print(now_day_modify)
now_day_result = now_day_modify[:2]+now_day_modify[3:5]
print(now_day_result)
now_time_modify = now_time[:5]
now_time_result = now_time[:2] + now_time[3:5]
print(now_time_modify)
print(now_time_result)
print(type(now_time_result))
print(real_year+now_day_result)
