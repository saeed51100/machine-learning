Please think long and hard.

# --------------------------
Overview
# --------------------------
I am a developer who programs with Python in Jupyter.
I need help writing a Forex time-series classification program.
I'm building a Forex trend reversal classifier using 130,000 hours of historical data with pre-labeled reversal points.

# --------------------------
Goal
# --------------------------
The dataset contains a "Label" column with trend-reversal classes:
0, 1, and 2.
The model should learn patterns that indicate reversal points and reproduce this labeling on unseen data.
Given 120 consecutive unseen hourly candles, the model must predict trend reversal points (0, 1, 2) for the next 5 hours immediately following the 120th candle.
Classes: 0=no signal, 1=buy reversal, 2=sell reversal

# --------------------------
Dataset
# --------------------------

1- The DataFrame (df) has 140,000 rows and 10 columns: DATETIME, DATE, TIME, OPEN, HIGH, LOW, CLOSE, TICKVOL, VOL, SPREAD
2- The timeframe is H1 (hourly); each row is one hour of Forex OHLCV data.
3- The dataset is fully continuous, with all holiday gaps already forward-filled.
4- The DATETIME column is strictly chronological and represents the true time index.
5- I copied the first 130,000 rows from df into df_model and added a 'Label' column to it. The 'Label' column contains trend-reversal labels (0, 1, 2).
6- I will use df_model (130,000 rows) for training, testing, and validation.
7- The remaining 10,000 rows of df (rows 130,001 to 140,000) are completely unseen and will be reserved for real-world testing.
8- The label distribution in df_model is highly imbalanced:
    - Class 0 ≈ 98.55%
    - Class 1 ≈ 0.73%
    - Class 2 ≈ 0.73%
9- Because imbalance is extremely high (>98%), class weights alone are insufficient; additional imbalance-handling strategies are required.
10- When using df_model for train/test/validation, use chronological splitting: ['first 70% for training, next 15% for validation, last 15% for testing' or 'walk-forward validation'].
11- The final goal is to reproduce the 'Label' column for unseen data.

# --------------------------
Features and hyperparameters (must be used)
# --------------------------

WINDOW_SIZE = 120
FORECAST_HORIZON = 5
FEATURES = ['OPEN','HIGH','LOW','CLOSE','TICKVOL']

# --------------------------
All sections
# --------------------------
    1- Load df
    2- Create df_model from df and add the 'label' column
    3- CHRONOLOGICAL SPLITTING
    4- SCALING DATA
    5- IMBALANCE HANDLING
    6- Create sequences (WINDOW_SIZE → X, FORECAST_HORIZON → y)
    7- Build the model
    8- Train the model
    9- Evaluate the model
    10- Run predictions
    11- Visualization
    12- Save trained model, scaler and summary
    13- Load trained model, scaler and summary

# --------------------------
Deliverable
# --------------------------

    Please write me the codes for part 3 and 4 and 5.
    All earlier sections are already completed.


