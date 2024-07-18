class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count: dict = {}
        freq: list[list[int]] = [[] for i in range(len(nums) + 1)]
        
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for n, c in count.items():
            freq[c].append(n)

        res: list = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

if __name__ == '__main__':
    s:Solution = Solution()

    print(s.topKFrequent([3,0,1,0], 1))

    

