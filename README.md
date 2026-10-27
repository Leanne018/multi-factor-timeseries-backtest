# Multi-Factor Equity Backtesting: Cross-Sectional Ranking on Networked Time Series

## Project Overview
This empirical project studies return predictability via multi-factor signals.
From a statistical perspective, each asset is treated as a **node** with a daily time series of prices; nodes may have latent dependence, forming a network of time series.

This framework is different from simple threshold trading rules. Instead of triggering actions when one single time series crosses a cutoff, we periodically rank all nodes by time-varying features and select a subset for evaluation.

## Workflow
1. **Data Collection & Cleaning**
   - Source: `yfinance` / `akshare`
   - Data: 3–5 years daily OHLC stock data
   - Output: cleaned CSV dataset, handle missing values and standardisation

2. **Factor Construction (Time-varying features)**
   - Momentum factor: recent price trend
   - Value factor: relative valuation level
   - Volatility factor: local realised variability

3. **Backtesting Logic**
   - Rebalance frequency: **monthly**
   - Rule: rank stocks by factor exposure, long top 10 stocks
   - Weight: equal-weight portfolio

4. **Evaluation Metrics**
   - Annualised return
   - Sharpe ratio
   - Maximum drawdown
   - Benchmark: CSI 300 index

## Statistical Concerns
- Look-ahead bias
- Survivorship bias
- Overfitting to historical samples
All assumptions and limitations will be documented.

## Planned Extension
In later versions, I aim to explore **dependence structure between time-series nodes (network structure)** and test whether incorporating network information improves the stability of factor signals.

## Reproducibility
All Python code, data pipeline, factor calculation and backtest engine are included.
Results and plots will be saved for comparison.

---
### Dependencies
```python
yfinance
pandas
numpy
matplotlib
scipy
