#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 20:11:18 2026

@author: nileyan
"""

# example_run.py
# Demo script: show how to import and use functions from utils.py
# This is only for demonstration, not full backtest

import pandas as pd
import numpy as np
import utils

if __name__ == "__main__":
    # create a tiny simulated panel for test
    test_data = pd.DataFrame({
        "A": [1.1, 1.3, 1.2, 1.5],
        "B": [0.9, 1.0, 1.4, 1.1],
        "C": [1.2, 1.1, 1.3, 1.6]
    }, index=pd.date_range("2025-01-01", periods=4))

    df_clean = utils.preprocess_raw_data(test_data)
    print("Cleaned test data:\n", df_clean)

    # demo cross-sectional zscore on one single date
    single_slice = df_clean.iloc[0]
    z = utils.calculate_feature_zscore(single_slice)
    print("\nCross-sectional z-score example:\n", z)
