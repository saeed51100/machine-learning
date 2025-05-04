#%% md
# # After changes: refactor > Convert To Python File
#%%
# forex_plot_utils.ipynb

# PARAMETERS (can be overridden in calling notebook)
vertical_line_color = 'gray'
vertical_line_width = 2  # Bolder vertical line

# IMPORTS
import pandas as pd
import matplotlib.pyplot as plt
import os

# UTILITY FUNCTIONS
def load_csv_with_datetime(csv_path):
    """
    Loads a CSV file and returns a DataFrame with a DATETIME column and <CLOSE>.
    """
    df = pd.read_csv(csv_path, sep='\t' if '\t' in open(csv_path).readline() else ',')
    df['DATETIME'] = pd.to_datetime(df['<DATE>'] + ' ' + df['<TIME>'], format='%Y.%m.%d %H:%M:%S')
    return df[['DATETIME', '<CLOSE>']].reset_index(drop=True)

def plot_all_series(historical_df, predicted_df, actual_future_df, title, colors, output_path=None):
    """
    Plots available data series for closing prices.
    """
    plt.figure(figsize=(14, 6))
    plotted = False

    if historical_df is not None:
        plt.plot(historical_df['DATETIME'], historical_df['<CLOSE>'],
                 label='Historical', color=colors['historical'])
        plotted = True

    if actual_future_df is not None:
        plt.plot(actual_future_df['DATETIME'], actual_future_df['<CLOSE>'],
                 label='Actual Future', color=colors['actual'])
        plotted = True

    if predicted_df is not None:
        plt.plot(predicted_df['DATETIME'], predicted_df['<CLOSE>'],
                 label='Predicted', color=colors['predicted'], linestyle='--')
        plotted = True

    if historical_df is not None:
        prediction_start_time = historical_df['DATETIME'].iloc[-1]
        plt.axvline(x=prediction_start_time, color=vertical_line_color,
                    linestyle='--', linewidth=vertical_line_width, label='Prediction Start')

    plt.title(title)
    plt.xlabel('Time')
    plt.ylabel('Close Price')
    if plotted:
        plt.legend()
    plt.grid(True)
    plt.tight_layout()

    if output_path:
        plt.savefig(output_path)
    plt.show()

#%%
