def readFile(fileName):
    validateFileName(fileName)
    data = ""
    with open(fileName, "r") as file:
        listData = file.readlines()
        joinedData = "".join(listData)
    return joinedData

def validateFileName(fileName):
    # Take the substring of that last 4 characters of the file name:
    # Should be 4 characters back from the end of the string i.e. len(fileName) - 4
    fileExtension = fileName[len(fileName) - 4 : len(fileName)]

    if fileExtension != ".amb":
        raise Exception("INVALID FILE EXTENSION. Please make sure that the file you are running ends with '.amb'")

def createRunnable(fileName, codeList):
    runnableFile = open(fileName, "a")
    idx = 0
    for codeLine in codeList:
        print("Line " + str(idx) + ": " + codeLine)
        runnableFile.write(codeLine)
