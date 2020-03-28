def alarm_clock(day, vacation):
    if vacation:
        if day==0 or day==6:
          return 'off'
        return '10:00'
    if not vacation:
        if day>=1 and day<6:
            return '7:00'
        return '10:00'