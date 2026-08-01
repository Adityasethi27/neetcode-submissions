class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            shape = "".join(sorted(word))
            if shape in groups:
                groups[shape].append(word)
            else:
                groups[shape] = [word]
        return list(groups.values())
        