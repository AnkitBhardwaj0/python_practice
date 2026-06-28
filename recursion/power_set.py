#power set by recursion
def power_set(s):
    if len(s)==0:
        return [[]]
    else:
        subsets=power_set(s[1:])
        return subsets+[[s[0]]+subset for subset in subsets]
print(power_set([1,2,3]))