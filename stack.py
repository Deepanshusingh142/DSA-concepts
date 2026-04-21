
#stack
stack = []
size_of_stack = 5
# peek = stack[-1]



def push(value):
  if len(stack) < size_of_stack:
    stack.append(value)
    
    print(f"peek element is {stack[-1]} ")
  else:
    is_empty() == False
    print("stack is over flow")

def is_empty():
  if len(stack)== 0:
      print("stack is empty")
      return True
  else:
      print("stack is not empty")
      return False
def pop():
  if is_empty() == False:
    remove = stack.pop()
    print(f"this is your peek element {remove}")
    return remove
  else:
    print(f"this is your next element that you can remove  {remove}")
  

while True:
  if len(stack) < size_of_stack:
    x =int(input("enter number the stack have space"))
    push(x)
  else:
    print("stack is full")
    break

option = (str.upper(input("do you want empty the ement")))
if option == "YES" or option == "Y":
  while True:
    
    if len(stack) == 0:
      print("now your stack is empty")
      break
    else:
      
      print(f"romove this element for now {pop()}")
else:
  print(f"ok sir your stack have {len(stack)}")

print(is_empty())
print(stack)



