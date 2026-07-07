class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix=""
        #strs=["bat","bag","bank","band"]

        for i in range(len(strs[0])):
            for j in strs:
                if i==len(j) or j[i] != strs[0][i]:
                    return common_prefix
            common_prefix += strs[0][i]
        return common_prefix
