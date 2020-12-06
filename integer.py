import os.path


numOfFiles = input("plese input the number of files: ")
numOfFiles = int(numOfFiles)

while numOfFiles > 0:
    fileName = input("Please input a file name: ")
    stack = []
    count = 0
    found = " "
    if os.path.isfile(fileName):
        file = open(fileName, 'r')
        text = file.read()
        file.close()
    else:
        print("Please input a valid file")
        break
    for x in text:
        if x == '(':
            stack.append(x)
            count = count + 1
        elif x == '{':
            stack.append(x)
            count = count + 1
        elif x == '[':
            stack.append(x)
            count = count + 1
        elif x == ')':
            if stack[count - 1] == '(':
                stack.pop()
                count = count - 1
            else:
                found = x
                break
        elif x == '}':
            if stack[count - 1] == '{':
                stack.pop()
                count = count - 1
            else:
                found = x
                break
        elif x == ']':
            if stack[count - 1] == '[':
                stack.pop()
                count = count - 1
            else:
                found = x
                break
    print("File Name \t Line Number \t Expected Charcter \t Found Character ")
    if  count == 0:
            print(fileName + " No error found")
    else:
            line = str(count)
            expected = stack[count - 1]
            if expected == "(":
                expected = ")"
            if expected == "{":
                expected = "}"
            if expected == "[":
                expected = "]"
            print(fileName + "\t\t" + line + "\t\t" + expected + "\t\t" + found)
    numOfFiles = numOfFiles - 1

	
