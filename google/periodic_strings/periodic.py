# Find whether string S is periodic
import logging

def period(s):
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


if __name__ == "__main__":
    assert(period("abababab") == "ab")
    assert(period("abcdabc") == None)
    assert(period("aaabaaa") == None)
    s = "".join(["reallyreallylongperiodicstring" * 1000000])
    assert(period(s) == "reallyreallylongperiodicstring")

