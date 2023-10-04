class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        MatchingLetter = True
        Prefix = ""
        PrefixEndIndex = 0
        while MatchingLetter == True:
            CurrentLetter = ""
            for i in range(len(strs)):
                if len(strs[i]) > 0:
                    if CurrentLetter == "":
                        CurrentLetter += strs[i][0:1]
                    if strs[i][0:1] != CurrentLetter:
                        MatchingLetter = False
                    strs[i] = strs[i][1:]
                else:
                    MatchingLetter = False
                    break
            if MatchingLetter == False:
                return Prefix
            Prefix += CurrentLetter
        return Prefix