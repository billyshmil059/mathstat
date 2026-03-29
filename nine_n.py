from scipy.stats import chi2
import numpy as np
d = 0
n = 600
n1 = 300
n2 = 300
m = np.array([[33, 43, 80, 144], [39, 35, 72, 154]])
p = [0] * 4
for i in range(4):
    p[i] = (m[1][i] + m[0][i]) / n

for i in range(4):
    for j in range(2):
        d += ((m[j][i] - n1 * p[i]) ** 2) / (p[i] * n1)

res = chi2.sf(d, 3)
print(d)
print(res)