#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 17:36:24 2026

@author: nileyan
"""

import pandas as pd
import numpy as np


def preprocess_raw_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    General preprocessing pipeline for time-series panel data.
    Handle missing observations and align timestamps across multiple series.

    Parameters
    ----------
    df : pd.DataFrame
        Panel dataframe, index = date, columns = different assets

    Returns
    -------
    pd.DataFrame
        Cleaned dataframe
    """
    df = df.sort_index()
    df = df.dropna(how="all")
    return df


def calculate_feature_zscore(group: pd.DataFrame) -> pd.Series:
    """
    Cross-sectional standardisation for time-varying features.
    Computed per timestamp to allow ranking across assets.
    This is grouped by each single date.

    Parameters
    ----------
    group : pd.DataFrame
        One time slice (single date) of feature values across assets

    Returns
    -------
    pd.Series
        Z-score normalized feature values
    """
    return (group - group.mean()) / group.std()


def form_long_portfolio(ranked: pd.DataFrame, top_k: int) -> pd.DataFrame:
    """
    Select top-ranked assets and assign equal weights.

    Parameters
    ----------
    ranked : pd.DataFrame
        Dataframe with assets sorted by feature value
    top_k : int
        Number of top assets to pick

    Returns
    -------
    pd.DataFrame
        Subset with equal weight column added
    """
    selected = ranked.head(top_k).copy()
    selected["weight"] = 1 / len(selected)
    return selected


def calculate_performance_metrics(series: pd.Series, risk_free: float = 0.02) -> dict:
    """
    Basic performance statistics: annualised return, max drawdown, Sharpe ratio.
    You can call this after you compute portfolio cumulative return.

    Parameters
    ----------
    series : pd.Series
        Cumulative wealth / net value series, daily or monthly
    risk_free : float
        Annual risk-free rate, default 2%

    Returns
    -------
    dict
        Dictionary of metrics
    """
    # daily return
    ret = series.pct_change().dropna()
    trading_days = 252

    ann_return = (1 + ret.mean()) ** trading_days - 1

    # max drawdown
    running_max = series.cummax()
    drawdown = series / running_max - 1
    max_dd = drawdown.min()

    # sharpe
    ann_vol = ret.std() * np.sqrt(trading_days)
    sharpe = (ann_return - risk_free) / ann_vol if ann_vol != 0 else np.nan

    return {
        "annualised_return": ann_return,
        "max_drawdown": max_dd,
        "sharpe_ratio": sharpe
    }
