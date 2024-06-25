'''
This program works like a Pomodoro timer.  It displays the start time and then counts down the
minutes from 25.   Every 5 minutes it tells you to take a short break and then resumes the countdown.

'''

from datetime import datetime
import time

def main():
    start_time = get_current_time()
    #print(type(start_time))
    formatted_time = start_time.strftime("%H:%M:%S")
    print(f'The start time was {formatted_time}')
    min_remaining = 25
    while min_remaining >=0:
        interval = get_elapsed_time(start_time)
        time_passed_min = interval.total_seconds()/60
        min_remaining = int(25 - time_passed_min)
        print(f'minutes remaining: {min_remaining}')
        if min_remaining>0 and min_remaining %5 == 0:
            print()
            print(f'The time remaining in minutes is {str(min_remaining)}')
            print("Take a short break")
            print()
        time.sleep(60)
    print("Your time is over.  Take a longer break before restarting.")

def get_current_time():
    now = datetime.now()
    return now

def get_elapsed_time(start_time):
    now = datetime.now()
    interval = now - start_time
    return interval

if __name__ == '__main__':
    main()


