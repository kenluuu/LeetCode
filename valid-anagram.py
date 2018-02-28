class Solution(object):
    def isAnagram(self, s, t):        
        dict = {}
        for letter in s:
            if letter not in dict:
                dict[letter] = 1
            else:
                dict[letter] += 1

        for letter in t:
            if letter in dict:
                dict[letter] -= 1
            else:
                return False
        for key in dict:
            if dict[key] != 0:
                return False

        return True
