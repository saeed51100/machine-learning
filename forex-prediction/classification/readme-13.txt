Please think long and hard.

--------------------------
Overview
--------------------------
I am building a Forex time-series classification model in Python/Jupyter.
The goal is to detect trend-reversal points using 130,000 hours of labeled historical H1 data.

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



--------------------------
Required hyperparameters
--------------------------
WINDOW_SIZE = 120
FORECAST_HORIZON = 5
FEATURES = ['OPEN','HIGH','LOW','CLOSE','TICKVOL']

# --------------------------
All sections
# --------------------------
    1- Create df_model from df and add the 'label' column
    2- CHRONOLOGICAL SPLITTING
    3- SCALING DATA
    4- Create sequences (WINDOW_SIZE → X, FORECAST_HORIZON → y)
    5- IMBALANCE HANDLING ( Class-weighted )
    6- Build, Train and Evaluate the model

--------------------------
Completed sections (1–3)
--------------------------
I have done the following steps:
    1- Create df_model from df and add the 'label' column
    2- CHRONOLOGICAL SPLITTING
    3- SCALING DATA


--------------------------
VARIABLES (ready for PART 4: Create sequences)
--------------------------
...


--------------------------
Your task
--------------------------
Write the full code only part 4 (Create sequences).

    Additional Requirements:
        - At the end of the code, print the variables required for part 5 (IMBALANCE HANDLING).

