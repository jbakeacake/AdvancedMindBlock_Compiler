import re

# Each tokenizer will receive code as a string, and the current position on that line of code
#
# These will be represented as such :
#
# input : String >> current line of code
# current : int >> current position on that line of code
# -------
# Generic tokenize functions, such as 'tokenizeCharacter' or 'tokenizePattern' will return an object with the length of the token, and an object with two keys
# [type] and [value]
#
# More specific tokenize functions, such as 'tokenizeSoftOpen' or 'tokenizeKeyword', will utilize generic tokenize functions as helper functions.
#

#
# tokenizeKeyword
#
def tokenizeKeyword(input, current):
    return tokenizePattern("keyword", "[^\s+]", input, current);


#
# Helper Tokenize Functions:
#
def tokenizeCharacter(type, value, input, current):
    #init our token return object:
    token = {};
    # if our value matches what the current character is, add values to our object and return:
    if value == input[current]:
        token["length"] = 1
        token["type"] = type
        token["value"] = value
        return token
    else: # Otherwise, return an error:
        print("ERROR")

def tokenizePattern(type, pattern , input, current):
    char = input[current] # init our first character in the string
    consumedChars = 0; # init our tracker for the length of the string
    token = {} # init our return object
    if re.search(pattern, char) != None: #Use Python's 're' package to determine whether the current character exists in our pattern
        value = '' # init our handle on the whole value of the token
        while (re.search(pattern, char) != None) and (consumedChars < len(input)): # Build up our token character by character, incrementing consumedChars and moving our current character through the string
            value += char
            consumedChars += 1
            char = input[current + consumedChars]
            print("CURRENT CHAR: " + char);

        token["length"] = consumedChars
        token["type"] = type
        token["value"] = value
        return token
    else:
        print("ERROR")
