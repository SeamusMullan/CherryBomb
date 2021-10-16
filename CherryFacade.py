import instaloader as il
import inspirobot as ibot
import requests
import CB_Functions as cbfunc
import CB_Formatting as cbform
import datetime as dt
import os
import threading as th

today = dt.datetime.now()

def Generate(threadname=""):
    try:
        link = ibot.generate()
        r = requests.get(link)
        if not os.path.exists("TheInspire"):
            os.makedirs("TheInspire")
        if threadname == "":
            open(f'TheInspire\\theInspire_{str(today).replace(":", "-")}.jpg', 'wb').write(r.content)
        else:
            open(f'TheInspire\\theInspire_{threadname}_{str(today).replace(":", "-")}.jpg', 'wb').write(r.content)
    except Exception as e:
        cbform.returnError(e)
        cbform.saveErrorLog(e)
        return False        


def GenerateWithThreads(threadname=""):
    amount = int(input("How many images do you want? : "))

    threads = []
    for i in range(0, amount):
        t = th.Thread(target=Generate(str(i)))
        threads.append(t)
        t.start()


    while [thread for thread in threads if thread.is_alive()]:
        pass
    else:
        print(f"{cbform.C.CBLUE}All threads are finished!{cbform.C.ENDC}")


