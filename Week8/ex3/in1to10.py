def in1to10(n, outside_mode):
    if outside_mode:
        if n<=1 or n>=10:
            return True
        else:
            return False
    elif not outside_mode:
        if n>=1 and n<=10:
            return True
        elif n<=1 or n>=10:
            return False
        else:
            return False


