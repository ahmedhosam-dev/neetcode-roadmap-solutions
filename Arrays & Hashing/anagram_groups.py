from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        res = defaultdict(list)

        for s in strs:
            count: list = [0] * 26


            for c in s:
                count[ord(c) - ord('a')] += 1

            res[tuple(count)].append(s)
            print(res)

        return res.values()


if __name__ == '__main__':
    s:Solution = Solution()

    print(s.groupAnagrams(["act","pots","tops","cat","stop","hat"]))
                        