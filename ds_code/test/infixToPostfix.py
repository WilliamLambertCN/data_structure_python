import sys,os
sys.path.append("ds_code/basic/")
# print(sys.path)
# print(os.getcwd())

def infixToPostfix(infixexpr):
    opstack=Stack()
    postfixList=[]
    prec={}
    prec["*"]=3
    prec["/"]=3
    prec["+"]=2
    prec["-"]=2
    prec["("]=1
    tokenList = list(infixexpr)

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or \
            token in "0123456789":
            postfixList.append(token)
        elif token =="(":
            opstack.push(token)
        elif token ==")":
            topToken = opstack.pop()
            while topToken!="(":
                postfixList.append(topToken)
                topToken = opstack.pop()
        else:
            while (not opstack.isEmpty()) and \
                prec[opstack.peek()] >= prec[token]:
                postfixList.append(opstack.pop())
            opstack.push(token)
    while not opstack.isEmpty():
        postfixList.append(opstack.pop())

    return " ".join(postfixList)

print(infixToPostfix("A*B+C*D"))
list("A*B+C*D")