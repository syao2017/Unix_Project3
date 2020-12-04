x = input("Please input a file name: ")
stack = []
count = 0
f = open(x, 'r')

text = f.read()
f.close()
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
    elif x == '}':
        if stack[count - 1] == '{':
            stack.pop()
            count = count - 1
    elif x == ']':
        if stack[count - 1] == '[':
            stack.pop()
            count = count - 1
print(stack)
