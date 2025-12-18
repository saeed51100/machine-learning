I am building a Forex time-series classification model in Python/Jupyter.
The goal is to detect trend-reversal points using 130,000 hours of labeled historical H1 data.
The dataset contains a "Label" column with trend-reversal classes:
0: no reversal
1: bullish reversal
2: bearish reversal

The model should learn patterns that indicate reversal points and reproduce this labeling on unseen data.

Trend-reversal events are extremely rare in my dataset. 
The class distribution in df_model is highly imbalanced:
- Class 0 ≈ 98.55%
- Class 1 ≈ 0.73%
- Class 2 ≈ 0.73%

So far, I have completed the following steps:
1- Chronological splitting of df_model (train/validation/test)
2- Scaling using only training data

* My question:
1- Is it appropriate to use the imbalanced-learn library to handle class imbalance in a time-series classification problem?
Specifically, does applying resampling methods (such as over-sampling or under-sampling) destroy the temporal sequence or introduce data leakage?
2- What is the best approach to imbalance handling in time series problems?