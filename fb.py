from datetime import datetime, time
from pytz import timezone







def razibvai(givenmins, bool):
    pacific= timezone('US/Pacific')
    now = datetime.now(pacific)

    time = now.strftime("%H:%M:%S")
    hours = int(time[:2])
    mins=int(time[3:5])
    secs=int(time[6:8])

    total = hours*60+mins
    if (bool == True):
        total =total + givenmins
        if(total<720):
            ampm='AM'
        else:
            ampm='PM'
        print("current:",time,"revised: ", int((total%1440)/60)%12,":",total%60,":" ,secs,ampm)
    else:
        total = total-(givenmins%1440)
        if (total<0):
            total = total + 1440
        if(total<720):
            ampm='AM'
        else:
            ampm='PM'
        print("current:", time, "revised: ", (int((total%1440)/60))%12,":",total%60,":",secs,ampm)

    

razibvai(10000,False)
razibvai(50,True)
