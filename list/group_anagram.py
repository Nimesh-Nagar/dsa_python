# 
from icecream import ic

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    
        hash_map = {}

        for ele in strs:
            ref = [0] * 26

            for ch in ele:
                ref[ ord(ch) - ord("a") ] += 1

            key = tuple(ref)
            # print(key)
            if key not in hash_map:
                hash_map[key] = []
            hash_map[key].append(ele)

        result = list(hash_map.values())
        ic(result)
        return result


print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
