from ParseProgram import parseProgram
from FileManager import readFile
from ParseTree import Node
from ParseTree import ParseTree
from Tokenizer import *

fileName = input("Please input the name of your '.amb' file:")

fileContent = readFile(fileName)

print(fileContent)

tokens = Tokenizer(fileContent)
for tok in tokens:
    print(tok)

parseTree = ParseTree()
parseProgram(parseTree.head, tokens)
parseTree.dumpTree()