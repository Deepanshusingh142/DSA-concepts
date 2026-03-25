#find  missing number is a sequance
a =[0,1,2,3,4,5,6,7,9,10]
expect_sum = set(range(a[0],a[-1]+1))
current = set(a)
result = expect_sum - current
print(result)

# for this approch i will change array into set and then we comepair both two each other