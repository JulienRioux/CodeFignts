Given an array strings, determine whether it follows the sequence given in the patterns array. 
In other words, there should be no i and j for which strings[i] = strings[j] and patterns[i] ≠ patterns[j] 
or for which strings[i] ≠ strings[j] and patterns[i] = patterns[j].

Example:

For strings = ["cat", "dog", "dog"] and patterns = ["a", "b", "b"], the output should be
areFollowingPatterns(strings, patterns) = true;
For strings = ["cat", "dog", "doggy"] and patterns = ["a", "b", "b"], the output should be
areFollowingPatterns(strings, patterns) = false.



def areFollowingPatterns(strings, patterns):
    
    # create a dict and check if there is no keys duplicates
    # if there is, check if their values are the same too
    D = {}
    for i in range(len(patterns)):
        if patterns[i] not in D:
            D[patterns[i]] = strings[i]
        else:
            if D[patterns[i]] != strings[i]:
                return False
            
    values = list(D.values())
    
    # Check for duplicates in the values
    return len(values) == len(set(values))
