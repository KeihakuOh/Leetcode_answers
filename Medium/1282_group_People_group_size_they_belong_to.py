class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        myMap = {}
        for i, person in enumerate(groupSizes):
            if person not in myMap:
                myMap[person] = [i]
            else:
                myMap[person].append(i)
        res = []
        for group in myMap:
            if len(myMap[group]) > group:
                temp = myMap[group]
                for i in range(0, len(temp), group): 
                    res.append(temp[i:i+group])
            else:
                res.append(myMap[group])
        return res
                
