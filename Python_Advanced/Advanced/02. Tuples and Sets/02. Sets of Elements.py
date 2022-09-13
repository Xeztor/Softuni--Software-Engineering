n, m = list(map(int, input().split()))

n_set = set()
m_set = set()

for i in range(1, n + m + 1):
    if i <= m:
        n_set.add(int(input()))
    else:
        m_set.add(int(input()))

[print(unique) for unique in n_set.intersection(m_set)]