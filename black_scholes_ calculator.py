import numpy as np
from scipy.stats import norm


def black_scholes(St, k, r, sigma, t, type='call'):
    d1 = (np.log(St / k) + (r + sigma ** 2 / 2) * t) / (sigma * np.sqrt(t))
    d2 = d1 - sigma * np.sqrt(t)

    if type.lower() == 'call':
        C = norm.cdf(d1) * St - norm.cdf(d2) * k * np.exp(-r * t)
        return C

    elif type.lower() == 'put':
        P = (norm.cdf(-d2) * k * np.exp(-r * t)) - (norm.cdf(-d1) * St)
        return P

    else:
        raise ValueError("Incorrect Options Price - Please enter 'call' or 'put'")


try:
    S = float(input("Current Stock Price: "))
    k = float(input("Strike Price: "))
    r = float(input("Risk Free Rate (as a whole number):  ")) / 100
    sigma = float(input("Volatility (as a whole number):  ")) / 100
    t = float(input("Time to Expiration in Years:  "))
    option_type = str(input("Options Type - Enter 'call' or 'put': ")).strip()

    results = black_scholes(St=S, k=k, r=r, sigma=sigma, t=t, type=option_type)
    print(f"Options Price: {round(results, 2)}")

except ValueError as e:
    print(f"Input Error: {e}")
