class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        dic = {}
        for person, size in enumerate(groupSizes):
            dic[size] = dic.get(size, []) + [person]
        return [lst[i:i+key] for key, lst in dic.items() for i in range(0,len(lst),key)]
