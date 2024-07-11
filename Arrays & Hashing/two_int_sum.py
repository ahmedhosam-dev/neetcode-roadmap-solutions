

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        checkSum: dict = {}

        for i in range(len(nums)):
            if (target - nums[i]) in checkSum:
                return [checkSum[target - nums[i]], i]
            checkSum[nums[i]] = i
        
        print(checkSum)



if __name__ == '__main__':
    s:Solution = Solution()

    print(s.twoSum([3,4,5,6], 7))
