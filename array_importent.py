
a1  = [1, 2, 4, 6, 8]
target1 = 100
win1 = 0
win2 = len(a1)-1
out = False
while win1 < win2:
  if a1[win1] +a1[win2] == target1:
    print(f"using this index you can sum your target {win1} and {win2}")
    out = True
    break
  elif a1[win1] + a1[win2] < target1:
    win1 = win1 + 1
  else:
    win2 = win2 - 1
if not  out:
  print("soory out of range")