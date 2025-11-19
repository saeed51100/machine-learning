Please think long and hard.
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
Dataset:
# --------------------------

* DataFrame name: df_model
* Rows: ~130,000 (continuous hourly series; gaps from holidays already filled)
* Columns (11 total), sample rows:

DATETIME,DATE,TIME,OPEN,HIGH,LOW,CLOSE,TICKVOL,VOL,SPREAD,Label
2008-11-28 00:00:00,NaN,NaN,10.36,10.36,10.32,10.33,0.0,0.0,0.0,0
2008-11-28 01:00:00,NaN,NaN,10.36,10.36,10.32,10.33,0.0,0.0,0.0,0
2008-11-28 02:00:00,2008.11.28,02:00:00,10.32,10.33,10.30,10.30,10.0,0.0,0.0,0
...


* DATETIME is continuous (index-like).

* Label column contains trend reversal points: 0, 1, 2.
The model should learn to reproduce this labeling.

# --------------------------
Features and hyperparameters (must be used)
# --------------------------

WINDOW_SIZE = 60
FORECAST_HORIZON = 10
FEATURES = ['OPEN','HIGH','LOW','CLOSE','TICKVOL']

# --------------------------
Requirements for the code you will write (MODEL + PREDICTION)
# --------------------------

1- Use df_model as the training dataset (it is already preprocessed/continuous).

2- Build an efficient, effective classification model that predicts reversal points (0/1/2) over the 10-hour horizon given the last 60 hourly candles.

3- The prediction pipeline must take a given_time from df ( not from df_model ) wich identifies the last available candle.
I have already prepared df which has a structure similar to df_model and 60 unseen candles are selected from it.

Use the specific given_time below for prediction tests:
given_time = "2025.08.13 21:00:00"

The prediction input should be the 60 candles that end at given_time.
The model should then output a length-10 array of class predictions for the next 10 hours immediately after given_time.


4- At the end of the prediction section your code must provide a DataFrame named predicted_df and return / show it as the last line.
predicted_df should include at least the forecast DATETIME for each of the 10 steps, the predicted class, and optionally predicted probabilities for each class.

# --------------------------
Deliverable (when you write the code)
# --------------------------

* A MODEL section that builds/trains (or defines/loading procedure for) a trained model suitable for this classification task (you may use TensorFlow/Keras; make clear training choices).

* A PREDICTION section that:

	- Prepares the 60-candle input from df ( not from df_model ) using given_time.
	- Runs the model to predict probabilities and classes for the next 10 hours.
	- Produces predicted_df as the last line of code. predicted_df must contain DATETIME (10 rows),
	- forecast_class, and optionally prob_0, prob_1, prob_2.

