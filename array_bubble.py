a = [10,5,8,7,3,2,4]
l = len(a)
# isme  hum sbse bdi value ko use thik position pr pahuchate hai 
#step 1 iteration
#setp 2  number of comparisions  set krnege
# loop  chlega 
# loop ki itration jitni aage bdegi comarisions utne hi km hote jayege 
# totel comparision = legth - iteration - 1
def bubble(a,l):
    for i in range(0,l):
        for j in range(0,l-i-1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1] ,a[j]


bubble(a,l)
print(a)