# *** Material Properties ***
nu=0.305 # Poisson's Ratio taken from Edupack
E=35.3 # Young's Modulus taken from EasyComposites

# *** Ideal Gas Law ***
N=24 # mol/l at RTP
T=200 # °C
R=0.08314 # l.bar/K/mol

# *** Pressure at sea level ***
P0= 1.013 #in bar

# *** Tube Dimensions ***
L=1420 # Length of aft tube in mm
ODa=130 # Outer diameter of aft tube in mm
ODm=100 #Outer diameter of motor tube in mm
t=2 # Thickness of aft tube in mm

# *** Miscalleneous ***


# *** Calculations ***
V=L*3.142/4*((ODa-2*t)^2-ODm^2)
n=V/N
P=(n*R*(T+273))/V+P0 #Pressure is in bar, and is for the worst case scenario

U1=(E*1000)/((1+nu)*(1-2*nu)) # Finding the multiplicator of the matrix

K=[[U1*(1-nu), U1*nu, U1*nu, 0], # Calculating the global stiffness matrix for an axissymmetric system
[U1*nu, U1*(1-nu), U1*nu, 0],
[U1*nu, U1*nu, U1*(1-nu), 0],
[0, 0, 0, U1*(1-2*nu)/2]]

F=[[-0.1*P], #Finding the stresses applying on the system
[0.1*P*ODa/(2*t)],
[0.1*P*ODa/(4*t)],
[0]]

# U=K^-1*F? #Finding the displacement caused from the internal pressure