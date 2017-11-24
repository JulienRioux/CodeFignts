# A string is said to be beautiful if b occurs in it no more times than a; c occurs in it no more times than b; etc.

# Given a string, check whether it is beautiful.

# Example

# For inputString = "bbbaacdafe", the output should be
# isBeautifulString(inputString) = true;
# For inputString = "aabbb", the output should be
# isBeautifulString(inputString) = false;
# For inputString = "bbc", the output should be
# isBeautifulString(inputString) = false.

def isBeautifulString(inputString):
    
    # Create a list of all the letters in the alphabet
    alpha = []
    a = ord("a")
    for i in range(26):
        alpha.append(chr(i+a))
    
    # For every letter in the alphabet, check if it occur more time in the 
    # inputString than the next letter in the alphabet
    for i in range(len(alpha)-1):
        if inputString.count(alpha[i]) < inputString.count(alpha[i+1]):
            return False
    # Otherwise, everything is alright!
    return True
