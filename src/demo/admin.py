
from django.contrib import admin
from .models import * 
# Register your models here.

admin.site.register(Country)
admin.site.register(State)
admin.site.register(District)
admin.site.register(Blog)
admin.site.register(Entry)
admin.site.register(Author)




# import datetime 
# import schedule
# import time
# current_time  = datetime.datetime.now()
# time_change = datetime.timedelta(minutes=1)
# end_date = current_time+time_change
# print("time change date ========================", current_time)

# print("time change date ========================", time_change)

# print("all date ========================", end_date)
# def job():
#     print("I'm working..." , datetime.datetime.now())

# schedule.every(3).seconds.do(job)

# while current_time < end_date:
#     current_time = datetime.datetime.now()
#     schedule.run_pending()



# current_time  = datetime.datetime.now()
# time_change = datetime.timedelta(minutes=10)
# all_time= current_time+time_change
# print(all_time)
