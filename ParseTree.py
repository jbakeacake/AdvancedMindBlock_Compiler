class Node:
    def __init__(self, type, value, tokenOrVariable = None, parent = None):
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
        for child in self.body:
            tab = "\t"
            print((tab * level) + "MY CHILDREN : " + self.type)
            
class ParseTree:
    def __init__(self, type = None):
        self.head = Node("Expression", None) # for purposes of testing, lets start with expression

    def dumpTree(self):
        currentNode = self.head
        level = 0
        print("TOP : " + currentNode.type)
        while len(currentNode.body) != 0:
            currentNode.dumpNode(level)
            currentNode = currentNode.nextNode()
            level += 1
