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
# Tokenizer(input : String) : Stack
#
# This is the tokenizer responsible for taking in the code, line by line, and tokenizing each piece of the code. It then places
# this token into stack where it will be used later when parsing.
#
def Tokenizer(input):
    current = 0; # start of the line
    tokens = [] # our token stack
    while current < len(input):
        tokenized = False # this represents whether or not we have found the right tokenizer for the current part of the input
        for func in tokenizers:
            if tokenized:
                break
            token = func(input, current)
            #Check if the token's consumed amount of chars is not '0' -- we check length instead of nullity to consume skipped white spaces
            if token[0] != 0:
                tokenized = True
                current += token[0]
            #If the token is not a skipped white space and exists, append it to the end of our list:
            if token[1] != None:
                tokens.append(token[1])
        #If we've iterated through all of our functions without successfully tokenizing, print an error:
        if not tokenized:
            break
    return tokens

#
# Specific Tokenize functions
#
def tokenizeNumber(input, current):
    return tokenizePattern("digit", "[0-9]+", input, current);

def tokenizeName(input, current):
    return tokenizePattern("label", "[A-Za-z]|[_]|[.]", input, current); # we're overriding our 'type'("label") parameter if our input is a keyword (this happens inside the tokenizePattern function)

def tokenizeSoftOpen(input, current):
    return tokenizeCharacter("softOpen", "[(]", input, current);

def tokenizeSoftClose(input, current):
    return tokenizeCharacter("softClose", "[)]", input, current);

def tokenizeHardOpen(input, current):
    return tokenizeCharacter("hardOpen", "[[]", input, current);

def tokenizeHardClose(input, current):
    return tokenizeCharacter("hardClose", "[]]", input, current);

def tokenizeQuote(input, current):
    return tokenizeCharacter("quote", '["]', input, current);

def tokenizeSemi(input, current):
    return tokenizeCharacter("semi", "[;]", input, current);

def tokenizeColon(input, current):
    #special case to make sure this colon isn't followed by an equals:
    if input[current + 1] == "=":
        return [0, None]
    return tokenizeCharacter("colon", "[:]", input, current);

def tokenizeAssignment(input, current):
    return tokenizePattern("assignment", "[:]|[=]", input, current);

def tokenizeMultOp(input, current):
    return tokenizeCharacter("multOp", "[*]|[/]", input, current);

def tokenizeAddOp(input, current):
    return tokenizeCharacter("addOp", "[+]|[-]", input, current);

def tokenizeCompOp(input, current):
    return tokenizePattern("compOp", "[<]|[<=]|[>]|[>=]|[=]|[!=]", input, current)

# tokenizeString(input, current) : token
#
# This is specialized function to tokenize strings
#
### TODO : THIS UTILIZES A QUOTE, REFORMAT TO ONLY TOKENIZE THE STRING FOLLOWING THE FIRST QUOTE
def tokenizeString(input, current):
    token = {}
    if input[current] == '"':
        value = ''
        consumedChars = 0
        consumedChars += 1 #consume since we've detected an open quote (")
        char = input[current + consumedChars]
        #while the current char isn't a closing quote...
        while char != '"':
            if char == None:
                print("ERROR: Unterminated String")
                return;
            if (current + consumedChars + 1) < len(input):
                value += char;
                consumedChars += 1
                char = input[current + consumedChars]
            else:
                break
        token["type"] = "characterString"
        token["value"] = value;
        return [consumedChars + 1, token] # '+1' so we consume the following end quote
    else:
        return [0, None]

#
# Tokenize Helper Functions:
#
def tokenizeCharacter(type, value, input, current):
    #init our token return object:
    token = {};
    # if our value matches what the current character is, add values to our object and return:
    if re.search(value, input[current]) != None:
        token["type"] = type
        token["value"] = input[current]
        return [1, token]
    else: # Otherwise, return an error with a "None" token
        return [0, None]

def tokenizePattern(type, pattern , input, current):
    char = input[current] # init our first character in the string
    consumedChars = 0; # init our tracker for the length of the string
    token = {} # init our return object
    if re.search(pattern, char) != None: #Use Python's 're' package to determine whether the current character exists in our pattern
        value = '' # init our handle on the whole value of the token
        while (re.search(pattern, char) != None): # Build up our token character by character, incrementing consumedChars and moving our current character through the string
            value += char
            if (current + consumedChars + 1) < len(input):
                consumedChars += 1
            else:
                break
            char = input[current + consumedChars]
                
        #override our passed in "type" if this value is a keyword:
        if value in keywords:
            token["type"] = value
            token["value"] = value
            return [len(token["value"]), token]
        else:
            token["type"] = type
            token["value"] = value
            return [len(token["value"]), token]
    else:
        return [0, None];

def skipWhiteSpace(input, current):
    if input[current] == " ":
        return [1, None]
    return [0, None]

#This is a list of all our tokenizers that we will iterate through to allow us tokenize the given string
tokenizers = [ # Removed 'tokenizeQuote' until reformatting is done
    tokenizeNumber,
    tokenizeName,
    tokenizeSoftOpen,
    tokenizeSoftClose,
    tokenizeHardOpen,
    tokenizeHardClose,
    tokenizeString,
    tokenizeSemi,
    tokenizeColon,
    tokenizeAssignment,
    tokenizeCompOp,
    tokenizeAddOp,
    tokenizeMultOp,
    skipWhiteSpace
]

#This is a list of all keywords so we avoid mistaking 'label' symbols for keywords:
keywords = [
    "START_PROGRAM",
    "END_PROGRAM",
    "START_SUB",
    "END_SUB",
    "GOSUB",
    "CODE",
    "IF",
    "THEN",
    "ELSE",
    "END_IF",
    "WHILE",
    "DO",
    "END_WHILE",
    "INT",
    "STRING",
    "PRINT",
    "INPUT",
    "END_SUB.",
    "END_PROGRAM."
]

# token_g = tokenizeCompOp(">", 0)
# token_ge = tokenizeCompOp(">=", 0)
# token_l = tokenizeCompOp("<", 0)
# token_le = tokenizeCompOp("<=", 0)
# token_name = tokenizeName("START_PROGRAM bingo", 0)
# token_num = tokenizeNumber("1200000000034",0)
# token_ass = tokenizeAssignment(":=",0)
# print(token_g)
# print(token_ge)
# print(token_l)
# print(token_le)
# print(token_name)
# print(token_num)
# print(token_ass)

# input = "[INT] bingo [3]"
# testTokens = Tokenizer(input)
# # print("\n> OUR INPUT: \t STRING str := 'Hello World!' \n")
# for token in testTokens:
#     print(token)
