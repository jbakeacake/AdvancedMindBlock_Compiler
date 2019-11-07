from ParseTree import Node
from ParseTree import ParseTree
from Tokenizer import *
from ParseExpression import *
from ParseCodeList import *


def parseProgram(currentNode, tokens, idx=0):
    if len(tokens) < 0:
        return None
    
    currentToken = tokens[idx]

    ProgramListSet = {
        "Program" : addProgramChildren,
        "VariableList" : addVariableListChildren,
        "SubList" : addSubListChildren,
        "Variable" : addVariableChildren,
        "ArrayVariable" : addArrayVariableChildren,
        "CodeList" : addCodeListChildren,
        "CodeLine" : addCodeLineChildren,
        "Condition" : addConditionChildren,
        "ThenCodeList" : addThenCodeListChildren,
        "ElseCodeList" : addElseCodeList,
        "Loop" : addLoopChildren,
        "WhileCodeList" : addWhileCodeListChildren,
        "ExpressionOrInput" : addExpressionOrInputChildren,
        "LineLabel" : addLineLabelChildren,
        "Assignment" : addAssignmentChildren,
        "Expression" : addExpressionChildren,
        "Term Tail" : addTermTailChildren,
        "Term" : addTermChildren,
        "Factor Tail" : addFactorTailChildren,
        "Factor" : addFactorChildren,
        "PossibleArray" : addPossibleArrayChildren

    }

    while idx < len(tokens) and currentNode != None:
        if len(currentNode.body) == 0:
            if ProgramListSet.get(currentNode.type) != None:
                ProgramListSet[currentNode.type](currentNode, currentToken)
            elif currentNode.tokenOrVariable == "token":
                parseTokenLiteral(currentNode, currentToken)
                if idx + 1 < len(tokens):
                    idx += 1
                    currentToken = tokens[idx]
        currentNode = currentNode.nextNode()

def addProgramChildren(currentNode, currentToken):
    if currentToken.get("type") == "START_PROGRAM":
        currentNode.addChild("START_PROGRAM", None, "token")
        currentNode.addChild("VariableList")
    else:
        raise Exception("Error on Program")

def addVariableListChildren(currentNode, currentToken):
    predictSet_0 = [
        "INT",
        "STRING",
        "hardOpen"
    ]

    predictSet_1 = [
        "CODE"
    ]

    if currentToken.get("type") in predictSet_0:
        currentNode.addChild("Variable")
        currentNode.addChild("VariableList")
    elif currentToken.get("type") in predictSet_1:
        currentNode.addChild("CODE", None, "token")
        currentNode.addChild("SubList")
    else:
        raise Exception("Error on VariableList")

def addSubListChildren(currentNode, currentToken):
    predictSet_0 = [
        "START_SUB"
    ]

    predictSet_1 = [
        "END_PROGRAM."
    ]

    if currentToken.get("type") in predictSet_0:
        currentNode.addChild("START_SUB", None, "token")
        currentNode.addChild("label", None, "token")
        currentNode.addChild("colon", None, "token")
        currentNode.addChild("CodeList")
        currentNode.addChild("SubList")
    elif currentToken.get("type") in predictSet_1:
        currentNode.addChild("END_PROGRAM.", None, "token")
    else:
        raise Exception("Error on SubList")

def addVariableChildren(currentNode, currentToken):
    if currentToken.get("type") == "INT":
        currentNode.addChild("INT", None, "token")
        currentNode.addChild("label", None, "token")
        currentNode.addChild("semi", None, "token")
    elif currentToken.get("type") == "STRING":
        currentNode.addChild("STRING", None, "token")
        currentNode.addChild("label", None, "token")
        currentNode.addChild("semi", None, "token")
    elif currentToken.get("type") == "hardOpen":
        currentNode.addChild("hardOpen", None, "token")
        currentNode.addChild("ArrayVariable")
    else:
        raise Exception("Error on Variable")

def addArrayVariableChildren(currentNode, currentToken):
    if currentToken.get("type") == "INT":
        currentNode.addChild("INT", None, "token")
        currentNode.addChild("hardClose", None, "token")
        currentNode.addChild("label", None, "token")
        currentNode.addChild("hardOpen", None, "token")
        currentNode.addChild("digit", None, "token") #TODO implement set of digits that are only positive
        currentNode.addChild("hardClose", None, "token")
        currentNode.addChild("semi", None, "token")
    elif currentToken.get("type") == "STRING":
        currentNode.addChild("STRING", None, "token")
        currentNode.addChild("hardClose", None, "token")
        currentNode.addChild("label", None, "token")
        currentNode.addChild("hardOpen", None, "token")
        currentNode.addChild("digit", None, "token") #TODO implement set of digits that are only positive
        currentNode.addChild("hardClose", None, "token")
        currentNode.addChild("semi", None, "token")
    else:
        raise Exception("Error on ArrayVariable")


def parseTokenLiteral(currentNode, currentToken):
    predictSet = [
        "digit",
        "assignment",
        "characterString",
        "softOpen",
        "softClose",
        "hardOpen",
        "hardClose",
        "label",
        "addOp",
        "multOp",
        "compOp",
        "semi",
        "colon",
        "START_PROGRAM",
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

    if currentToken.get("type") in predictSet:
        currentNode.type = currentToken.get("type")
        currentNode.value = currentToken.get("value")
    else:
        raise Exception("Error on Token")