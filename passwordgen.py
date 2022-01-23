"""
Uses the secure randomizing algorith from the Python secrets module to
generate a random password. Contains two layers of randomization to ensure
password security.

James Sy
1/2/2022
"""

import secrets

sec = secrets.SystemRandom()

alpha = {1:"a", 2:"b", 3:"c", 4:"d", 5:"e", 6:"f", 7:"g", 8:"h", 9:"i", 10:"j",
11:"k", 12:"l", 13:"m", 14:"n", 15:"o", 16:"p", 17:"q", 18:"r", 19:"s", 20:"t",
21:"u", 22:"v", 23:"w", 24:"x", 25:"y", 26:"z"}

chars = {1:"!", 2:"@", 3:"#", 4:"$", 5:"^", 6:"&", 7:"*", 8:".", 9:"-", 10:"_",
11:"+", 12:"=", 13:";", 14:":", 15:"?"}

def generate(length, caps, spec):
    """
    Generates a random password
    length: the number of characters in the password
    caps: wheter or not the password contains capital letters (True if it does, False otherwise)
    spec: whether or not the password contains special characters (True if it does, False otherwise)
    """
    pw = ""

    if spec:
        for x in range(length):
            choices = sec.randint(0, 2) # 0 letter, 1 number, 2 special
            if choices == 0:
                if caps:
                    pw += case_sensitive()
                else:
                    pw += case_insensitive()
            elif choices == 1:
                pw += number()
            elif choices == 2:
                pw += special()
    else:
        for x in range(length):
            choices = sec.randint(0, 1) # 0 letter, 1 number
            if choices == 0:
                if caps:
                    pw += case_sensitive()
                else:
                    pw += case_insensitive()
            else:
                pw += number()
    return pw

def case_sensitive():
    """
    Generates either a capital or lowercase random letter
    """
    letter = case_insensitive()

    upper_lower = sec.randint(0, 1) # 0 is lower, 1 is upper
    if upper_lower == 0:
        return letter
    else:
        return letter.upper()

def case_insensitive():
    """
    Generates a lowercase random letter
    """
    key = sec.randint(1, len(alpha))
    return alpha[key]

def number():
    """
    Generates a random number
    """
    return str(sec.randint(0, 9))

def special():
    """
    Generates a random special character
    """
    key = sec.randint(1, len(chars))
    return chars[key]
