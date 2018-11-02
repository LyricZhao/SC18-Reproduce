import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(6,4))
x = [4, 5, 6, 7]
plt.xticks(x)

# Baseline
y = [0.1, 0.2, 0.3, 0.5]
plt.plot(x, y, linewidth = 1, marker = '2', label = 'BL L2', ms = 4) # L2
y = [-1, -1, -1, 0.3] # the last number if for noHT
plt.plot(x, y, linewidth = 0, marker = 'o', label = 'BL/noHT L2', ms = 8)

# Shaking Corals
y = [0.04, 0.1, 0.12, 0.2]
plt.plot(x, y, linewidth = 1, marker = 'p', label = 'SC L2', ms = 4) # L2
y = [-1, -1, -1, 0.1] # the last number if for noHT
plt.plot(x, y, linewidth = 0, marker = '*', label = 'SC/noHT L2', ms = 8)

plt.ylim(0, 1.0)
plt.xlabel('Order')
plt.ylabel('Miss ratio')
plt.legend()

plt.savefig('cacheproxy.eps', format = 'eps', dpi = 1200, bbox_inches = 'tight')
# plt.show()