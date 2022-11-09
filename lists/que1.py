#!/usr/bin/python3
def add_target(nums, target):
    for i in range(len(nums)):
        for v in range(i + 1, len(nums)):
            if nums[i] + nums[v] == target:
                return[i, v]
