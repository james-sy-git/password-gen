"""
Random password generator that allows the user to choose to include special
characters, and capital letters (whether or not the password needs
to be case-sensitive). Also cross-references the password against the English
dictionary, as passwords containing existing words are more vulnerable.

James Sy
1/22/2022
"""

import passwordgen

from PyDictionary import PyDictionary

dict = PyDictionary()

pw_length = int(input("Please enter the desired number of characters in your password: "))
assert isinstance(pw_length, int) and pw_length > 0, "ERROR: Your entry was not valid."

case = input("Is this password case-sensitive? (Type Y if yes, N if NO): ")
assert case == "Y" or case == "N", "ERROR: Your entry was not Y or N."

spec = input("Should your password contain special characters? (Type Y if YES, N if NO): ")
assert spec == "Y" or spec == "N", "ERROR: Your entry was not Y or N."

def gen_password():
    """
    Generates a password based on the user's inputs in pw_length, case and spec
    """
    if case == "Y" and spec == "Y":
        output = passwordgen.generate(pw_length, True, True)
        if check(output):
            gen_password()
    elif case == "Y" and spec == "N":
        output = passwordgen.generate(pw_length, True, False)
        if check(output):
            gen_password()
    elif case == "N" and spec == "Y":
        output = passwordgen.generate(pw_length, False, True)
        if check(output):
            gen_password()
    else: # case == "N" and spec == "N"
        output = passwordgen.generate(pw_length, False, False)
        if check(output):
            gen_password()

    return output

def check(word):
    """
    Uses the PyDictionary module to compare a generated password to known
    English words, and determines if a word is in the dictionary (returns False
    if it is)
    """
    if dict.meaning(word, True) is None:
        return True
    else:
        return False

if __name__ == "__main__":
    print("Your password is: " + gen_password())
