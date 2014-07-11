import math
def dopplerperiod(period,v):
    return period*(100+v)/100


def relat_dopplerperiod(period, v):
    if v>=0:
        return dopplerperiod(period, v)/(math.sqrt(1.0-(v/100.0)**2))
    else:
        return dopplerperiod(period, v)/(math.sqrt(1.0-(v/100.0)**2))


def sync():
    clock2.digit=clock3.digit
    clock1.digit=clock3.digit


def reset():
    clock1.digit=0
    clock2.digit=0
    clock3.digit=0



def adjust_period(period,v):
    return dopplerperiod(period,v), relat_dopplerperiod(period, v)

for i in [-99,-99.9,-99.999,-99.9999999]:
    print i, adjust_period(10.0,i)