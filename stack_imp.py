# from sys import maxsize
# def createStack():
#     stack=[]
#     return stack
#
# def isempty(stack):
#     return len(stack)==0
#
# def push(stack,item):
#     stack.append(item)
#     print(item+"is pushed into stack")
#
# def pop(stack):
#     if isempty(stack):
#         return str(-maxsize-1)
#     return stack.pop()
#
# stack=createStack()
# push(stack,str(10))
# push(stack,str(20))
# print(pop(stack))

from sys import maxsize
def createStack():
    stack=[]
    return stack

def isempty(stack):
    return len(stack)==0
def push(stack,item):
    stack.append(item)
    print(item )
def pop(stack):
    if isempty(stack):
        return str(-maxsize-1)
    return stack.pop()

stack=createStack()
push(stack,str(1))
push(stack,str(2))
print(pop(stack))
print(pop(stack))
print(pop(stack))
