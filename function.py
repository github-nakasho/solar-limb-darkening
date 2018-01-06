
"""===============================================================

function.py 

purpose: define function


2017 Dec. 10: coded by Sho K. NAKAMURA

==============================================================="""



### define function ###

def function(params, x, y):

	residual=y-(params[0]*x+params[1])
	

	return residual

