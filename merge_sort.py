# start index jo sub array ko suru krega
# end index jo sub array ko khatm krega
# mid jo start aur end dono ka beech ka index nikalega

def marge(arr, start,mid ,end):  #  # merge function 
        # left sub array aur right sub array ki length nikalenge
    length_left = mid - start + 1
    length_right = end - mid
    # left sub array aur right sub array ke liye temp arrays banayenge
    left_arr = [0]*length_left
    right_arr =[0]*length_right

     # elements ko left aur right sub arrays mein daalenge
    for i in range(length_left):
        left_arr[i] = arr[start + i]
    for j in range(length_right):
        right_arr[j] = arr[mid+1 +j]
    i = 0 # left array ke pehle element se compare karne ke liye (left pointer)
  
    j = 0  # right array ke pehle element se compare karne ke liye (right pointer)
    original_index = start  # original array mein values wapas dalne ke liye index

    # ab hum left aur right ko merge karenge [start ..... end]
    while i < length_left and j < length_right:
        if left_arr[i] <= right_arr[j]:
            arr[original_index] = left_arr[i]
            i +=1
        else:
            arr[original_index] = right_arr[j]
            j +=1
        original_index += 1
    # agar left array ke element bache hai toh unko wpas dalenge
    while i < length_left:
        
        arr[original_index] = left_arr[i]
        i +=1
        original_index += 1

    while j < length_right:
        arr[original_index] = right_arr[j]
        j += 1
        original_index += 1

   
def marge_sort_main(arr, start, end):
    if start < end:
        mid = (start+ end)  //2
        marge_sort_main(arr,start,mid)   #left half
        marge_sort_main(arr,mid+1 , end) #right half
        marge(arr,start,mid,end) #marge both halves , yaha pr hum apne upper wale function ko call krenge jo sorting krega
arr = [20,5,9,70,36,2,1]
marge_sort_main(arr,0,len(arr)-1)# 0 se aakhri index tak sort
print(arr)