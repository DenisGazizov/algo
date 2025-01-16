def canMakeSubsequence(str1: str, str2: str) -> bool:
    def incr(a):
        return chr(ord(a) + 1)
    if len(str2) > len(str1):
        return False
    i,j = 0,0
    while len(str1) - i > len(str2):
        while j < len(str2) and (str1[i+j] == str2[j] or incr(str1[i+j]) == str2[j]):



        i += 1

