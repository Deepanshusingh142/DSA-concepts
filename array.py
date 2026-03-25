a = [1,2,3,2]  # space complexity O(1)
# Traversal
for x in a:
    print(x)      #   jaha bhi itration hota hai toh pta nhi ki value kaha mile isliye time complexity O(n)

# Access
print(a[2])  #  time complexity hamesa O(1) yani constent  rehti hai ok
 
# Insert
a.append(5) #  time complexity  O(1) yani constent  rehti hai ok  kuki single insert ho raha hai
print(a) 
# Delete
a.remove(1)  #  time complexity  O(1) yani constent  rehti hai ok  kuki single delete ho raha hai

print(a) 
