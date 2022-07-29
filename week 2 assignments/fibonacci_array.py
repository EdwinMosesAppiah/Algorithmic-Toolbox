def fibnum(n):
   if n<= 0:
     return "Incorrect Output"
   arr = [0, 1]
   if n > 2:
        for i in range (2, n):
            arr.append(arr[i-1] + arr[i-2])
   return arr[n-1]
   

n = int(input())
print(fibnum(n))
