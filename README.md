# Black-Scholes vs Monte Carlo Option Pricing
A Python implementation for pricing European call options using both analytical (Black–Scholes) and numerical (Monte Carlo) methods. This project demonstrates the convergence of Monte Carlo simulations to the analytical solution and provides statistical confidence intervals for the numerical estimates.
## Project Overview
This Python implementation provides a comparative analysis of two fundamental approaches in financial derivatives pricing: the analytical Black-Scholes model and the numerical Monte Carlo simulation method. The project demonstrates how Monte Carlo methods converge to the theoretical Black-Scholes price as the number of simulated paths increases, offering insights into the trade-offs between computational efficiency and accuracy in quantitative finance.

## Key Objectives
- Compare analytical and numerical pricing methods for European call options
- Demonstrate Monte Carlo convergence properties
- Provide educational insights into quantitative finance techniques
- Offer reusable code for financial modeling and analysis

## Features

### Core Functionality
- **Black-Scholes Formula Implementation**: Exact analytical solution using cumulative normal distribution
- **Monte Carlo Simulation**: Path generation using Geometric Brownian Motion (GBM)
- **Convergence Analysis**: Comparative results across 4 orders of magnitude (1K to 1M paths)
- **Statistical Validation**: 95% confidence interval calculation for Monte Carlo estimates
- **Reproducible Results**: Fixed random seed for consistent outputs

### Advanced Capabilities
- Error analysis and convergence tracking
- Discounted payoff computation with continuous compounding
- Efficient vectorized NumPy operations for performance
- Clean, documented code with mathematical formulas included

## 🛠️ Technical Requirements

### Python Dependencies
```python
numpy >= 1.19.0      # Numerical computations and array operations
scipy >= 1.6.0       # Statistical functions (norm.cdf)
