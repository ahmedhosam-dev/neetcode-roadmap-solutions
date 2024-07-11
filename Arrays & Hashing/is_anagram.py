

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) > len(t) or len(s) < len(t):
            return False
        
        checkS: dict = {}
        checkT: dict = {}

        for i in s:
            if i in checkS:
                checkS[i] += 1
                continue
            checkS[i] = 1

        for i in t:
            if i in checkT:
                checkT[i] += 1
                continue
            checkT[i] = 1

        for i in checkS:
            if i not in checkT:
                return False
            if  checkS[i] != checkT[i]:
                return False
        
        return True


if __name__ == '__main__':
    s: Solution = Solution()
