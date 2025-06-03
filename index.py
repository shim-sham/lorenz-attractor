# dx/dt = σ(y-x) ----> x is proportional to the rate of convection
# dy/dt = x(ρ-z) - y --> y is proportional to the horizontal temperature variation
# dz/dt = xy - βz ---> z is proportional to the vertical temperature variation
# plan:
# - variable number of cups
# - cups spin on a pivot based on how much water
# - rate of flow of water is variable (and also controls speed of cup spin)
# - rate of drainage also affects



import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
