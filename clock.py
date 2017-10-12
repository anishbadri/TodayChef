import main
from apscheduler.schedulers.blocking import BlockingScheduler
# from apscheduler.schedulers.background import BackgroundScheduler
import time
from datetime import datetime

sched=BlockingScheduler()

@sched.scheduled_job('cron',day_of_week ='mon-sun',hour = 18, minute = 41)
def Hello():
	main.RemainderSend('4055417443','you genius')
	main.Remainder("Are you cooking today? Reply 'Yes' or 'No' ")


# @sched.scheduled_job('interval', minutes=1	)
# def timed_job():
#     main.Remainder()
#     # main.RemainderSend('+14055417443','Message')


# sched.start()

if __name__ == "__main__":
	try:
		sched.start()
	except(KeyboardInterrupt,SystemExit):
		pass
	print('Done')


    # This is here to simulate application activity (which keeps the main thread alive).
    # try:
   	# 	while True:
   	# 		time.sleep(2)
    # except (KeyboardInterrupt, SystemExit):
    #     # Not strictly necessary if daemonic mode is enabled but should be done if possible
    # 	bsched.shutdown()
# 		