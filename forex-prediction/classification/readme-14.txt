Please think long and hard.

--------------------------
Overview
--------------------------
This is PART 4 of a multi-part Forex time-series classification pipeline in Python/Jupyter.
You must assume that PARTS 1~3 are already completed correctly.
The goal is to detect trend-reversal points of labeled historical H1 data.

--------------------------
Goal
--------------------------
The dataset contains a "Label" column with trend-reversal classes:
0: no reversal
1: bullish reversal
2: bearish reversal

The model should learn patterns that indicate reversal points and reproduce this labeling on unseen data.
Given 120 consecutive unseen hourly candles, the model must predict trend reversal points (0, 1, 2) for the next 5 hours immediately following the 120th candle.
Classes: 0=no signal, 1=buy reversal, 2=sell reversal

--------------------------
Dataset
--------------------------
1- The DataFrame (df) has 140,000 rows and 10 columns: DATETIME, DATE, TIME, OPEN, HIGH, LOW, CLOSE, TICKVOL, VOL, SPREAD
2- The timeframe is H1 (hourly); each row is one hour of Forex OHLCV data.
3- The dataset is fully continuous, with all holiday gaps already forward-filled.
4- The DATETIME column is strictly chronological and represents the true time index.
5- I copied the first 130,000 rows from df into df_model and added a 'Label' column to it.
    The 'Label' column contains trend-reversal labels:
        0: no reversal
        1: bullish reversal
        2: bearish reversal.
6- I will use df_model (130,000 rows) for training, testing, and validation.
7- The remaining 10,000 rows of df (rows 130,001 to 140,000) are completely unseen and will be reserved for real-world testing.
8- The label distribution in df_model is highly imbalanced:
    - Class 0 ≈ 98.55%
    - Class 1 ≈ 0.73%
    - Class 2 ≈ 0.73%
9- When using df_model for train/test/validation, use chronological splitting: ['first 70% for training, next 15% for validation, last 15% for testing' or 'walk-forward validation'].
10- The final goal is to reproduce the 'Label' column for unseen data.


--------------------------
Required hyperparameters
--------------------------
WINDOW_SIZE = 120
FORECAST_HORIZON = 5
FEATURES = ['OPEN','HIGH','LOW','CLOSE','TICKVOL']

# --------------------------
All parts
# --------------------------
    1- Create df_model from df and add the 'label' column
    2- CHRONOLOGICAL SPLITTING
    3- SCALING DATA
    4- Create sequences (WINDOW_SIZE → X, FORECAST_HORIZON → y)
    5- IMBALANCE HANDLING ( Class-weighted )
    6- Build, Train and Evaluate the model

--------------------------
Completed parts (1~3)
--------------------------
I have done the following parts:
    1- Create df_model from df and add the 'label' column
    2- CHRONOLOGICAL SPLITTING
    3- SCALING DATA


--------------------------
VARIABLES FROM PREVIOUS PART
--------------------------
...


--------------------------
Your task
--------------------------
Write the full code only part 4 (Create sequences).

    Additional Requirements:
        - At the end of the code, print the variables required for part 5 (IMBALANCE HANDLING).

