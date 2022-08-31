import sys,os
sys.path.append("ds_code/basic/")
# print(sys.path)

from stack import Stack

def matches(l,r):
    syms="([{)]}"
    return syms.index(l)==syms.index(r)+3

def parChecker(symbolString):
    s=Stack()
    balanced =True
    index=0
    while index <len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                if not matches(symbol,s.pop()):
                    balanced = False
        index = index+1
    if balanced and s.isEmpty():
        return True
    else:
        return False
# print(parChecker("((()))"))
# print(parChecker("(()"))

