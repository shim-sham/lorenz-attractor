# dx/dt = σ(y-x) ----> x is proportional to the rate of convection
# dy/dt = x(ρ-z) - y --> y is proportional to the horizontal temperature variation
# dz/dt = xy - βz ---> z is proportional to the vertical temperature variation
# plan:
# - variable number of cups
# - cups spin on a pivot based on how much water
# - rate of flow of water is variable (and also controls speed of cup spin)
# - rate of drainage also affects

# Create an initial state vector y0 that includes:
    # Fill level for each bucket
    # The angle (theta)
    # Angular velocity (omega)
# Write a function def waterwheel_ode(t, y): to define how the system changes
# Use solve_ivp() to simulate the system over time
# Plot something simple like theta vs. time to start


import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

n = 5 # just a place holder! remember to change this to an input
fill_rate = 0.5
drain_rate = 0.1
friction = 2
dt = 0.05
sim_time = 30

#initial conditions
y0 = np.zeros(n + 2) #format: [bucket1, bucket2,..., bucketn, theta(angle), omega(anglular v) ]
y0[n] = np.pi / n #theta
y0[n+1] = 0 # stationary


# gotta to find how everything is changing all the time
def derivative(y):
    global n
    theta = y[n+1]
    omega = y[n]
    bucket_water = []
    for i in range(n):
        bucket_water.append(y[i])
    print(bucket_water)

derivative(y0)