class Solution(object):
    def lengthOfLastWord(self, s):
        array = s.split(" ")  
        length = len(array)
        number = length - 1
        for _ in range(length):
            if array[number] != "":
                return len(array[number])
            else:
                number -= 1