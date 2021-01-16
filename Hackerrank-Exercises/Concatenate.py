from numpy import *

n, m, p = map(int, input().split())

n_matrix = array([list(map(int, input().split())) for _ in range(n)])

m_matrix = array([list(map(int, input().split())) for _ in range(m)])

print(concatenate((n_matrix, m_matrix), axis=0))
