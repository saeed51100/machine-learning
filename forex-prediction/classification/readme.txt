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
Given 60 consecutive unseen hourly candles, the model must predict trend reversal points (0, 1, 2) for the next 10 hours immediately following the 60th candle.
Classes: 0=no signal, 1=buy reversal, 2=sell reversal

# --------------------------
Dataset
# --------------------------

1- The DataFrame (df) has 140,000 rows and 10 columns: DATETIME, DATE, TIME, OPEN, HIGH, LOW, CLOSE, TICKVOL, VOL, SPREAD
2- The timeframe is hourly; each row is one hourly candle.
3- The df dataset is continuous with Forex market holiday gaps already filled.
4- The DATETIME column is continuous and serves as the time index.
5- I copied the first 130,000 rows from df into df_model and added a 'Label' column to it. The 'Label' column contains trend reversal points labeled as 0 (no reversal), 1 (buy reversal), or 2 (sell reversal).
6- I will use df_model (130,000 rows) for training, testing, and validation.
7- The remaining 10,000 rows of df (rows 130,001 to 140,000) are completely unseen and will be reserved for real-world testing.
8- Label distribution in df_model is highly imbalanced: [98.55%] are class 0, [0.73%] are class 1, and [0.73%] are class 2.
9- Class weights alone are insufficient for this >98% imbalance — additional imbalance-handling strategies are required.
10- When using df_model for train/test/validation, use chronological splitting: ['first 70% for training, next 15% for validation, last 15% for testing' or 'walk-forward validation'].
11- Our goal is to reproduce the 'Label' column for unseen data.

# --------------------------
Features and hyperparameters (must be used)
# --------------------------

WINDOW_SIZE = 60
FORECAST_HORIZON = 10
FEATURES = ['OPEN','HIGH','LOW','CLOSE','TICKVOL']

# --------------------------
Deliverable
# --------------------------

* Please provide the MODEL SECTION code only. I have already implemented the PREDICTION and VISUALIZATION sections.
Build an efficient and effective time-series classification model (e.g., using TensorFlow/Keras) that, given the last 60 unseen hourly candles, predicts reversal labels (0/1/2) over the next 10 hours.