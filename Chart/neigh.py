import numpy as np
import matplotlib.pyplot as plt

bl = [0, 0, 0, 0]
bl16 = [0, 0, 0, 0]
sc = [0, 0, 0, 0]

bl_time = [1 / 1.00, 1 / 1.00, 1 / 1.00, 1 / 1.00]
bl16_time = [1 / 1.00, 1 / 1.02, 1 / 1.03, 1 / 1.06]
sc_time = [1 / 1.02, 1 / 1.07, 1 / 1.26, 1 / 1.81]

o_bl = [1.00, 1.00, 1.00, 1.00]
o_bl16 = [1.00, 1.02, 1.03, 1.06]
o_sc = [1.02, 1.07, 1.26, 1.81]

for i in range(0, 4):
	bl[i] =  bl_time[i] / bl_time[i]
	bl16[i] =  bl_time[i] / bl16_time[i]
	sc[i] = bl_time[i] / sc_time[i]

ind = np.arange(len(bl))  # the x locations for the groups
width = 0.2  # the width of the bars

fig, ax = plt.subplots(figsize = (6, 3))
# plt.subplots_adjust(right = 0.91)
ax.plot([0 - width, 1 - width, 2 - width, 3 - width], o_bl, linewidth = 0, marker = '1', color = 'Black')
rects1 = ax.bar(ind - width * 1.0,   bl, width, color =   'SkyBlue', label =   'BL')

ax.plot([0, 1, 2, 3], o_bl16, linewidth = 0, marker = '1', color = 'Black')
rects2 = ax.bar(ind - width * 0.0, bl16, width, color = 'IndianRed', label = 'BL16')

ax.plot([0 + width, 1 + width, 2 + width, 3 + width], o_sc, linewidth = 0, marker = '1', color = 'Black')
rects3 = ax.bar(ind + width * 1.0,   sc, width, color =      'Pink', label =   'SC')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Speedup')
ax.set_xticks(ind)
ax.set_xticklabels(('O4', 'O5', 'O6', 'O7'))
ax.legend()

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

maxh = 0
maxh = max(maxh, getmaxof(rects1))
maxh = max(maxh, getmaxof(rects2))
maxh = max(maxh, getmaxof(rects3))
maxh *= 0.15

autolabel(rects1, 'center', maxh)
autolabel(rects2, 'center', maxh)
autolabel(rects3, 'center', maxh)

plt.savefig('neigh.eps', format = 'eps', dpi = 1200, bbox_inches = 'tight')
# plt.show()