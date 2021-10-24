from fipy import *
mesh = Grid2D(nx=1000, ny=1000, dx=0.25, dy=0.25)

phi = CellVariable(name=r"$\phi$", mesh=mesh)
phi.setValue(GaussianNoiseVariable(mesh=mesh,
                                   mean=0.5,
                                   variance=0.01))
PHI = phi.getArithmeticFaceValue()
D = a = epsilon = 1.
eq = (TransientTerm() == DiffusionTerm(coeff=D * a**2 * (1 - 6 * PHI * (1 - PHI))) - 
DiffusionTerm(coeff=(D, epsilon**2)))viewer = Viewer(vars=(phi,), datamin=0., datamax=1.)dexp = -5elapsed = 0.while elapsed < 1000.:    dt = min(100, exp(dexp))    elapsed += dt    dexp += 0.01    eq.solve(phi, dt=dt)    viewer.plot()