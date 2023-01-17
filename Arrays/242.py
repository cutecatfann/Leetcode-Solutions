class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        else:
            letters = "abcdefghijklmnopqrstuvwxyz"
            for l in letters:
                if s.count(l) != t.count(l):
                    return False
        return True
