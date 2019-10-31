from ParseTree import Node
from ParseTree import ParseTree
from Tokenizer import *

def parseTokens(tokens):
    idx = 0
    parseTree = ParseTree()
    currentNode = parseTree.head
    #Check if length of tokens is greater than 0:
    if len(tokens) <= 0:
        return None
    
    #while our current index of our tokens list is valid
    while idx < len(tokens) and currentNode != None:
        # if our current Node has no children (body), lets explore it:
        if len(currentNode.body) == 0:
            if currentNode.type is "Expression":
                if tokens[idx].get("type") is "digit":
                    currentNode.addChild("Term")
                    currentNode.addChild("Term Tail")
                    currentNode.addChild("semi")
                else:
                    raise Exception("Error on Expression")
            elif currentNode.type is "Term Tail":
                if tokens[idx].get("type") is "addOp":
                    currentNode.addChild("addOp", None, "token")
                    currentNode.addChild("Term")
                    currentNode.addChild("Term Tail")
                elif tokens[idx].get("type") is "semi":
                    currentNode.addChild(None)
                else:
                    raise Exception("Error on Term Tail")
            elif currentNode.type is "Term":
                if tokens[idx].get("type") is "digit":
                    currentNode.addChild("Factor")
                    currentNode.addChild("Factor Tail")
                else:
                    print(tokens[idx].get("type"))
                    raise Exception("Error on Term")
            elif currentNode.type is "Factor Tail":
                if tokens[idx].get("type") is "multOp":
                    currentNode.addChild("multOp", None, "token")
                    currentNode.addChild("Factor")
                    currentNode.addChild("Factor Tail")
                elif tokens[idx].get("type") is "semi" or tokens[idx].get("type") is "addOp":
                    currentNode.addChild(None)
                else:
                    raise Exception("Error on Factor Tail")
            elif currentNode.type is "Factor":
                if tokens[idx].get("type") is "digit":
                    currentNode.addChild("digit", None, "token")
                else:
                    raise Exception("Error on Factor")
            elif currentNode.tokenOrVariable is "token":
                if tokens[idx].get("type") is "digit" or tokens[idx].get("type") is "addOp" or tokens[idx].get("type") is "multOp": #TODO Add Terminal Token list for checks
                    currentNode.type = tokens[idx].get("type")
                    currentNode.value = tokens[idx].get("value")
                    idx += 1
            
        currentNode = currentNode.nextNode()
    return parseTree
            

line = "2 + 3 * 4"
tokens = Tokenizer(line)
for token in tokens:
    print(token)

pt = parseTokens(tokens)
