#!/bin/python3.12

""" 
First problem (Easy):

Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

    Input: nums = [1, 2, 3, 3]
    Output: true

Example 2:

    Input: nums = [1, 2, 3, 4]
    Output: false

"""


class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        # TODO:
        # You will use dict data type
        # when there collision you will return true
        # other ways false

        checkCollision: dict = {}

        for num in nums:
            if num in checkCollision:
                return True
            else:
                checkCollision[num] = num

        return False


if __name__ == "__main__":
    ...
