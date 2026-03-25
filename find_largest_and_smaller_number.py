arr =[10,15,2,11,60,80,77]
small = arr[0]
large = arr[0]
for i in range(1,len(arr)):
  if arr[i] < small:
    small = arr[i]
  elif arr[i] > large:
    large = arr[i]
print(f"largest number {large}  and your smallest number {small} ")
#interview 3