from numpy import *
from scipy.integrate import odeint
import matplotlib.pyplot as plt 
from matplotlib.backends.backend_pdf import PdfPages

def basic_zombies(y, t, Alpha, Beta, Delta, Pi, Zeta):
    """
    The basic model.
    """
    
    S = y[0]
    Z = y[1]
    R = y[2]

    Sprime = Pi - Beta*S*Z - Delta*Z
    Zprime = Beta*S*Z + Zeta*R - Alpha*S*Z 
    Rprime = Delta*S + Alpha*S*Z - Zeta*R  

    return [Sprime, Zprime, Rprime]

def latent_period(y, t, Alpha, Beta, Delta, Pi, Roh, Zeta):
    """
    Model with latent period.
    """

    S = y[0]
    I = y[1]
    Z = y[2]
    R = y[3]

    Sprime = Pi - Beta*S*Z - Delta*Z
    Iprime = Beta*S*Z - Roh*I - Delta*I 
    Zprime = Roh*I + Zeta*R - Alpha*S*Z 
    Rprime = Delta*S + Delta*I + Alpha*S*Z - Zeta*R 

def treatment(y, t, Alpha, Beta, c, Delta, Pi, Roh, Zeta):
    """
    Model with treatment.
    """

    S = y[0]
    I = y[1]
    Z = y[2]
    R = y[3]

    Sprime = Pi - Beta*S*Z - Delta*Z + c*Z 
    Iprime = Beta*S*Z - Roh*I - Delta*I
    Zprime = Roh*I + Zeta*R - Alpha*S*Z - c*Z 
    Rprime = Delta*S + Delta*I + Alpha*S*Z - Zeta*R
