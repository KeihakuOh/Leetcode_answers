class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        char_count = Counter(s)
        sorted_chars = sorted(char_count.keys(), reverse=True)
        result = []

        while sorted_chars:
            primary_char = sorted_chars[0]
            if result and result[-1] == primary_char:
                if len(sorted_chars) < 2: 
                    break

                secondary_char = sorted_chars[1] 
                result.append(secondary_char)
                char_count[secondary_char] -= 1

                if char_count[secondary_char] == 0:
                    sorted_chars.pop(1)
            else:
                use_count = min(repeatLimit, char_count[primary_char])
                result.extend([primary_char] * use_count)
                char_count[primary_char] -= use_count

                if char_count[primary_char] == 0:
                    sorted_chars.pop(0)

        return "".join(result)
