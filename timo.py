def add_time(time,duration,today="none"):

    daya={"monday":0,"tuesday":1,"wednesday":2,"thursday":3,"friday":4,"saturday":5,"sunday":6}
    time=time.split(' ')
    meridian=time[1]
    time_real=time[0].split(':')
    time_hours=time_real[0]
    time_minutes=time_real[1]
    duration=duration.split(':')
    duration_hours=duration[0]
    duration_minutes=duration[1]
    days=0

    if meridian=="PM":
        time_hours=int(time_hours)+12
    

    

    output_minutes=int(time_minutes)+int(duration_minutes)
    output_hours=int(time_hours)+int(duration_hours)
    
    if output_minutes>59:
        h=0
        while output_minutes>=60:
            output_minutes=output_minutes-60
            h=h+1
        output_hours=output_hours+h
    
        
        
    if output_hours>24 and output_hours%24!=0:
        while output_hours>24:
            output_hours=output_hours-24
            days=days+1
        if output_hours>=12:
            meridian="PM"
            output_hours=output_hours-12
        elif output_hours<12:
            meridian="AM"

    if output_hours<24:
        if output_hours>=12:
            meridian="PM"
            output_hours=output_hours-12
        elif output_hours<12:
            meridian="AM"

    if output_hours%24==0:
        days=days+round(output_hours/24)
        output_hours=12
        if days%2==0 and days>0:
            meridian="AM"
        
        



    if days==0:
        when=""
    if days==1:
        when=" (next day)"
    if days>1:
        when=" (%d days later)"%(days)

    if today!="none":
        today=today.lower()
        today_num=daya[today]
        the_day=today_num+days
        weekdays=list(daya.keys())
        if the_day<=6:
            part_day=str(","+" "+weekdays[the_day].capitalize())
        elif the_day>=7:
            while the_day>=7:
                the_day=the_day-7
            part_day=str(","+" "+weekdays[the_day].capitalize())
    elif today=="none":
        part_day=""

    if len(str(output_minutes))==1:
        output_minutes="0"+str(output_minutes)

    sol=str(output_hours)+":"+str(output_minutes)+" "+meridian+part_day+when
        
    return sol

print(add_time("11:59 PM", "24:05"))
print(add_time("11:40 AM", "0:25"))
