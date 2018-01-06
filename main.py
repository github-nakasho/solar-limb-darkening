
"""===============================================================

main.py 

purpose: least square fitting for solar limb darkening


2017 Dec. 10: coded by Sho K. NAKAMURA

==============================================================="""


### import some libraries ###

import numpy
from matplotlib import pyplot
from scipy import optimize


### import .py files ###

import function
import common


### compute least square ###

initparam=[0.0, 0.0]
result=optimize.leastsq(function.function, 
						initparam, args=(common.mu, common.obs))


### show numbers ### 

print(str(result[0][0]))
print(str(result[0][1]))


### show result with sin-I/I plot ###

x=numpy.linspace(0.0, 1.0, 100)

pyplot.scatter(common.sin, common.obs)
pyplot.plot(x, result[0][0]*numpy.sqrt(1.0-x*x)+result[0][1])


pyplot.show()


### show result with polar contour ###

theta=numpy.linspace(0, 2*numpy.pi, 100)
r=numpy.linspace(0, 1.0, 100)

r, theta=numpy.meshgrid(r, theta)
z=result[0][0]*numpy.sqrt(1.0-r)+result[0][1]


ax=pyplot.subplot(111, polar=True)
ctf=ax.contourf(theta, r, z, 100, cmap='OrRd_r', vmin=0.4, vmax=1.0)
pyplot.colorbar(ctf)


pyplot.show()

