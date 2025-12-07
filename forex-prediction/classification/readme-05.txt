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
    9- Run predictions

# --------------------------
Deliverable
# --------------------------

    You do not need to write all previous sections.
    All earlier sections are already completed.

    You must prepare only the following part:
    4- SCALING DATA

    The output report for step 3 is as follows:
CHRONOLOGICAL SPLIT SUMMARY
***********************************************************************

Total samples: 146356
Requested proportions (TRAIN/VAL/TEST): 70% / 15% / 15%

SPLIT SIZES (absolute)
------------------------------------------------------------
TRAIN  : 102449 samples  (indices [0 : 102448])
VAL    : 21953 samples  (indices [102449 : 124401])
TEST   : 21954 samples  (indices [124402 : 146355])

SPLIT TIME RANGES (DATETIME)
------------------------------------------------------------
TRAIN  : 2008-11-28 00:00:00  -->  2020-08-05 16:00:00
VAL    : 2020-08-05 17:00:00  -->  2023-02-06 09:00:00
TEST   : 2023-02-06 10:00:00  -->  2025-08-09 03:00:00

SPLIT SIZES (percent of total)
------------------------------------------------------------
TRAIN  : 69.9999%
VAL    : 14.9997%
TEST   : 15.0004%

LABEL DISTRIBUTIONS (column = 'Label')
------------------------------------------------------------
TRAIN LABEL DISTRIBUTION (counts and %):
        count  percentage
Label
0      101109      98.692
1         670       0.654
2         670       0.654

VAL LABEL DISTRIBUTION (counts and %):
       count  percentage
Label
0      21548     98.1551
1        202      0.9201
2        203      0.9247

TEST LABEL DISTRIBUTION (counts and %):
       count  percentage
Label
0      21572       98.26
1        191        0.87
2        191        0.87

***********************************************************************

Please also have step 4 produce a report that I can use in designing the next question.






