import os
import Compiler
from FileManager import *

# fileName = input("Please input the name of your '.amb' file:")
inputContent = readFile("test.amb")

Compiler.constructFile(inputContent)
os.system('cmd /k "cd ./RunnableFiles && gcc main.c"')

# print(fileContent)

# myList = [2,2,3,4,5]

# for idx, term in enumerate(myList):
#     print(myList[idx])
# tokens = Tokenizer(fileContent)
# for token in tokens:
#     print(token)

# parseTree = ParseTree()
# parseProgram(parseTree.head, tokens)
# parseTree.dumpTree()