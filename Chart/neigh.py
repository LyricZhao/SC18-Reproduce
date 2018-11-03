import numpy as np
import matplotlib.pyplot as plt
from proxy_reader import read_result

bl = [0, 0, 0, 0]
bl16 = [0, 0, 0, 0]
sc = [0, 0, 0, 0]
sc_ht56 = [0, 0, 0, 0]
sc_ht112 = [0, 0, 0, 0]

bl_time = np.array([read_result('./figs/fig2/bl_skx_%d.log' % i)['time'] for i in range(4, 8)])
bl16_time = np.array([read_result('./figs/fig2/bl16_skx_%d.log' % i)['time'] for i in range(4, 8)])
sc_time = np.array([read_result('./figs/fig2/sc_skx_%d.log' % i)['time'] for i in range(4, 8)])
sc_ht56_time = np.array([read_result('./figs/fig2/sc_ht56_skx_%d.log' % i)['time'] for i in range(4, 8)])
sc_ht112_time = np.array([read_result('./figs/fig2/sc_ht112_skx_%d.log' % i)['time'] for i in range(4, 8)])

o_bl = [''] * 4
o_bl16 = [''] * 4
o_sc = [''] * 4
o_sc_ht56 = [''] * 4
o_sc_ht112 = [''] * 4



for i in range(4):
    bl[i] =  bl_time[i] / bl_time[i]
    o_bl[i] = float('%.2f' % bl[i])
    bl16[i] =  bl_time[i] / bl16_time[i]
    o_bl16[i] = float('%.2f' % bl16[i])
    sc[i] = bl_time[i] / sc_time[i]
    o_sc[i] = float('%.2f' % sc[i])
    sc_ht56[i] = bl_time[i] / sc_ht56_time[i]
    o_sc_ht56[i] = float('%.2f' % sc_ht56[i])
    sc_ht112[i] = bl_time[i] / sc_ht112_time[i]
    o_sc_ht112[i] = float('%.2f' % sc_ht112[i])

ind = np.arange(len(bl))  # the x locations for the groups
width = 0.15  # the width of the bars
real_width = width * 0.9

colors = ['SkyBlue', 'Cyan', 'Pink', 'Orange', 'IndianRed']

fig, ax = plt.subplots(figsize = (6, 3))
# plt.subplots_adjust(right = 0.91)
ax.plot([i - width * 2 for i in range(4)], o_bl, linewidth = 0, marker = '1', color = 'Black')
rects1 = ax.bar(ind - width * 2.0,   bl, real_width, color=colors[0], label =   'BL')

ax.plot([i - width * 1 for i in range(4)], o_bl16, linewidth = 0, marker = '1', color = 'Black')
rects2 = ax.bar(ind - width * 1.0, bl16, real_width, color=colors[1], label = 'BL16')

ax.plot([i + width * 0 for i in range(4)], o_sc, linewidth = 0, marker = '1', color = 'Black')
rects3 = ax.bar(ind + width * 0.0,   sc, real_width, color=colors[2], label =   'SC')

ax.plot([i + width * 1 for i in range(4)], o_sc_ht56, linewidth = 0, marker = '1', color = 'Black')
rects4 = ax.bar(ind + width * 1.0,   sc_ht56, real_width, color=colors[3], label =   'SC_ht56')

ax.plot([i + width * 2 for i in range(4)], o_sc_ht112, linewidth = 0, marker = '1', color = 'Black')
rects5 = ax.bar(ind + width * 2.0,   sc_ht112, real_width, color=colors[4], label =   'SC_ht112')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Speedup')
ax.set_xticks(ind)
ax.set_xticklabels(('O4', 'O5', 'O6', 'O7'))
ax.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=4,
        ncol=3, mode="expand", borderaxespad=0.)

def autolabel(rects, xpos = 'center', maxh = 0.2):
    xpos = xpos.lower()  # normalize the case of the parameter
    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}  # x_txt = x + w*off

    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() * offset[xpos], height - maxh, '%.2f' % height, ha = ha[xpos], va = 'bottom', fontsize = 9, rotation = 90.)

def getmaxof(rects):
	ret = 0
	for rect in rects:
		ret = max(ret, rect.get_height())
	return ret

rects = [rects1, rects2, rects3, rects4, rects5]
maxh = max([getmaxof(rect) for rect in rects]) * .15
for rect in rects:
    autolabel(rect, 'center', maxh)

plt.savefig('neigh.eps', format = 'eps', dpi = 1200, bbox_inches = 'tight')
# plt.show()
