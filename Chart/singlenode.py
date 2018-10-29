import numpy as np
import matplotlib.pyplot as plt

bl_gf = [340, 463, 558, 564]
sc_gf = [356, 443, 553, 522]

bl_su = [0, 0, 0, 0]
sc_su = [0, 0, 0, 0]

bl_time = [1 / 1.00, 1 / 1.00, 1 / 1.00, 1 / 1.00]
sc_time = [1 / 1.02, 1 / 1.07, 1 / 1.26, 1 / 1.81]

for i in range(0, 4):
	bl_su[i] =  bl_time[i] / bl_time[i]
	sc_su[i] = bl_time[i] / sc_time[i]

ind = np.arange(len(bl_su))  # the x locations for the groups
width = 0.2  # the width of the bars

fig, axs = plt.subplots(2, 1, figsize = (6, 5))
# plt.subplots_adjust(right = 0.91)
ax_gf = axs[0]
ax_su = axs[1]

rects1 = ax_gf.bar(ind - width * 0.5,   bl_gf, width, color =   'SkyBlue', label =   'BL')
rects2 = ax_gf.bar(ind + width * 0.5,   sc_gf, width, color =      'Pink', label =   'SC')

rects3 = ax_su.bar(ind - width * 0.5,   bl_su, width, color =   'SkyBlue', label =   'BL')
rects4 = ax_su.bar(ind + width * 0.5,   sc_su, width, color =      'Pink', label =   'SC')

ax_gf.set_ylabel('GFLOPS')
ax_gf.set_xticks(ind)
ax_gf.set_xticklabels(('O4', 'O5', 'O6', 'O7'))
ax_gf.legend()

ax_su.set_ylabel('Speedup')
ax_su.set_xticks(ind)
ax_su.set_xticklabels(('O4', 'O5', 'O6', 'O7'))
ax_su.legend()

def autolabel(ax, rects, fm, xpos='center', maxh = 0.2):
    xpos = xpos.lower()  # normalize the case of the parameter
    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}  # x_txt = x + w*off

    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() * offset[xpos], height - maxh, fm % height, ha = ha[xpos], va = 'bottom', fontsize = 9, rotation = 90.)

def getmaxof(rects):
	ret = 0
	for rect in rects:
		ret = max(ret, rect.get_height())
	return ret

def do_label(ax, fm, rectsA, rectsB):
	maxh = 0
	maxh = max(maxh, getmaxof(rectsA))
	maxh = max(maxh, getmaxof(rectsB))
	maxh *= 0.2
	autolabel(ax, rectsA, fm, 'center', maxh)
	autolabel(ax, rectsB, fm, 'center', maxh)

do_label(ax_gf, '%.0f', rects1, rects2)
do_label(ax_su, '%.2f', rects3, rects4)


plt.savefig('singlenode.eps', format = 'eps', dpi = 1200, bbox_inches = 'tight')
# plt.show()