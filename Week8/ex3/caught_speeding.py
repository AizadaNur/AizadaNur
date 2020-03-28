def caught_speeding(speed, is_birthday):
    res=0
    if is_birthday:
        if speed<=65 :
            res=0
        if speed>65 and speed<=85:
            res= 1
        if speed>=86:
            res= 2
    else:
        if speed<=60 :
            res=0
        if speed>60 and speed<=80:
            res= 1
        if speed>=81:
            res= 2
    return res
