#1pehele index ko assum krenge ki wo sorted hai 
#2 bacche hue element compair ke liye hai 
# 3 assum se aage wale ko current varible jiso apne previous  yani 
# sorted element se compair krenge ki wo bda ki chhota 
# sorted hote hi sorted element ki conting bd bd jayegi aurm currect indis ko aage move kra denge 
# swaping hogi
#itration hone ke baad jb sor ho jayega 
#tb hum previous --1 krke checckr krnge current value se ki bdi hai ya chhoti
a = [8,6,1,9,3,4,5,2]
def insertion(a):
    for i in range(1,len(a)):
        current = a[i] # element of array
        previous = i-1
        #shifting ka kaam hamra while loop krega 
        while previous >= 0 and a[previous] > current:
            a[previous + 1] = a[previous]
            previous -=1
        a[previous + 1] = current
insertion(a)
print(a)