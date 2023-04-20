import numpy

def alberti_innerdisc():
    val = list(range(0,256))
    val = numpy.roll(val, 3)
    return list(val)

def alberti_increment():
    return 8

def alberti_period_length():
    return 5

def beaufort_key():
    return list(bytes('CLOAK', 'utf-8'))