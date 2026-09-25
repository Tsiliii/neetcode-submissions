class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer_dict = {}

        for string in strs:
            characters = [0] * 26
            for char in string:
                characters[ord(char)-ord('a')] += 1
            
            key = tuple(characters)
            
            if key not in answer_dict:
                answer_dict[key] = []

            answer_dict[key].append(string)

        return list(answer_dict.values())
        
        
        # groups = {}
        # for string in strs:
        #     ordered_list = sorted((list(string)))
        #     ordered_string = "".join(ordered_list)
        #     if ordered_string not in groups:
        #         groups[ordered_string] = []
        #     groups[ordered_string].append(string)
        # return list(groups.values())