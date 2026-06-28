#fibonacci using recursion
import time
def fibo(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
start=time.time()
print(fibo(4))
print("time taken to execute the code is ",time.time()-start)
#we cannot use this method for large numbers as it takes a lot of time to execute the code.