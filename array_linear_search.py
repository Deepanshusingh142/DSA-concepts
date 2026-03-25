a = [10,12,13,14,15]
target = 1
found = False
for x in range(0,len(a)):
  if a[x] == target:
    print(f"the nmber is fonded on this {x} location")
    found = True
    break
  if found is not True:
    print("the tageted number is not fonded")
    break
#time complexity O(n) kuki single loop hai humne ye nhi pta ki target kaha milega  ho skta hai
# ki target  stating me mile yani best case   mid mile yani normal case    
# target last me kahi mila toh worst case