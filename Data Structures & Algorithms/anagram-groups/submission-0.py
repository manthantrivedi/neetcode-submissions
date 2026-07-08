class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for i in strs:
            sortedString = ''.join(sorted(i)) 
            print(sortedString)
            result[sortedString].append(i)
        
        return list(result.values())