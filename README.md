ZombieAttack
============

A zombie attack modeled in Python. 

## Requirements: 

Python 2 (2.7 or above), NumPy, SciPy, matplotlib

The program consists of one Python file, zombies.py. It can be run from a Unix command line using:

    python zombies.py

The program consists of three different models for a zombie attack: a basic model, a model with a latent period 
in which humans are infected but not zombies, and a model with treatment for zombie-ism. 

The function `basic_zombies(y, t, Alpha, Beta, Delta, Pi, Zeta)` returns a derivative for the vector y
at time t; this can be passed into `scipy.integrate.odeint()` to solve the set of ODEs that represent the 
basic model. The functions `latent_period(y, t, Alpha, Beta, Delta, Pi, Roh, Zeta)` and 
`treatment(y, t, Alpha, Beta, c, Delta, Pi, Roh, Zeta)` do the same task for the two other models. 

For the basic model, the vector y consists of [S, Z, R], where S stands for Susceptibles (humans who are 
not yet zombies but could be), Z stands for Zombies, and R stands for Removed (humans who have died, either
through attacks or natural causes.) 
For the other two models, y consists of [S, I, Z, R]; S, Z and R are same as before, and I 
stands for Infected (humans who have been bitten by a zombie but are not yet zombies).

Alpha, Beta, c, Delta, Pi, Roh, Zeta are all constants in the ODEs. These represent the following:

Alpha -- the rate at which a susceptible can resist becoming a zombie by fighting zombies off 
Beta -- the rate at which a susceptible becomes a zombie via transmission
c -- rate of cure from zombie-ism
Delta -- rate of natural (non-zombie-related) death
Pi -- birth rate
Roh -- rate at which an infected person becomes a zombie
Zeta -- rate at which humans in the removed class resurrect and become zombies

The `run_basic()`, `run_latent()`, and `run_treatment()` functions all solve the respective ODEs using
`scipy.integrate.odeint()` and plot the results using matplotlib.pyplot. Currently, the solutions for 
Susceptibles and Zombies are plotted. The solution for the Removed and Infected classes can be plotted 
using the correct indices in the `solution` variable. 

The values used by the constants are set in the following piece of code:

    if __name__ == '__main__':
        Alpha, Beta, c, Delta, Pi, Roh, Zeta = 0.005, 0.0028, 0.05, 0.0001, 0, 5, 5

These values can be changed and the modified values will be passed into the three `run()` functions.

Each of the three `run()` functions have initial values in a variable called `init` and the time 
range (start time, end time, and time step) in a variable called `times`. The values there can 
be changed to modify the initial conditions and time ranges. Currently, initial values are set 
to 500 (thousand) for Susceptibles, and zero for the others. `times` is (0, 20, 100). 


 



