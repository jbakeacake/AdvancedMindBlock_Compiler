class Node:
    def __init__(self, type, value, tokenOrVariable = None, parent = None, isLiteral = False):
        self.type = type
        self.value = value
        self.tokenOrVariable = tokenOrVariable
        self.parent = parent
        self.body = []
        self.bodyIdx = 0
    
    def addChild(self, type, value = None, tokenOrVariable = None):
        if type != None:
            child = Node(type, value, tokenOrVariable, self)
            self.body.append(child)
    
    def nextNode(self):
        if self.bodyIdx < len(self.body):
            rtnNode = self.body[self.bodyIdx]
            self.bodyIdx += 1
            return rtnNode
        else:
            self.bodyIdx = 0
            rtnNode = self.parent
            return rtnNode
    def dumpNode(self, level):
        tabs = "\t" * (level)
        if self.tokenOrVariable == "token":
            print(tabs + "VALUE : " + str(self.value))
        else:
            print(tabs + "TYPE : " + self.type)
        for child in self.body:
            child.dumpNode(level + 1)

    def writeNode(self, codeTermList):
        if self.tokenOrVariable =="token":
            codeTermList.append(self)
        for child in self.body:
            child.writeNode(codeTermList)
    

            
class ParseTree:
    def __init__(self, type = None):
        self.head = Node("Program", None)

    def dumpTree(self):
        self.head.dumpNode(0)

    def writeTree(self, codeTermList):
        self.head.writeNode(codeTermList)
    
