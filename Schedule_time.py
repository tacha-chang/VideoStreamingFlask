import schedule
import time

schedule.every().day.at("9:30").do(job) #lines
schedule.every().day.at("9.00").do(job) # yesterday
schedule.every().wednesday.at("13:15").do(job) #สัปดา
