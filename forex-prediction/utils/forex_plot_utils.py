#%% md
# # After changes: refactor > Convert To Python File
#%%
# forex_plot_utils.ipynb

# PARAMETERS (can be overridden in calling notebook)
vertical_line_color = 'gray'
vertical_line_width = 2  # Bolder vertical line

colors = {
    'historical': 'black',
    'actual': 'green',
    'predicted': 'red'
}

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

def plot_all_series(historical_df=None, predicted_df=None, actual_future_df=None, title="", output_path=None):

    """
    Plots available data series:
    - Line plots for <CLOSE> if present
    - Vertical markers for 'buy'/'sell' if predicted_df has classification labels
    """
    plt.figure(figsize=(14, 6))
    plotted = False

    # Plot historical prices
    if historical_df is not None and '<CLOSE>' in historical_df.columns:
        plt.plot(historical_df['DATETIME'], historical_df['<CLOSE>'],
                 label='Historical', color=colors['historical'])
        plotted = True

    # Plot actual future prices
    if actual_future_df is not None and '<CLOSE>' in actual_future_df.columns:
        plt.plot(actual_future_df['DATETIME'], actual_future_df['<CLOSE>'],
                 label='Actual Future', color=colors['actual'])
        plotted = True

    # Plot predicted prices (regression)
    if predicted_df is not None:
        if '<CLOSE>' in predicted_df.columns:
            # Regression forecast
            plt.plot(predicted_df['DATETIME'], predicted_df['<CLOSE>'],
                     label='Predicted', color=colors['predicted'], linestyle='--')
            plotted = True

        # Plot classification reversal markers (buy/sell)
        if 'label' in predicted_df.columns:
            for i, row in predicted_df.iterrows():
                if row['label'] in ['buy', 'sell']:
                    plt.axvline(x=row['DATETIME'], color='red' if row['label'] == 'sell' else 'blue',
                                linestyle=':', linewidth=vertical_line_width,
                                label=row['label'].capitalize() if i == 0 else "")  # avoid duplicate labels

    # Vertical line to show where prediction starts
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
