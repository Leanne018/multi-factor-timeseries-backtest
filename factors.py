#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 11:20:54 2026

@author: nileyan
"""

# factors.py
# Factor signal construction: momentum, value, volatility

import pandas as pd

def calc_momentum_factor(price_series: pd.DataFrame, lookback: int) -> pd.DataFrame:
    """
    Calculate cross-sectional momentum factor.
    Parameters
    ----------
    price_series : pd.DataFrame
        Adjusted close price panel, index=date, columns=assets
    lookback : int
        Lookback window for momentum
    Returns
    -------
    pd.DataFrame
        Momentum factor values
    """
    # TODO: implement momentum calculation
    pass


def calc_vol_factor(price_series: pd.DataFrame, window: int) -> pd.DataFrame:
    """
    Calculate realised volatility factor.
    """
    # TODO: implement volatility calculation
    pass


def calc_value_factor(price_series: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate value-related signal.
    """
    # TODO: implement value factor
    pass
