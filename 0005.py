def longestPalindrome(s: str) -> str:
    for pos, l in enumerate(s):
        print(pos, l)
        
    return ''

if __name__ == '__main__':
    s1 = 'babad'
    s2 = 'bb'
    s3 = 'privetmadam'
    s4 = 'madamprivet'
    
    res = longestPalindrome(s1)
    print(s1, res)
