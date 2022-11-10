#!/usr/bin/python3
nums = [4,5,7,9]

target = 12

def twoSum(nums, target):
    prevMap = {}
    for index, num in enumerate(nums):
        diff = target - num
        if diff in prevMap:
            return [prevMap[diff], index]
        prevMap[num] = index
    return


result = twoSum(nums, target)
print(result)