# European Call Option Pricing: Black-Scholes vs Monte Carlo Simulation

This Python script compares the price of a European call option calculated using the **Black–Scholes formula** and a **Monte Carlo simulation**. It also estimates the 95% confidence interval of the Monte Carlo price.

## Features

- Computes the analytical Black–Scholes price of a European call option.
- Performs Monte Carlo simulations for multiple numbers of paths.
- Calculates absolute errors between Monte Carlo and Black–Scholes prices.
- Computes a 95% confidence interval for the Monte Carlo estimate.

## Requirements

- Python 3.8+
- NumPy
- SciPy

Install the required packages with:

```bash
pip install numpy scipy
