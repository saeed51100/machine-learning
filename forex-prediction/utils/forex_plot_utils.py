#%% md
# # After changes: refactor > Convert To Python File
#%%
import pandas as pd
import matplotlib.pyplot as plt

# GLOBAL STYLES
vertical_line_color = 'gray'
vertical_line_width = 2

colors = {
    'historical': 'black',
    'actual': 'green',
    'predicted': 'red'
}

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
    Plots:
    - Historical & actual <CLOSE> prices (line plot)
    - Regression forecasts (dashed line)
    - Classification signals (vertical gray lines with 'buy' or 'sell' labels)
    """

    plt.figure(figsize=(14, 6))
    plotted = False

    # Historical <CLOSE>
    if historical_df is not None and '<CLOSE>' in historical_df.columns:
        plt.plot(historical_df['DATETIME'], historical_df['<CLOSE>'],
                 label='Historical', color=colors['historical'])
        plotted = True

    # Actual future <CLOSE>
    if actual_future_df is not None and '<CLOSE>' in actual_future_df.columns:
        plt.plot(actual_future_df['DATETIME'], actual_future_df['<CLOSE>'],
                 label='Actual Future', color=colors['actual'])
        plotted = True

    # Regression forecast <CLOSE>
    if predicted_df is not None:
        if '<CLOSE>' in predicted_df.columns:
            plt.plot(predicted_df['DATETIME'], predicted_df['<CLOSE>'],
                     label='Predicted', color=colors['predicted'], linestyle='--')
            plotted = True

        # Classification forecast (buy/sell markers)
        if 'label' in predicted_df.columns:
            for _, row in predicted_df.iterrows():
                if row['label'] in ['buy', 'sell']:
                    plt.axvline(x=row['DATETIME'], color=vertical_line_color,
                                linestyle='--', linewidth=vertical_line_width)
                    plt.text(row['DATETIME'], plt.ylim()[1], row['label'],
                             color='black', ha='center', va='top', fontsize=9, rotation=90)

    # Prediction start marker
    if historical_df is not None:
        prediction_start_time = historical_df['DATETIME'].iloc[-1]
        plt.axvline(x=prediction_start_time, color=vertical_line_color,
                    linestyle='--', linewidth=vertical_line_width, label='Prediction Start')

    # Final plot styling
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
