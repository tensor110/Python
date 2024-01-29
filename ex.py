# ----3----
# --3-2-3--
# 3-2-1-2-3
n = 3
for i in range(n):
   for j in range(3*n):
        if(i<j):
            print("-")
        else:
            print(n-j)