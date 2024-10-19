def palindrome(s):
    lp = 0
    rp = len(s)-1
    while rp >= lp:
        if not s[lp]==s[rp]:
            return False
        lp += 1
        rp -= 1
    return True
print(palindrome("bobson"))