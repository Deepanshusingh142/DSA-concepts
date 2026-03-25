# find the largest element in the list
a  = [10,12,1,3,4,5,66,90,13]
lagest = a[0]

for x in range(1, len(a)):
  if a[x] > lagest:
    lagest = a[x]
print(lagest)

#interview question 1