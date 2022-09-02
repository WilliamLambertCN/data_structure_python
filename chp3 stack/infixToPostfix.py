from pickletools import StackObject
import sys,os
sys.path.append("ds_code/basic/")
# print(sys.path)
# print(os.getcwd())

from stack import Stack
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
res = infixToPostfix("3*4+5*6")
print(res)


def evalPostfix(postfix):
    digits = Stack()
    for i,token in enumerate(postfix):
        if token in "0123456789":
            digits.push(float(token))
        elif token in "*/+-":
            rt=digits.pop()
            lt=digits.pop()
            if token == "*":
                temp_res=lt*rt
            elif token == "/":
                temp_res=lt*rt
            elif token == "+":
                temp_res=lt+rt
            elif token == "-":
                temp_res=lt-rt
            digits.push(temp_res)
    return digits.pop()

print(evalPostfix(res))