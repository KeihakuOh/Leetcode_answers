class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        count = Counter(s)
        sorted_chars = sorted(count.keys(), reverse=True)
        result = []
        
        while sorted_chars:
            char = sorted_chars[0]
            if result and result[-1] == char and count[char] > 0:
                if len(sorted_chars) < 2:
                    break
                
                second_char = sorted_chars[1]
                result.append(second_char)
                count[second_char] -= 1

                if count[second_char] == 0:
                    sorted_chars.pop(1)
            else:
                use_count = min(repeatLimit, count[char])
                result.extend([char] * use_count)
                count[char] -= use_count
                
                if count[char] == 0:
                    sorted_chars.pop(0)

        return "".join(result)
