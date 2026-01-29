import os
import time

def cls():
    os.system(command="clear")

study: bool = True
break_bool: bool = False

pomodoro: bool = True
count = 0

study_time = 0.1
break_time = 1

study_sec: int = study_time*60
break_sec: int = break_time*60

while pomodoro:
    cls()
    print(f"Remaining Time : {study_sec}")
    time.sleep(1)
    cls()
    study_sec -= 1
    count += 1
    if study_sec < 1:
        study = False
    if study == False:
        break_bool = True
        cls()
        print(f"Remaining Break Time : {break_sec}")
        time.sleep(1)
        cls()
        break_sec -= 1
        if break_sec < 1:
            break_bool = False
            study = True



    

