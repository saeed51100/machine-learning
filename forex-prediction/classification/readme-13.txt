Please think long and hard.

--------------------------
Overview
--------------------------
This is PART 3 of a multi-part Forex time-series classification pipeline implemented in Python/Jupyter.
You must assume that PARTS 1-2 are already been completed correctly and only write the code for PART 3.
The overall goal is to detect price trend-reversal points in labeled historical H1 Forex data.

--------------------------
Goal
--------------------------
The dataset contains a 'CLOSE' price column and a corresponding 'Label' column that indicates price trend-reversal events with three classes:
0: no reversal
1: bullish reversal
2: bearish reversal

The labels 1 and 2 mark the beginning and end of the price trend (peaks and valleys) and the rest are marked with 0. So most of the rows in the dataset have labels 0 and there are very few 1 and 2.

The model should learn patterns that indicate reversal points and reproduce this labeling on unseen data.
Given 120 consecutive hourly candles as input, the model must predict price trend reversal points (0, 1, 2) for the next 5 hours immediately following the 120th candle.

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
    6- Build, Train and Evaluate the model

--------------------------
Completed parts
--------------------------
I have done the following parts:
    1- Create df_model from df and add the 'Label' column
    2- Chronological splitting of df_model

--------------------------
VARIABLES FROM PREVIOUS PART
--------------------------
...

--------------------------
Your task
--------------------------
Write the full code only for the following parts:
    3- Scaling using only training data

    * additional requirements:
        At the end of the code, print the variables required for part 4 (Create sequences).