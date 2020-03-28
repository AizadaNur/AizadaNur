def common_end(a, b):
    end=max(len(a),len(b))
    for i in range(end):
        if a[len(a)-1]==b[len(b)-1] or a[0]==b[0]:
            return True
        return False