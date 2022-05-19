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

    output_minutes=int(time_minutes)+int(duration_minutes)
    output_hours=int(time_hours)+int(duration_hours)
    
    if output_minutes>59:
        h=0
        while output_minutes>60:
            output_minutes=output_minutes-60
            h=h+1
        output_hours=output_hours+h

    
    if output_hours>12:
        meridian_=0
        
        n=0
        while output_hours>12:
            output_hours=output_hours-12
            meridian_=meridian_+1
            days=days+1
    time_hours=int(time_hours)
    duration_hours=int(duration_hours)
    meridian_=0
    while duration_hours>0:
        if time_hours-12==0:
            meridian_=meridian_+1
        time_hours=time_hours+1
        duration_hours=duration_hours-1
        

    if meridian=="AM":
        x=meridian_%2
        if x==0:
            meridian="AM"
        else:
            meridian="PM"
    if meridian=="PM":
        x=meridian_%2
        if x==0:
            meridian="PM"
        else:
            meridian="AM"
    if len(str(output_minutes))==1:
        output_minutes="0"+str(output_minutes)
    new_time=str(output_hours)+":"+str(output_minutes)+ " "+meridian
    if days==0:
        when=""
        count=0
    elif days==2:
        when="(next day)"
        count=1
    elif days>2:
        count=1
        while days>=2:
            days=days-2
            count=count+1
        when="("+str(count)+" days later)"

    
        
    if today=="none":
        part_day=""
    else:
        x=today.lower()
        x=daya[x]
        x=x+count
        if x<6:
            keys=daya.keys()
            keys=list(keys)
            part_day=keys[x]
        elif x>6:
            while x>6:
                x=x-6
            part_day=keys[x]

            
    return (" "+new_time+" "+","+" "+part_day.capitalize()+" "+when)



print(add_time("3:30 PM", "2:12","Monday"))            

    
            
