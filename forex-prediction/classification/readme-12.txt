Please think long and hard.

--------------------------
Overview
--------------------------
This is PART 2 of a multi-part Forex time-series classification pipeline implemented in Python/Jupyter.
You must assume that PART 1 are already been completed correctly and only write the code for PART 2.
The overall goal is to detect price trend regimes in labeled historical H1 Forex data.

--------------------------
Goal
--------------------------
The dataset contains a 'CLOSE' price column and a corresponding 'Label' column that indicates price trend events with three classes:
    0 → No meaningful trend (sideways / flat movement)
    1 → Bullish trend
    2 → Bearish trend

The model should learn patterns that indicate trend points and reproduce this labeling on unseen data.
Given 72 consecutive hourly candles as input, the model must predict price trend points (0, 1, 2) for the next 36 hours immediately following the 72th candle.

The prediction output therefore consists of a sequence of 5 labels, where:
0 = no signal
1 = buy (bullish reversal)
2 = sell (bearish reversal)

--------------------------
Dataset
--------------------------

1- The DataFrame (df) has 140,000 rows and 10 columns: DATETIME, DATE, TIME, OPEN, HIGH, LOW, CLOSE, TICKVOL, VOL, SPREAD
2- The timeframe is H1 (hourly); each row is one hour of Forex OHLCV data.
3- The dataset is fully continuous, with all holiday gaps already forward-filled.
4- The DATETIME column is strictly chronological and represents the true time index.
5- The first 130,000 rows of df were copied into df_model, and a 'Label' column was added.
    The 'Label' column contains price trend-reversal labels:
        0: no reversal
        1: bullish reversal
        2: bearish reversal.
6- df_model (130,000 rows) will be used for training, validation, and testing.
7- The remaining 10,000 rows of df (rows 130,001 to 140,000) are completely unseen and reserved for real-world testing.
8- Label distribution in df_model is highly imbalanced:
    - Class 0 ≈ 98.55%
    - Class 1 ≈ 0.73%
    - Class 2 ≈ 0.73%
9- When splitting df_model, strict chronological splitting must be used:
    - Either 70% train / 15% validation / 15% test, or
    - Walk-forward validation
    - No shuffling is allowed
10- The final objective is to reproduce the 'Label' column on unseen data.

--------------------------
Required hyperparameters
--------------------------
WINDOW_SIZE = 120
FORECAST_HORIZON = 5
FEATURES = ['OPEN','HIGH','LOW','CLOSE','TICKVOL']


# --------------------------
All Pipeline Parts
# --------------------------
    1- Create df_model from df and add the 'Label' column
    2- CHRONOLOGICAL SPLITTING
    3- SCALING DATA
    4- Create sequences (WINDOW_SIZE → X, FORECAST_HORIZON → y)
    5- IMBALANCE HANDLING ( Class-weighted )
    6- Build and Train the model

--------------------------
Completed part
--------------------------
I have done the following part:
    1- Create df_model from df and add the 'Label' column

--------------------------
VARIABLES FROM PREVIOUS PART
--------------------------
df_model

--------------------------
Your task
--------------------------
Write the full code only for the following part:
    2- Chronological splitting of df_model

    * additional requirements:
        At the end of the code, print the variables required for part 3 (SCALING DATA).

