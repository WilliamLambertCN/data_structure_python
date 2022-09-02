import sys,os
sys.path.append("ds_code/basic/")
# print(sys.path)
# print(os.getcwd())

from stack import Stack

def infixToPrefix(infixexpr):
    opStack=Stack()
    prefixStack=Stack()
    prec={}
    prec["*"]=3
    prec["/"]=3
    prec["+"]=2
    prec["-"]=2
    prec[")"]=1
    tokenList = list(infixexpr)[::-1] # inverse the string

    for token in tokenList: #digits
        # print(token)
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or \
            token in "0123456789":
            prefixStack.push(token)
        elif token ==")": # )
            opStack.push(token)
        elif token =="(": # (
            topToken = opStack.pop()
            while topToken!=")":
                prefixStack.push(topToken)
                topToken = opStack.pop()
        elif opStack.isEmpty() or prec[opStack.peek()] <= prec[token]: # ops
            opStack.push(token)
        elif not opStack.isEmpty() and prec[opStack.peek()] > prec[token]:
            while (not opStack.isEmpty()) and \
                prec[opStack.peek()] > prec[token]:
                prefixStack.push(opStack.pop())
            opStack.push(token)
    while not opStack.isEmpty(): # ops into prefix exp
        prefixStack.push(opStack.pop())
    
    res=""
    while not prefixStack.isEmpty():
        res = res+prefixStack.pop()
    return res

print(infixToPrefix("1+(2+3)*4-5"))