class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for string in strs:
            ordered_list = sorted((list(string)))
            # print(ordered_list)
            ordered_string = "".join(ordered_list)
            if ordered_string not in groups:
                groups[ordered_string] = []
            groups[ordered_string].append(string)
        return list(groups.values())