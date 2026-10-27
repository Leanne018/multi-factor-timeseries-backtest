# Multi-Factor Equity Backtesting: Cross-Sectional Ranking on Networked Time Series

## Project Overview
This empirical project studies return predictability via multi-factor signals.
From a statistical perspective, each asset is treated as a **node** with a daily time series of prices; nodes may have latent dependence, forming a network of time series.

This framework is different from simple threshold trading rules. Instead of triggering actions when one single time series crosses a cutoff, we periodically rank all nodes by time-varying features and select a subset for evaluation.

## Methodology Overview
This repository implements a reproducible empirical pipeline for studying time-varying predictive signals across a collection of asset time series. Each asset can be treated as a node within a network, where individual series may share latent dependence with one another.

The workflow follows a standard empirical research sequence: data acquisition, cleaning and alignment, feature construction, periodic cross-sectional ranking, portfolio formation, and out-of-sample performance evaluation.

Features are computed only from information available at each historical timestamp to avoid forward information leakage. At each rebalancing date, assets are sorted by their feature values, and a subset is selected to form a simple equal-weight portfolio. The portfolio trajectory is tracked over time and compared against a broad market benchmark series.

The evaluation includes standard time-series performance statistics. Special attention is paid to well-known statistical limitations of this type of study: look-ahead bias, survivorship bias, and the risk of overfitting to historical samples. All modelling assumptions are documented for reproducibility.

This implementation is intentionally lightweight and modular. It separates data loading, feature calculation, portfolio simulation, and performance reporting into distinct components. The modular design allows later extensions, including the introduction of estimated dependence structures between the time-series nodes.

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
