from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for word in strs:
            key = "".join(sorted(word))
            
            if key not in dic:
                dic[key] = []
            dic[key].append(word)
        lst = list(dic.values())
        lst.sort(key=len)
        return lst