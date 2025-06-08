class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def getLongestPrefixIndex(strs):
            shortest_string_len = min(len(word) for word in strs)

            for i in range(shortest_string_len):
                ch = strs[0][i]

                if any(word[i] != ch for word in strs):
                    return i

            return shortest_string_len

        return strs[0][:getLongestPrefixIndex(strs)]
