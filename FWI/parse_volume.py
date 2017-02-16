import pylab
import numpy as np
import sys

filename = "line23_tomo_model"

output = np.zeros((128,1040,96), dtype=np.int)

with open(filename, 'r') as f:
	for line in f:
		v = np.array([int(a) for a in line.split(',')])
		inline = v[0] - 1
		xline = v[1] - 1
		depths = v[2::2]
		vels = v[3::2]
		output[inline, xline,:] = vels

pylab.imshow(output[64,:,:].T, aspect='auto')
pylab.colorbar()
pylab.show()
