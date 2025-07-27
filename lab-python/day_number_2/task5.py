from collections import Counter
s = sorted(input().split())
s_counts = Counter(s)
for s, count in s_counts.most_common():
    print(count, s)
