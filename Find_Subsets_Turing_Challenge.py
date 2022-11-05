"""
Turing Challenge
Find subsets of a given array, subsets should be in an order.
"""
#Solution

def find_subsets(arr):
    x = len(arr)
    ans=[]
    for i in range(1 << x):
        ans.append([arr[j] for j in range(x) if (i & (1 << j))])
    return ans
print(find_subsets([4,5,6]))
