
def lengthOfLongestSubstring(s: str) -> int:
    max_len = 0
    substr = []
    for pos, symbol in enumerate(s):
        if symbol in substr:
            start_idx = substr.index(symbol)
            max_len = max(max_len, len(substr))
            substr = substr[start_idx +1:]
        substr.append(symbol)
    return max(max_len, len(substr))


if __name__ == '__main__':
    s_1 = "garbage collector"
    s_2 = 'abracegabru'
    s_3 = "abcabcbb"
    s_4 = 'pwwkew'
    s_5 = 'qqqqqqqwetry'
    res = lengthOfLongestSubstring(s_4)
    print(s_4, res)
