from scipy.stats import chi2
import numpy as np
d = 0
n = 200
m = np.array([[25, 50, 25], [52, 41, 7]])
p = np.array([1/2, 1/2])
q = np.array([77/200, 91/200, 32/200])

for i in range(2):
    for j in range(3):
        d += ((m[i][j] - q[j] * p[i] * n) ** 2) / (q[j] * p[i] * n)

res = chi2.sf(d, 2)
print(d)
print(res)