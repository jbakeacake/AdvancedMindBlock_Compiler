'''
The Emitter is responsible for returning the correct C code to append to a runnable C file.
'''

def emitIntegerLiteral(node):
    return node.value
def emitStringLiteral(node):
    return node.value
def emitSTRINGType(node):
    return "char* "
def emitINTType(node):
    return "int "
def emitAssignmentLiteral(node):
    return "="
def emitStringLiteral(node):
    return '"' + node.value + '"'
def emitSoftOpenLiteral(node):
    return "("
def emitSoftCloseLiteral(node):
    return ")"
def emitHardOpenLiteral(node):
    return "["
def emitHardCloseLiteral(node):
    return "]"
def emitLabelLiteral(node):
    return node.value
def emitAddOpLiteral(node):
    return " " + node.value + " "
def emitMultOpLiteral(node):
    return " " + node.value + " "
def emitCompOpLiteral(node):
    return node.value
def emitSemiLiteral(node):
    return "; \r"
def emitColonType(node):
    return "{ \r"
def emitSTART_PROGRAM(node):
    return "#include <stdlib.h>\r#include <stdio.h> \r"
def emitSTART_SUB(node):
    return "void "
def emitEND_SUB(node):
    return "} \r"
def emitIF(node):
    return "if("
def emitTHEN(node):
    return ") { \r"
def emitELSE(node):
    return "} else { \r"
def emitEND_IF(node):
    return "} \r"
def emitWHILE(node):
    return "while("
def emitDO(node):
    return ") {\r"
def emitEND_WHILE(node):
    return "} \r"
def emitPRINT(node):
    return "printf"
def emitINPUT(node):
    return "scanf"
def emitEND_SUB(node):
    return "} \r"

termDictionary = {
        "digit" : emitIntegerLiteral,
        "assignment" : emitAssignmentLiteral,
        "characterString" : emitStringLiteral,
        "softOpen" : emitSoftOpenLiteral,
        "softClose" : emitSoftCloseLiteral,
        "hardOpen" : emitHardOpenLiteral,
        "hardClose" : emitHardCloseLiteral,
        "label" : emitLabelLiteral,
        "addOp" : emitAddOpLiteral,
        "multOp" : emitMultOpLiteral,
        "compOp" : emitCompOpLiteral,
        "semi" : emitSemiLiteral,
        "colon" : emitColonType,
        "START_PROGRAM" : emitSTART_PROGRAM,
        "START_SUB" : emitSTART_SUB,
        "END_SUB" : emitEND_SUB,
        "GOSUB" : None,
        "CODE" : None,
        "IF" : emitIF,
        "THEN" : emitTHEN,
        "ELSE" : emitELSE,
        "END_IF" : emitEND_IF,
        "WHILE" : emitWHILE,
        "DO" : emitDO,
        "END_WHILE" : emitEND_WHILE,
        "INT" : emitINTType,
        "STRING" : emitSTRINGType,
        "PRINT" : emitPRINT,
        "INPUT" : emitINPUT,
        "END_SUB." : emitEND_SUB,
        "END_PROGRAM." : None
}

def getEmitCodeTerm(node):
    codeLine = termDictionary.get(node.type)
    if codeLine != None:
        codeLine = codeLine(node)
    return codeLine