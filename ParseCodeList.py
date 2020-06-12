from ParseTree import Node
from ParseTree import ParseTree
from Tokenizer import *
from ParseExpression import *


# def parseCodeList(currentNode, tokens, idx):
#     if len(tokens) < 0:
#         return None
    
#     currentToken = tokens[idx]

#     codeListSet = {
#         "CodeList" : addCodeListChildren,
#         "CodeLine" : addCodeLineChildren,
#         "Condition" : addConditionChildren,
#         "ThenCodeList" : addThenCodeListChildren,
#         "ElseCodeList" : addElseCodeList,
#         "Loop" : addLoopChildren,
#         "WhileCodeList" : addWhileCodeListChildren,
#         "ExpressionOrInput" : addExpressionOrInputChildren,
#         "LineLabel" : addLineLabelChildren,
#         "Assignment" : addAssignmentChildren,
#         "Expression" : addExpressionChildren,
#         "Term Tail" : addTermTailChildren,
#         "Term" : addTermChildren,
#         "Factor Tail" : addFactorTailChildren,
#         "Factor" : addFactorChildren
#     }

#     while idx < len(tokens) and currentNode != None:
#         if len(currentNode.body) == 0:
#             if codeListSet.get(currentNode.type) != None:
#                 codeListSet[currentNode.type](currentNode, currentToken)
#             elif currentNode.tokenOrVariable == "token":
#                 parseTokenLiteral(currentNode, currentToken)
#                 if idx + 1 < len(tokens):
#                     idx += 1
#                     currentToken = tokens[idx]
#         currentNode = currentNode.nextNode()

def addCodeListChildren(currentNode, currentToken):
    predictSet_0 = [
        "PRINT",
        "GOSUB",
        "label",
        "IF",
        "WHILE"
    ]

    predictSet_1 = [
        "END_SUB."
    ]

    if currentToken.get("type") in predictSet_0:
        currentNode.addChild("CodeLine")
        currentNode.addChild("CodeList")
    elif currentToken.get("type") in predictSet_1:
        currentNode.addChild("END_SUB.", None, "token")
    else:
        raise Exception("Error on CodeList")

def addCodeLineChildren(currentNode, currentToken):

    if currentToken.get("type") == "label":
        currentNode.addChild("LineLabel")
    elif currentToken.get("type") == "IF":
        currentNode.addChild("Condition")
    elif currentToken.get("type") == "WHILE":
        currentNode.addChild("Loop")
    elif currentToken.get("type") == "PRINT":
        currentNode.addChild("PRINT", None, "token")
        currentNode.addChild("softOpen", None, "token")
        currentNode.addChild("Expression")
        currentNode.addChild("softClose", None, "token")
        currentNode.addChild("semi", None, "token")
    elif currentToken.get("type") == "GOSUB":
        currentNode.addChild("GOSUB", None, "token")
        currentNode.addChild("label", None, "token")
        currentNode.addChild("softOpen", None, "token")
        currentNode.addChild("softClose", None, "token")
        currentNode.addChild("semi", None, "token")
    else:
        raise Exception("Error on CodeLine")

def addConditionChildren(currentNode, currentToken):
    predictSet = [
        "IF"
    ]

    if currentToken.get("type") in predictSet:
        currentNode.addChild("IF", None, "token")
        currentNode.addChild("Expression")
        currentNode.addChild("compOp", None, "token")
        currentNode.addChild("Expression")
        currentNode.addChild("THEN", None, "token")
        currentNode.addChild("ThenCodeList")
    else:
        raise Exception("Error on Condition")

def addThenCodeListChildren(currentNode, currentToken):
    predictSet_0 = [
        "PRINT",
        "GOSUB",
        "label",
        "IF",
        "WHILE"
    ]

    predictSet_1 = [
        "ELSE"
    ]

    predictSet_2 = [
        "END_IF"
    ]

    if currentToken.get("type") in predictSet_0:
        currentNode.addChild("CodeLine")
        currentNode.addChild("ThenCodeList")
    elif currentToken.get("type") in predictSet_1:
        currentNode.addChild("ELSE", None, "token")
        currentNode.addChild("ElseCodeList")
    elif currentToken.get("type") in predictSet_2:
        currentNode.addChild("END_IF", None, "token")
    else:
        raise Exception("Error on ThenCodeList")

def addElseCodeList(currentNode, currentToken):
    predictSet_0 = [
        "PRINT",
        "GOSUB",
        "label",
        "IF",
        "WHILE"
    ]

    predictSet_1 = [
        "END_IF"
    ]

    if currentToken.get("type") in predictSet_0:
        currentNode.addChild("CodeLine")
        currentNode.addChild("ElseCodeList")
    elif currentToken.get("type") in predictSet_1:
        currentNode.addChild("END_IF", None, "token")

def addLoopChildren(currentNode, currentToken):
    
    if currentToken.get("type") == "WHILE":
        currentNode.addChild("WHILE", None, "token")
        currentNode.addChild("Expression")
        currentNode.addChild("compOp", None, "token")
        currentNode.addChild("Expression")
        currentNode.addChild("DO", None, "token")
        currentNode.addChild("WhileCodeList")
    else:
        raise Exception("Error on Loop")

def addWhileCodeListChildren(currentNode, currentToken):
    predictSet_0 = [
        "PRINT",
        "GOSUB",
        "label",
        "IF",
        "WHILE"
    ]

    predictSet_1 = [
        "END_WHILE"
    ]

    if currentToken.get("type") in predictSet_0:
        currentNode.addChild("CodeLine")
        currentNode.addChild("WhileCodeList")
    elif currentToken.get("type") in predictSet_1:
        currentNode.addChild("END_WHILE", None, "token")
    else:
        raise Exception("Error on WhileCodeList")

def addExpressionOrInputChildren(currentNode, currentToken):
    predictSet_0 = [
        "softOpen",
        "digit",
        "characterString",
        "label"
    ]

    predictSet_1 = [
        "INPUT"
    ]

    if currentToken.get("type") in predictSet_0:
        currentNode.addChild("Expression")
    elif currentToken.get("type") in predictSet_1:
        currentNode.addChild("INPUT")
        currentNode.addChild("semi", None, "token")
    else:
        raise Exception("Error on ExpressionOrInput")

def addLineLabelChildren(currentNode, currentToken):
    predictSet = [
        "label"
    ]

    if currentToken.get("type") in predictSet:
        currentNode.addChild("label", None, "token")
        currentNode.addChild("Assignment")

def addAssignmentChildren(currentNode, currentToken):
    predictSet_0 = [
        "assignment"
    ]

    predictSet_1 = [
        "hardOpen"
    ]

    if currentToken.get("type") in predictSet_0:
        currentNode.addChild("assignment", None, "token")
        currentNode.addChild("ExpressionOrInput")
        currentNode.addChild("semi", None, "token")
    elif currentToken.get("type") in predictSet_1:
        currentNode.addChild("hardOpen", None, "token")
        currentNode.addChild("digit", None, "token")
        currentNode.addChild("hardClose", None, "token")
        currentNode.addChild("assignment", None, "token")
        currentNode.addChild("ExpressionOrInput")
        currentNode.addChild("semi", None, "token")
    else:
        raise Exception("Error on Assignment Variable")


# input = "IF 7 > 1 THEN label := 42; ELSE label := 0; END_IF END_SUB."

# tokens = Tokenizer(input)
# for token in tokens:
#     print(token)

# pt = ParseTree()

# parseCodeList(pt.head, tokens, 0)

# print("\n")
# pt.dumpTree()
