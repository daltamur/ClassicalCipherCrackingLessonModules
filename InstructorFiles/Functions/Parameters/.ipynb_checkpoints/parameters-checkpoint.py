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
    #For best results, make the key between 3 and 8 letters
    return list(bytes('CLOAK', 'utf-8'))

def check_beaufort_decypher(testVal):
    assert testVal=='FOLLOWTHECLUES'
    
def get_hill_cipher_key():
    #the video's byte length is divisible by 43, so we are forcing the
    #key to be a 43x43 matrix. However, it will always be random and therefore different for everystudent
    return np.random.randint(256, size=(43, 43))