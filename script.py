s1 = "abcd"
s2 = "a3cd"

for c1, c2 in (s1, s2):
    if c1 != c2:
        c2 = c1
        if s1 == s2:
            print('True')
            break
        else:
            print('False')
            break
