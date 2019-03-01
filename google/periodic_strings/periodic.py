# Find whether string S is periodic
import logging
import time

def period_1(s):
    # an odd length string cannot be periodic
    if len(s)%2 != 0:
        return None
    for window in range(1, len(s)//2, 2):
        print(window)
        if window > 1:
            template = s[0:window-1]
            reps = len(s)//(window-1)
        else:
            template = s[0]
            reps = len(s)
        candidate = "".join([template] * reps)
        if candidate == s:
            return template 
    return None


def period_2(s):
    # an odd length string cannot be periodic
    if len(s)%2 != 0:
        return None
    buffer = ""
    per = "" 
    p = 0
    for i in range(0, len(s)):
        buffer += s[i]
        if i > 0 and s[i] == per[p]:
            p += 1
            if p == len(per):
                p = 0
        else:
            p = 0
            per += buffer
            buffer = "" 
    print(per)
    if len(per) < len(s):
        return per
    else:
        return None
           

if __name__ == "__main__":
    assert(period_2("abababab") == "ab")
    assert(period_2("abcdabc") == None)
    assert(period_2("aaabaaa") == None)
    s = "".join(["reallyreallylongperiodicstring" * 1000000])
    t1 = time.time()
    assert(period_2(s) == "reallyreallylongperiodicstring")
    t2 = time.time()
    t3 = time.time()
    assert(period_1(s) == "reallyreallylongperiodicstring")
    t4 = time.time()
    print("%s, %s" % (t2-t1, t4-t3))

