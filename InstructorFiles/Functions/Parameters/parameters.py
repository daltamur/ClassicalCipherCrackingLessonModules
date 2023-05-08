import numpy as np

def alberti_innerdisc():
    val = list(range(0,256))
    val = np.roll(val, 3)
    return list(val)

def alberti_increment():
    #make this whatever you want
    return 8

def alberti_period_length():
    #make this whatever you want
    return 5

def beaufort_key():
    #For best results, make the key between 3 and 8 letters, that way it isn't something that is too big for the student to work with
    return list(bytes('CLOAK', 'utf-8'))

def check_beaufort_decypher(testVal):
    assert testVal=='FOLLOWTHECLUES'
    
def transposition_key():
    #Keep this key constant, this lesson requires the student to do a crib search on a text, and since that takes a long time I have hidden the key for encryption/decryption in the text
    return list(bytes('DESURTION', 'utf-8'))