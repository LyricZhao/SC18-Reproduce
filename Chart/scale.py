import numpy as np
import matplotlib.pyplot as plt

'''
lts/gts
bl/sc
order=6
gflops/time

NOTE: should be GTS>LTS,BL>SC
'''

fig, axes = plt.subplots(nrows = 1, ncols = 2, figsize = (6, 4))
plt.subplots_adjust(bottom = 0.24, right = 0.94)

ax_flops = axes[0]
ax_times = axes[1]
x = [1, 2, 3, 4]
ax_flops.set_xticks(x)

# Baseline
# LTS Order 6
y = [200, 198, 196, 195]
t = [256, 140, 90, 70]
ax_flops.plot(x, y, linewidth = 1, marker = '1', color = 'Red', label = 'BL L6', ms = 4)
ax_times.plot(x, t, linewidth = 1, marker = '1', color = 'Red', label = 'BL L6', ms = 4)
# GTS Order 6
y = [401, 394, 372, 350]
t = [312, 160, 100, 83]
ax_flops.plot(x, y, linewidth = 1, marker = 's', color = 'Black', label = 'BL G6', ms = 4) 
ax_times.plot(x, t, linewidth = 1, marker = 's', color = 'Black', label = 'BL G6', ms = 4)

# Shaking Corals
# LTS Order 6
y = [1040, 976, 940, 923]
t = [200, 110, 70, 53]
ax_flops.plot(x, y, linewidth = 1, marker = 'h', color = 'Green', label = 'SC L6', ms = 4) 
ax_times.plot(x, t, linewidth = 1, marker = 'h', color = 'Green', label = 'SC L6', ms = 4)
# LTS Order 6 with dynamic rupture
y = [1070, 1000, 956, 940]
ax_flops.plot(x, y, '--', linewidth = 1, marker = 'h', color = 'Green', label = 'SC L6', ms = 4) 
# GTS Order 6
y = [1340, 1176, 1140, 1103]
t = [245, 128, 85, 67]
ax_flops.plot(x, y, linewidth = 1, marker = 'p', color = 'Blue', label = 'SC G6', ms = 4)
ax_times.plot(x, t, linewidth = 1, marker = 'p', color = 'Blue', label = 'SC G6', ms = 4)
# GTS Order 6 with dynamic rupture
y = [1390, 1206, 1204, 1170]
ax_flops.plot(x, y, '--', linewidth = 1, marker = 'p', color = 'Blue', label = 'SC G6', ms = 4) 

ax_times.yaxis.set_label_position('right')
ax_flops.set_xlabel('Sockets (56 cores per socket)')
ax_flops.set_ylabel('GFLOPS per socket')
ax_times.set_xlabel('Sockets (56 cores per socket)')
ax_times.set_ylabel('Extrapolated time (h)')
ax_flops.legend(ncol = 6, prop = {'size': 9}, bbox_to_anchor = (2.3, -0.2))

plt.savefig('scale.eps', format = 'eps', dpi = 1200, bbox_inches = 'tight')
# plt.show()