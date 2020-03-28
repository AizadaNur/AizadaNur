def left2(str):
    result = ""
    if len(str)<=2:
        result = str
    last=len(str)
    result=str[2:last]+str[:2]
    return result