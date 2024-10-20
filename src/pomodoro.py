# Pomodoro timer logic

# Recommended channel:
# https://www.youtube.com/@abaointokyo

import time

def start_pomodoro(task):
    work_duration = 25 * 60  # 25 minutes in seconds
    break_duration = 5 * 60  # 5 minutes in seconds

    while True:
        print(f"Working on: {task}")
        start_timer(work_duration)
        
        take_short_break(break_duration)
        is_task_done = input("Is the task complete? (yes/no): ").lower()
        
        if is_task_done == "yes":
            print(f"Task '{task}' completed!")
            break
        else:
            print("Continuing with task.")

def start_timer(duration):
    while duration:
        mins, secs = divmod(duration, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        duration -= 1

def take_short_break(duration):
    print(f"Taking a {duration//60}-minute break!")
    start_timer(duration)
