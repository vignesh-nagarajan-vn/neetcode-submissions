class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_alphabetized = "".join(sorted(s))
        t_alphabetized = "".join(sorted(t))
        if s_alphabetized == t_alphabetized:
            return True
        else:
            return False
