import matplotlib.pyplot as plt
import numpy as np

y = np.array([
    0,2,4,6,8,10,12,14,16,18,
    20,22,24,26,28,30,32,34,36,38,
    40,38,36,34,32,34,36,38,40,42,
    44,46,48,46,44,42,40,38,36,34,
    32,30,28,26,24,26,30,35,40,45,
    50,55,60,65,70,75,80,85,90,95,
    100,96,92,88,84,80,76,72,68,64,
    60,56,52,48,44,40,36,32,28,24,
    20,18,16,14,12,10,9,8,7,6,5
])

x = np.arange(0, 101, 1)
print(f'{y.mean()}')
#
dy = np.diff(y)
#print(f'dy - {dy}')

trend = np.sign(dy)  # +1 up, -1 down, 0 flat
#print(f'trend - {trend}')

reversal_indices = np.where(np.diff(np.sign(dy)) != 0)[0] + 1
print(f'reversal_indices - {reversal_indices}')









'''
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.show()
'''