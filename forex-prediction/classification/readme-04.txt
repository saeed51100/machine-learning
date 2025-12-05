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
Given 64 consecutive unseen hourly candles, the model must predict trend reversal points (0, 1, 2) for the next 10 hours immediately following the 64th candle.
Classes: 0=no signal, 1=buy reversal, 2=sell reversal

# --------------------------
Dataset
# --------------------------

1- The DataFrame (df) has 140,000 rows and 10 columns: DATETIME, DATE, TIME, OPEN, HIGH, LOW, CLOSE, TICKVOL, VOL, SPREAD
2- The timeframe is hourly; each row is one hourly candle.
3- The df dataset is continuous with Forex market holiday gaps already filled.
4- The DATETIME column is continuous and serves as the time index.
5- I copied the first 130,000 rows from df into df_model and added a 'Label' column to it. The 'Label' column contains trend-reversal labels (0, 1, 2).
6- I will use df_model (130,000 rows) for training, testing, and validation.
7- The remaining 10,000 rows of df (rows 130,001 to 140,000) are completely unseen and will be reserved for real-world testing.
8- Label distribution in df_model is highly imbalanced: [98.55%] are class 0, [0.73%] are class 1, and [0.73%] are class 2.
9- Class weights alone are insufficient for this >98% imbalance — additional imbalance-handling strategies are required.
10- When using df_model for train/test/validation, use chronological splitting: ['first 70% for training, next 15% for validation, last 15% for testing' or 'walk-forward validation'].
11- Our goal is to reproduce the 'Label' column for unseen data.

# --------------------------
Features and hyperparameters (must be used)
# --------------------------

WINDOW_SIZE = 64
FORECAST_HORIZON = 10
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
    9- Run predictions

# --------------------------
Deliverable
# --------------------------

    The previous sections are complete. You only need to prepare the following section:
    3-"CHRONOLOGICAL SPLITTING" - split df_model into train/validation/test sets chronologically.



