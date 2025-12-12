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
0, 1, and 2.
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

--------------------------
Required hyperparameters
--------------------------
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
    7- Build, Train and Evaluate the model
    8- Run predictions
    9- Visualization
    10- Save trained model, scaler and summary
    11- Load trained model, scaler and summary

--------------------------
Completed sections (1–4)
--------------------------
I have done the following steps:
    1- Load df
    2- Create df_model from df and add the 'label' column
    3- CHRONOLOGICAL SPLITTING
    4- SCALING DATA

--------------------------
Variables & summaries for Part 5 (Imbalance handling)
--------------------------

1) Split indices (chronological slice positions):
   train_end index: 102449
   val_end   index: 124402

2) Shapes of splits:
   train_df shape: (102449, 11)
   val_df   shape: (21953, 11)
   test_df  shape: (21954, 11)

3) Label distribution (counts) in TRAIN set:
   Class 0: 101109 samples (98.692032%)
   Class 1: 670 samples (0.653984%)
   Class 2: 670 samples (0.653984%)
   -> Total training samples = 102449

4) Label distribution (counts) in VAL set:
   Class 0: 21548 samples
   Class 1: 202 samples
   Class 2: 203 samples
   -> Total validation samples = 21953

5) Label distribution (counts) in TEST set:
   Class 0: 21572 samples
   Class 1: 191 samples
   Class 2: 191 samples
   -> Total test samples = 21954

6) Initial class_weight (sklearn 'balanced') computed from TRAIN labels:
   Class 0: weight = 0.337751
   Class 1: weight = 50.969652
   Class 2: weight = 50.969652
   (These are a starting reference; with extreme imbalance you'll likely need resampling + specialized losses.)

7) Objects/arrays you will likely need for Part 5:
   - y_train_labels           (numpy array of training labels)
   - train_class_counts       (dict of per-class counts in train)
   - class_weight_dict        (dict of computed weights from sklearn)
   - X_train_scaled           (numpy array of scaled training features, shape = (n_train, n_features))
   - X_val_scaled             (numpy array of scaled val features)
   - X_test_scaled            (numpy array of scaled test features)
   - X_train_scaled_df        (pandas DataFrame of scaled train features)
   - scaler                  (fitted StandardScaler instance)

--------------------------
Your task
--------------------------
Write the full code only part 5 (IMBALANCE HANDLING).


    Additional Requirements:
    - Because imbalance is extremely high (>98%), class weights alone are insufficient; additional imbalance-handling strategies are required.
    - At the beginning of the code in this section, place a parameter or parameters so that I can manage the imbalance value by setting them.
    - At the end of the code, print the variables required for part 6 (Create sequences).

