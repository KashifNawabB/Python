"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Constraints
1 ≤ s.length ≤ 104
s consists of parentheses only '()[]{}'.
"""
#Solution

def find_subsets(arr):
    x = len(arr)
    ans=[]
    for i in range(1 << x):
        ans.append([arr[j] for j in range(x) if (i & (1 << j))])
    return ans
print(find_subsets([4,5,6]))
