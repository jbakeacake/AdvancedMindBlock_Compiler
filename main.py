predictSet = {
    "label" : ["LineLabel"],
    "IF" : ["Condition"],
    "WHILE" : ["Loop"],
    "PRINT" : ["PRINT(Expression)"], #placeholder till I figure out how to parse this
    "GOSUB" : ["GOSUB", "label"],
    }
currentToken = {
    "type" : "GOSUB"
}

if predictSet.get(currentToken.get("type")) != None:
    children = predictSet.get(currentToken.get("type"));
    for item in children:
        print(item)