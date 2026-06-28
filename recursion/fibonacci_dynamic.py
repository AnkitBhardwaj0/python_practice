#fibonacci using dynamic programming
import time
def febo(n,memo={}):
    if n in memo:
        return memo[n]
    else:
        memo[n] = febo(n-1,memo) + febo(n-2,memo)
        return memo[n]
start=time.time()
memo={0:0,1:1}
print(febo(48,memo))
print("time taken to execute the code is ",time.time()-start)