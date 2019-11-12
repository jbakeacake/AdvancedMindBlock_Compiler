from ParseProgram import parseProgram
from FileManager import readFile
from ParseTree import Node
from ParseTree import ParseTree
from Emitter import *
from Tokenizer import *

def constructFile(input):
    tokens = Tokenizer(input)
    parseTree = ParseTree()
    parseProgram(parseTree.head, tokens)
    #create a list of all the code term's to append to our file:
    nodeList = []
    codeTermList = []
    parseTree.writeTree(nodeList)
    #now with our full node list, let's use our emitter to fill out our actual C code term list:
    for node in nodeList:
        term = getEmitCodeTerm(node)
        #Since some key words return a None value, lets set those terms as an empty string
        if term is None:
            term = ""
        codeTermList.append(term)
    #now that our code term list is filled out, let's strip tokens that would be considered invalid in C
    cleanTermList(codeTermList)

    #now write our code terms into a file:
    file = open("./RunnableFiles/main.c", "w")
    for idx, term in enumerate(codeTermList):
        print(term)
        file.write(term)


def cleanTermList(codeTermList):
    '''
    There are several cases in which a token's placement inside our list can be considered
    invalid. For now, let's just modify our "Variable ArrayVariable" to properly declare 
    '''
    #First remove unneeded hard brackets:
    for idx, term in enumerate(codeTermList):
        #if were in a valid place of our list:
        if idx > 2:
            # determine if our term is a type, then check for brackets in front and behind:
            if term.strip() == "int" or term.strip() == "char*":
                if codeTermList[idx - 1] == "[":
                    del codeTermList[idx - 1]
                    idx -= 1
                    del codeTermList[idx + 1]
            if term == "printf":
                definePRINT(codeTermList, idx)
            if term == "scanf":
                defineINPUT(codeTermList, idx)

def definePRINT(codeTermList, idx):
    '''
    Currently, the way we print information in AMB is done by:
        PRINT(Expression); -- i.e. "PRINT", "(", "label", ")"
    C prints information via:
        printf("<type>", label);'

    To properly convert this into C code, we'll need to be adding some extra terms into our list.
    Particularly, after our "(" term, so we'll need to be inserting tokens 2 indices ahead of our current
    "printf" term.

    We also need to determine whether the label we're using is a number or a string. In order to determine
    this, we can traverse our "VariableList" nodes to determine if our "label" matches a "Variable" child and
    extract our type from there.
    '''
    typeMarker = ""
    label = codeTermList[idx + 2]
    print("BINGO " + label)
    lblType = determineLabelType(codeTermList, label)
    print("BINGO " + lblType)
    if lblType == "int":
        typeMarker = '"%d \\n"'
    elif lblType == "char*":
        typeMarker = '"%s \\n"'
    # our current index should be at the position of our "printf" term, so our "(" is 1 index ahead:
    codeTermList.insert(idx + 2, typeMarker)
    # if our value is just a plain character string, avoid adding the comma:
    if not '"' in codeTermList[idx + 3]:
        codeTermList.insert(idx + 3, ",")

def defineINPUT(codeTermList, idx):
    '''
    A similar concept from definePRINT will be used here.
    The difference being that we'll use the label that is being assigned to our INPUT as the pointer for
    our INPUT's parameter.

    AMB Format:
    label := INPUT; -- i.e. "label", ":=", "INPUT", ";"
    C Format:
    scanf("<type>", &label);

    When this function is called, our current index in our term list will be the index of the current
    "scanf" term. We'll use this our point of origin to modify our list accordingly.

    If we're starting at our INPUT, we'll need to acquire the value of our "label" term, remove that term
    from the list, along with the "=" term. Then, we will need to insert a "(", "<type>", ",", "label", ")"
    into our list.
    '''
    #init
    typeMarker = ""
    #get our type:
    label = codeTermList[idx-2]
    lblType = determineLabelType(codeTermList, label)
    if lblType == "int":
        typeMarker = '"%d"'
        label = "&" + label
    elif lblType == "char*":
        typeMarker = '"%s"'
    # Now start inserting appropriate terms:
    codeTermList.insert(idx + 1, "(")
    codeTermList.insert(idx + 2, typeMarker)
    codeTermList.insert(idx + 3, ",")
    codeTermList.insert(idx + 4, label)
    codeTermList.insert(idx + 5, ")")
    # set the label and the assingment to an empty string so we don't modify our list
    codeTermList[idx - 1] = ""
    codeTermList[idx - 2] = ""


def determineLabelType(codeTermList, label):
    rtnType = ""
    for idx, term in enumerate(codeTermList):
        if label == term:
            rtnType = codeTermList[idx - 1]
            break
    return rtnType.strip()



