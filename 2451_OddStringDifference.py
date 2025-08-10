from typing import List

class Solution:
    def oddString(self, words: List[str]) -> str:
        diff_map = {}
        for word in words:
            diff_array = []
            for i in range(1, len(word)):
                diff_array.append(ord(word[i]) - ord(word[i-1]))
            diff_tuple = tuple(diff_array)
            if diff_tuple not in diff_map:
                diff_map[diff_tuple] = [word]
            else:
                diff_map[diff_tuple].append(word)
        for k, v in diff_map.items():
            if len(v) == 1:
                return v[0]