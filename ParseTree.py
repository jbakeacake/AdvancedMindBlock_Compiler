class Node:
    def __init__(self, type, value, tokenOrVariable = None, parent = None, checked = 0):
        self.type = type
        self.value = value
        self.tokenOrVariable = tokenOrVariable
        self.parent = parent
        self.body = []
        self.bodyIdx = 0
        self.checked = checked # this purely to use while dumping nodes, no other value
    
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
        if self.checked == 0:
            if self.tokenOrVariable is "token":
                print(tabs + "VALUE : " + str(self.value))
            else:
                print(tabs + "TYPE : " + self.type)
            self.checked = 1
        for child in self.body:
            for child in self.body:
                child.dumpNode(level + 1)
            
class ParseTree:
    def __init__(self, type = None):
        self.head = Node("Program", None) # for purposes of testing, lets start with expression

    def dumpTree(self):
        self.head.dumpNode(0)
