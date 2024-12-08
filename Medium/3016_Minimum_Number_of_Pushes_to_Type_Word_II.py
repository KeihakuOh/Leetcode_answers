class Solution:
    def minimumPushes(self, word: str) -> int:
        ans = 0
        freq_map = Counter(word).most_common()
        layer = 1
        count = 0
        max_num = 8
        for i, freq in freq_map:
            if count == max_num:
                count = 0
                layer += 1
            count += 1
            ans += freq * layer
        return ans
