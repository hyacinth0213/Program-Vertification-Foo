from z3 import *

a = Bool('Netflix subscription')
b = Bool('Ed Sheeran album')
c = Bool('iPhone XR')
d = Bool('Adidas Yeezy Sneakers')
e = Bool('A Song of Ice and Fire book')
f = Bool('tickets for Mark Forster')
g = Bool('selfie stick')
h = Bool('hair straightener')

def build_solver():
	solver = Solver()

	# add constrain condition
	solver.add(Implies(a, Not(b)))
	solver.add(Implies(c, Not(d)))
	solver.add(Implies(e, And(a, f)))

	solver.add(Implies(Not(d),Or(e,g)))
	solver.add(Implies(And(Not(g),h),c))
	solver.add(Implies(h, Not(g)))
	solver.add(Implies(And(Xor(a, d),Not(b)),f))
	solver.add(Implies(And(And(a, Not(c)),f), Not(g)))
	solver.add(Implies(Not(e),h))

	return solver

if __name__ == '__main__':
	solver = build_solver()
	print(solver.check())
	print(solver.model())
