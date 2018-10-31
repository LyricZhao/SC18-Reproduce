import numpy as np
import matplotlib.pyplot as plt

# from 2^0 to 2^(len-1)
ele_counts = [261, 278777, 576411, 125043, 67203, 44567, 25385, 569]
dyn_counts = [ 15,  42891, 	   73, 		0,     0,     0,     0,   0]

ind = np.arange(len(ele_counts))
fig, ax = plt.subplots(figsize = (6, 3))

width = 1
plt.subplots_adjust(left = 0.15, right = 0.98)

rects1 = ax.bar(ind - width * 0.5, ele_counts, width, color =  'Gray', edgecolor = 'Black', label = 'Elements')
rects2 = ax.bar(ind - width * 0.5, dyn_counts, width, color = 'Black', edgecolor = 'Black', label = 'Dynamic rupture faces')

ax.set_ylabel('Counts')
ax.set_xticks(ind)
ax.set_xticklabels([2 ** i for i in range(0, len(ele_counts))])
ax.legend()

plt.savefig('load.eps', format = 'eps', dpi = 1200, bbox_inches = 'tight')
# plt.show()