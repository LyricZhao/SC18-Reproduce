import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(6,4))
x = [4, 5, 6, 7]
plt.xticks(x)

# Baseline
y = [0.1, 0.2, 0.3, 0.5]
plt.plot(x, y, linewidth = 1, label = 'BL L2') # L2
y = [0.05, 0.05, 0.04, 0.06]
plt.plot(x, y, '--', linewidth = 1, label = 'BL L3') # L3


# Shaking Corals
y = [0.04, 0.1, 0.12, 0.2]
plt.plot(x, y, linewidth = 1, label = 'SC L2') # L2
y = [0.07, 0.05, 0.09, 0.1]
plt.plot(x, y, '--', linewidth = 1, label = 'SC L3') # L3

plt.xlabel('Order')
plt.ylabel('Miss ratio')
plt.legend()

plt.savefig('cacheproxy.eps', format = 'eps', dpi = 1200, bbox_inches = 'tight')
# plt.show()