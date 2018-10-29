import numpy as np
import matplotlib.pyplot as plt

# io_type = ('Synchronous I/O', 'I/O thread', 'Direct I/O')
io_time = [15.6, 6.4, 2]

ind = np.arange(len(io_time))
width = 0.5

fig, ax = plt.subplots(figsize = (6, 3))

rects = []

rects.append(ax.barh(ind[0], io_time[0], width, color =   'SkyBlue', label = 'Synchronous I/O')[0])
rects.append(ax.barh(ind[1], io_time[1], width, color = 'IndianRed', label =      'I/O thread')[0])
rects.append(ax.barh(ind[2], io_time[2], width, color =      'Pink', label =      'Direct I/O')[0])

ax.set_yticks(ind)
ax.invert_yaxis()
ax.set_xlabel('Time(s)')
ax.legend()

def getmaxof(rects):
	ret = 0
	for rect in rects:
		ret = max(ret, rect.get_width())
	return ret

def autolabel(rect, maxh = 0.2):
	width = rect.get_width()
	ax.text(width - maxh, rect.get_y() + rect.get_height() * 0.5, '%.1f' % width, va = 'center', ha = 'center', fontsize = 10, color = 'Black')

maxh = getmaxof(rects) * 0.06
for rect in rects: autolabel(rect, maxh)

plt.savefig('async.eps', format = 'eps', dpi = 1200, bbox_inches = 'tight')
# plt.show()