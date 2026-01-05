import numpy as np
from scipy.stats import norm

S0 = 100.0
K = 100.0
T = 2.0
r = 0.05
sigma = 0.2
np.random.seed(0)


def black_scholes_call(S0, K, T, r, sigma):
    d1 = (np.log(S0 / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return S0 * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)


def monte_carlo_call(S0, K, T, r, sigma, n_paths):
    Z = np.random.randn(n_paths)
    ST = S0 * np.exp((r - 0.5 * sigma ** 2) * T + sigma * np.sqrt(T) * Z)
    payoff = np.maximum(ST - K, 0.0)
    price = np.exp(-r * T) * np.mean(payoff)
    return price, payoff


bs_price = black_scholes_call(S0, K, T, r, sigma)

paths = [1_000, 10_000, 100_000, 1_000_000]
results = []

for n in paths:
    mc_price, payoff = monte_carlo_call(S0, K, T, r, sigma, n)
    error = abs(mc_price - bs_price)
    results.append((n, mc_price, error))

mc_price, payoff = monte_carlo_call(S0, K, T, r, sigma, paths[-1])
std_error = np.std(payoff) / np.sqrt(paths[-1])
ci_lower = mc_price - 1.96 * std_error * np.exp(-r * T)
ci_upper = mc_price + 1.96 * std_error * np.exp(-r * T)

print(f"Black–Scholes price: {bs_price:.6f}")
print()
for n, price, error in results:
    print(f"Paths: {n:<8} Monte Carlo price: {price:.6f} | Error: {error:.6f}")
print()
print(f"95% confidence interval (N={paths[-1]}): [{ci_lower:.6f}, {ci_upper:.6f}]")