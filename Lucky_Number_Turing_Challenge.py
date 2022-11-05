"""
Find lucky number in given array
Python Turing Challenge
"""
#Solution

def findLuckyNumber(arr):
    dic = {}
    my_list = []
    for i in arr:
        dic[i] = dic.get(i, 0) + 1
    for k, v in dic.items():
        if k == v:
            my_list.append(k)
    ans = max(my_list, default=-1)
    return ans
print(findLuckyNumber([2,2,3,4]))
print(findLuckyNumber([1,2,2,3,3,3]))
print(findLuckyNumber([2,2,2,3,3]))