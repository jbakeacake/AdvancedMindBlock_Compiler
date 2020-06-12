import os
import Compiler
from FileManager import *

# fileName = input("Please input the name of your '.amb' file:")
inputContent = readFile("test.amb")

Compiler.constructFile(inputContent)
os.system("echo ##############")
os.system("echo __________________________")
os.system("echo Advanced Mind Block Output:")
os.system("echo __________________________")
os.system("cd ./RunnableFiles && gcc main.c -o main && main")

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
