a = [10,20,30,40,50]  #  un sorted array hai ye 
checker = a[0]
sot = True
for x in range(1,len(a)):
  if a[x] > checker:
    checker = a[x]
  else:
    sot = False
    break
if sot:
  print("list is sorted")
else:
  print("list is not sorted")