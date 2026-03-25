#selection sort
a = [4,12,45,10,5,7]
for i in range(len(a)-1):
  min_inx = i
  for j in range(i+1,len(a)):
    if a[j] < a[min_inx]:
      min_inx = j
  a[i],a[min_inx] = a[min_inx] ,a[i]
print(a)
