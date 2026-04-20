#stack 
#oprations
# 1 pop 
# 2 push
# 3 peek
# 4 is empty
# 5 size

stack = []
stack_size = 6
def push(value):
    if  size() < stack_size:
        stack.append(value)
    else:
        print("stack have no space ",size(),"elements in stack")
def pop():
    if is_empty():
        print("stack in empty ")
    else:
        return stack.pop()

def peek():
    if is_empty():
        print("stack is empty")
    else:
        return print(stack[-1])
    
def is_empty():
    return len(stack)==0

def size():
    return len(stack)

while True:
    if size() < stack_size:

        x =int(input("enter nuber"))
        push(x)
    else:
        print("stack is full and the top element is ",stack[-1])
        break

