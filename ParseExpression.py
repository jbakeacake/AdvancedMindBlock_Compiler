from ParseTree import Node
from ParseTree import ParseTree
from Tokenizer import *

# def parseExpression(currentNode, tokens, idx):

#     if len(tokens) <= 0:
#         return None
    
#     currentToken = tokens[idx]

#     expressionSet = {
#         "Expression" : addExpressionChildren,
#         "Term Tail" : addTermTailChildren,
#         "Term" : addTermChildren,
#         "Factor Tail" : addFactorTailChildren,
#         "Factor" : addFactorChildren
#     }

#     while idx < len(tokens) and currentNode != None:
#         if len(currentNode.body) == 0:
#             if expressionSet.get(currentNode.type) != None:
#                 expressionSet[currentNode.type](currentNode, currentToken)
#             elif currentNode.tokenOrVariable is "token":
#                 parseTokenLiteral(currentNode, currentToken)
#                 #if our next index is within bounds, lets add one
#                 if idx + 1 < len(tokens):
#                     idx += 1
#                     currentToken = tokens[idx]
#         currentNode = currentNode.nextNode()


# Returns a tuple containing all nodes to be added to an expression node:
def addExpressionChildren(currentNode, currentToken):
    predictSet = [
        "softOpen",
        "digit",
        "characterString",
        "label"
    ]
    if currentToken.get("type") in predictSet:
        currentNode.addChild("Term")
        currentNode.addChild("Term Tail")
    else:
        raise Exception("Error on Expression")

def addTermTailChildren(currentNode, currentToken):
    # Create a predict set just to maintain uniformity with other add children methods
    predictSet_0 = [
        "addOp"
    ]

    predictSet_1 = [
        "compOp",
        "DO",
        "softClose",
        "THEN",
        "semi"
    ]

    if currentToken.get("type") in predictSet_0:
        currentNode.addChild("addOp", None, "token")
        currentNode.addChild("Term")
        currentNode.addChild("Term Tail")
    elif currentToken.get("type") in predictSet_1:
        currentNode.addChild(None)
    else:
        raise Exception("Error on Term Tail")

def addTermChildren(currentNode, currentToken):
    predictSet = [
        "softOpen",
        "digit",
        "characterString",
        "label"
    ]

    if currentToken.get("type") in predictSet:
        currentNode.addChild("Factor")
        currentNode.addChild("Factor Tail")
    else:
        raise Exception("Error on Term")

def addFactorTailChildren(currentNode, currentToken):
    predictSet_0 = [
        "multOp"
    ]

    predictSet_1 = [
        "addOp",
        "compOp",
        "DO",
        "softClose",
        "semi",
        "THEN"
    ]

    if currentToken.get("type") in predictSet_0:
        currentNode.addChild("multOp", None, "token")
        currentNode.addChild("Factor")
        currentNode.addChild("Factor Tail")
    elif currentToken.get("type") in predictSet_1:
        currentNode.addChild(None)
    else:
        raise Exception("Error on Factor Tail")

def addFactorChildren(currentNode, currentToken):
    predictSet_0 = [
        "softOpen"
    ]
    predictSet_1 = [
        "digit"
    ]
    predictSet_2 = [
        "characterString"
    ]
    predictSet_3 = [
        "label"
    ]

    if currentToken.get("type") in predictSet_0:
        currentNode.addChild("Expression")
    elif currentToken.get("type") in predictSet_1:
        currentNode.addChild("digit", None, "token")
    elif currentToken.get("type") in predictSet_2:
        currentNode.addChild("characterString", None, "token")
    elif currentToken.get("type") in predictSet_3:
        currentNode.addChild("label", None, "token")
        currentNode.addChild("PossibleArray")
    else:
        raise Exception("Error on Factor")

def addPossibleArrayChildren(currentNode, currentToken):
    predictSet_0 = [
        "hardOpen"
    ]

    predictSet_1 = [
        "multOp",
        "addOp",
        "compOp",
        "DO",
        "softClose",
        "semi",
        "THEN"
    ]

    if currentToken.get("type") in predictSet_0:
        currentNode.addChild("hardOpen", None, "token")
        currentNode.addChild("Factor") # Changed from "digit" to "Factor" so we can loop through arrays
        currentNode.addChild("hardClose", None, "token")
    elif currentToken.get("type") in predictSet_1:
        currentNode.addChild(None)
    else:
        raise Exception("Error on Possible Array")

# line = "2 + 3 * 4;"
# tokens = Tokenizer(line)
# for token in tokens:
#     print(token)

# pt = ParseTree()

# parseExpression(pt.head, tokens, 0)

# print("\n")
# pt.dumpTree()
