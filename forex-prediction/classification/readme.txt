Please think long and hard.

# --------------------------
Overview
# --------------------------
I am a developer and I program with Python in Jupyter.
I want you to help me write a Forex time-series classification program.
I'm building a Forex trend reversal classifier using 130,000 hours of historical data with pre-labeled reversal points.

# --------------------------
Goal
# --------------------------
The dataset contains a "Label" column with trend reversal classifications:
0, 1, and 2.
The model must learn the patterns that indicate trend reversal points and accurately reproduce this labeling behavior on unseen data.
Given 60 consecutive unseen hourly candles, the model should predict trend reversal points (0, 1, 2) for the next 10 hours immediately following the 60th candle.
Classes: 0=no signal, 1=buy reversal, 2=sell reversal

# --------------------------
Dataset
# --------------------------

1- The df dataset has 140,000 rows and 10 columns: DATETIME, DATE, TIME, OPEN, HIGH, LOW, CLOSE, TICKVOL, VOL, SPREAD
2- The timeframe is one hour, with each row representing one hourly candle.
3- The df dataset is continuous with Forex market holiday gaps already filled.
4- The DATETIME column is continuous and serves as the time index.
5- I have copied the first 130,000 rows from df into df_model and added a 'Label' column to it. The 'Label' column contains trend reversal points labeled as 0 (no reversal), 1 (buy reversal), or 2 (sell reversal).
6- I use df_model (130,000 rows) for training, testing, and validation.
7- The remaining 10,000 rows of df (rows 130,001 to 140,000) represent completely unseen data and will be used to test the model's real-world prediction capability.
8- In the df_model Label column, the distribution is approximately: [98.55%] are class 0, [0.73%] are class 1, and [0.73%] are class 2.
9- Class weights alone do not work for >98% imbalance.You must implement additional strategies for class imbalance.
10- When using df_model for train/test/validation, use chronological splitting: ['first 70% for training, next 15% for validation, last 15% for testing' or 'walk-forward validation'].
11- Our goal is to reproduce the 'Label' column for unseen data.

# --------------------------
Features and hyperparameters (must be used)
# --------------------------

WINDOW_SIZE = 60
FORECAST_HORIZON = 10
FEATURES = ['OPEN','HIGH','LOW','CLOSE','TICKVOL']

# --------------------------
Deliverable (when you write the code)
# --------------------------

*  Build an efficient, effective classification model that predicts reversal points (0/1/2) over the 10-hour horizon given after the last 60 hourly unseen candles. (you may use TensorFlow/Keras).
    - Just write me the code for the model section: "MODEL SECTION";I have already written the "PREDICTION" and "VISUALATION" sections.


