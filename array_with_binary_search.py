#binary search
Array = [5, 3, 9, 1]


target = 8
def binary(Array,target):
  start = 0
  end = len(Array)-1
  while start <= end:
        mid = (start+end)//2
        if Array[mid] == target:
            return f"founded"
        elif Array[mid] < target:
          start = mid + 1
        else:
          end = mid -1
  return f"number is not found"
print(binary(Array,target))
#  time complexity O(log n )  log for dividation   and n for number of intration because loop is here