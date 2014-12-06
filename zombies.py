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

    return [Sprime, Iprime, Zprime, Rprime]

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

    return [Sprime, Iprime, Zprime, Rprime]    

def run_basic(Alpha, Beta, Delta, Pi, Zeta):
    init = [500, 0, 0]
    times = linspace(0,20,100)

    solution = odeint(basic_zombies, init, times, args=(Alpha, Beta, Delta, Pi, Zeta))
    plt.plot(times, solution[:,0], label="Humans (Susceptibles)")
    plt.plot(times, solution[:,1], label="Zombies")
    plt.xlabel("Time")
    plt.ylabel("Population Value (1000s)")
    plt.legend()
    plt.title("The basic model")
    plt.show() 

def run_latent_period(Alpha, Beta, Delta, Pi, Roh, Zeta):
    init = [500, 0, 0, 0]
    times = linspace(0,20,100)
    solution = odeint(latent_period, init, times, args=(Alpha, Beta, Delta, Pi, Roh, Zeta))
    plt.xlabel("Time")
    plt.ylabel("Population Value (1000s)")
    plt.plot(times, solution[:,0], label="Humans (Susceptibles)")
    plt.plot(times, solution[:,2], label="Zombies")
    plt.legend()
    plt.title("Model with latent period")
    plt.show() 

def run_treatment(Alpha, Beta, c, Delta, Pi, Roh, Zeta):
    init = [500, 0, 0, 0]
    times = linspace(0,20,100)
    solution = odeint(treatment, init, times, args=(Alpha, Beta, c, Delta, Pi, Roh, Zeta))
    plt.xlabel("Time")
    plt.ylabel("Population Value (1000s)")
    plt.plot(times, solution[:,0], label="Humans (Susceptibles)")
    plt.plot(times, solution[:,2], label="Zombies")
    plt.title("Model with treatment")
    plt.legend()
    plt.show()     

if __name__ == '__main__':
    Alpha, Beta, c, Delta, Pi, Roh, Zeta = 0.005, 0.0028, 0.05, 0.0001, 0, 5, 5
    run_basic(Alpha, Beta, Delta, Pi, Zeta) 
    run_latent_period(Alpha, Beta, Delta, Pi, Roh, Zeta)
    run_treatment(Alpha, Beta, c, Delta, Pi, Roh, Zeta)