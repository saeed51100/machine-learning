Please think long and hard.

--------------------------
Overview
--------------------------
I am building a Forex time-series classification model in Python/Jupyter.
The goal is to detect trend-reversal points using 130,000 hours of labeled historical data.

--------------------------
Goal
--------------------------
The model must:
Use 120 past candles to predict 5 future labels (0=no signal, 1=buy reversal, 2=sell reversal).
Reproduce the "Label" column on unseen data.

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

I have done the following steps, and I am writing the results for you:
1- Load df
2- Create df_model from df and add the 'label' column
3- CHRONOLOGICAL SPLITTING
4- SCALING DATA
5- IMBALANCE HANDLING


--------------------------
Results of running parts 1 to 5:
--------------------------

# --- Hyperparameters ---
WINDOW_SIZE = 120
FORECAST_HORIZON = 5
FEATURES = ['OPEN', 'HIGH', 'LOW', 'CLOSE', 'TICKVOL']

# --- Dataset Sizes ---
Train_df_rows = 102449
Val_df_rows   = 21953
Test_df_rows  = 21954

# --- Sequence Shapes ---
X_train shape: (102325, 120, 5)
y_train_multi shape: (102325, 5)
y_train_any shape: (102325,)
X_val shape: (21829, 120, 5)
y_val_multi shape: (21829, 5)
y_val_any shape: (21829,)
X_test shape: (21830, 120, 5)
y_test_multi shape: (21830, 5)
y_test_any shape: (21830,)

# --- Class Weights (for y_train_any) ---
class_weights = {0: 0.35665115630609434, 1: 10.196811160936722, 2: 10.196811160936722}

# --- Sample Weights (train) ---
sample_weights_train: numpy array of length = 102325

# --- Oversampled Training Set ---
X_train_resampled shape: (109979, 120, 5)
y_train_any_resampled shape: (109979,)
resampled_class_counts = {np.int64(0): np.int64(95635), np.int64(1): np.int64(7172), np.int64(2): np.int64(7172)}

# --- Scaler Information ---
Scaler type: StandardScaler (fit only on training data)
Scaler mean shape: (5,)
Scaler var shape: (5,)

# --- Notes ---
Use X_train_resampled, y_train_any_resampled for training.
Use X_val_scaled, y_val_any for validation.
Use X_test_scaled, y_test_any for final evaluation.
FORECAST_HORIZON = 5 → model must output 5 labels per sequence.

--------------------------
Your task
--------------------------
Write the full code for:
    6- Create sequences (WINDOW_SIZE → X, FORECAST_HORIZON → y)
    7- Build the model
    8- Train the model
    9- Evaluate the model
Earlier sections (1~5) are already complete.

