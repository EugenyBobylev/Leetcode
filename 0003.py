
def lengthOfLongestSubstring(s: str) -> int:
    bag = set()
    limit = 95
    max_len = len(bag)
    start = 0
    dct = {}
    for idx, symbol in enumerate(s):
        if symbol in dct:
            max_len = len(s[start, idx])
            start = 

    return max(max_count, len(bag))


if __name__ == '__main__':
    s_1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ "
    s_2 = 'abracegabru'
    res = lengthOfLongestSubstring(s_1)
    print(s_1, res)
