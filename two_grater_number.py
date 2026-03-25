#find two gratest number
a = [11,10,20,2,3,4,16,80]
if a[0] > a[1]:
  first = a[0]
  sec = a[1]
else:
  first =a[1]
  sec = a[0]
for num in range(2,len(a)):
  if a[num] > first:
    sec = first
    first = a[num]
  elif a[num] > sec and a[num] != first:
    sec = a[num]
print(f"pehla nuber{first}  second nuber {sec}")

#interview 4
