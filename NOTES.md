# Notes & Modelling Assumptions
This document records fixed assumptions, known biases and limitations of the backtesting pipeline.

## Trading Assumptions
- Rebalancing executes at closing price on the rebalance date.
- No transaction cost, slippage or market impact is included in this baseline version.
- Long-only portfolio; short selling is not supported.
- Equal weight is assigned to selected stocks at each rebalance.
- Dividend and corporate action adjustments are not implemented for the initial iteration.

## Potential Biases
1. **Look-ahead bias**: We strictly align feature calculation with timestamp, only using information available before the rebalance date.
2. **Survivorship bias**: The stock universe currently only includes active stocks; delisted stocks will not be included in the dataset.
3. **Overfitting risk**: Multiple factor parameters and ranking thresholds may lead to in-sample overfitting. Out-of-sample testing is required for robustness.

## Known Limitations for Future Improvement
- The universe size is relatively small.
- Factor correlation is not controlled.
- No turnover constraint.
- Benchmark return frequency is matched manually.
