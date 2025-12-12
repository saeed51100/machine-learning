Please think long and hard.

--------------------------
Overview
--------------------------
I am building a Forex time-series classification model in Python/Jupyter.
The goal is to detect trend-reversal points using 130,000 hours of labeled historical H1 data.

--------------------------
Goal
--------------------------
The model must:
    - Use 120 past candles to predict 5 future labels (0=no signal, 1=buy reversal, 2=sell reversal).
    - The task is to reproduce the "Label" column on unseen data.

--------------------------
Dataset
--------------------------

df has 140,000 rows, columns:
DATETIME, DATE, TIME, OPEN, HIGH, LOW, CLOSE, TICKVOL, VOL, SPREAD
Hourly timeframe (H1), fully continuous.
First 130,000 rows → df_model, with an added Label column (0/1/2).
Rows 130,001–140,000 are completely unseen test data.
Labels are highly imbalanced:
class 0: 98.55%
class 1: 0.73%
class 2: 0.73%

Must use chronological splitting for train/val/test (70/15/15 or walk-forward).

--------------------------
Required hyperparameters
--------------------------
WINDOW_SIZE = 120
FORECAST_HORIZON = 5
FEATURES = ['OPEN','HIGH','LOW','CLOSE','TICKVOL']

--------------------------
Completed Steps (1–2)
--------------------------
I have done the following steps:
1- Load df
2- Create df_model from df and add the 'label' column


--------------------------
Your task
--------------------------
Write the full code for:
    3- Chronological splitting of df_model
    4- Scaling using only training data

At the end of the code, print the variables required for part 5 (Imbalance handling).

--------------------------
Deliverable
--------------------------

Provide clean, complete Python code for parts 3, 4, and 5 only.

