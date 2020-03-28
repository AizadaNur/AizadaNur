def combo_string(a, b):
    short=min(len(a),len(b))
    shortest = b
    longest=a
    if len(a)==short:
        shortest=a
        longest=b
    return shortest+longest+shortest