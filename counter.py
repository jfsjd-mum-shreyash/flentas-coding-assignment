from collections import Counter

def is_permutation_exist(pattern, text):
    pattern_count = Counter(pattern)
    n = len(pattern)
    for i in range(len(text) - n + 1):
        window = text[i:i+n]
        window_count = Counter(window)
        if window_count == pattern_count:
            return True
    return False

t = int(input())
for _ in range(t):
    pattern = input().strip()
    text = input().strip()
    if is_permutation_exist(pattern, text):
        print("YES")
    else:
        print("NO")
