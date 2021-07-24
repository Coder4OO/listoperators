from functools import reduce
import operator

def list_multiply(l):
	return reduce(operator.mul, l)
	
def list_divide(l):
	return reduce(operator.div, l)
	
def list_subtract(l):
	return reduce(operator.sub, l)
	
def list_sum(l):
	return sum(l)
	