# # # # # #
# Imports #
# # # # # #

# Data Processing
import pandas as pd

# Visualization
import matplotlib.pyplot as plt

# Local Imports
import constants

# # # # # # #
# Functions #
# # # # # # #
'''
makeBoxPlot creates a box & whisker plot of a dataframe containing at least the
    following two columns: `start_time/intermission-start`, and `duration`.
    It then constructs a boxplot of the durations starting at each hour
    of the day: e.g., the mean of durations starting at 1am, 2am, and so on.

Returns: 
    0 if executed correctly, 1 if an error occured. 

Args:
    df: The dataframe to be turned into a boxplot
    cutoff: time in seconds to cut off the box & whisker: 0 * 60^2 < c < 24 * 60^2
    operator: how to cut off: gt, gteq, lt, etc.
    Time division: minutes, hours
    maximum: Max cutoff, only used for '>' and '>='.
        e.g., makeBoxPlot(1*HOURS, '>=', 'hours', 2*HOURS), read as 1hr <= h <= 2hrs
'''
def makeBoxPlot(df, cutoff, operator = '<', time_division = 'hours', maximum = (24 * constants.HOURS)):
    if('start_time' in df.columns ):
        start_str = 'start_time'
    else: # I chose to make interm. start, just to ensure the DFs aren't mixed up...
        start_str = 'intermission_start'
    op_func = constants.OPS[operator]

    # e.g., Interm. op Cutoff
    cutoff_df = df[op_func(df['duration'].dt.total_seconds(), cutoff)]
    
    cutoff_df = cutoff_df[cutoff_df['duration'].dt.total_seconds() <= maximum]

    cutoff_group = cutoff_df.groupby(cutoff_df[start_str].dt.hour)['duration']

    grouped_data = []
    for index, val in cutoff_group:
        if (time_division == 'hours'):
            grouped_data.append(val.reset_index(drop=True) / pd.Timedelta(hours=1)) 
        elif (time_division == 'minutes'):
            grouped_data.append(val.reset_index(drop=True) / pd.Timedelta(minutes=1))
        else:
            print('Error!!! Bad Time Division.')
            return 1 

    result_df = pd.concat(grouped_data, axis=1).dropna()
    result_df.columns = range(0, len(cutoff_group))

    formatted_cuttof = ((cutoff / 60 / 60) if time_division == 'hours' else (cutoff / 60))
    formatted_maximum = ((maximum / 60 / 60) if (maximum > 60*60 ) else (maximum / 60))
    if(operator == '<' or operator == '<='):
        y_label = '[0 < d %s %.1f]'% (operator, formatted_cuttof)
    else:
        new_op = '<' + operator[1:]
        print(formatted_maximum)
        y_label = '[%.1f %s d <= %.1f]'% (formatted_cuttof, new_op, formatted_maximum)


    plt.xlabel('Start of Intermission (24 Hours)')
    plt.ylabel('Avg. Intermission Duration ' + y_label + ' (' + time_division + ')')
    result_df.boxplot()
    plt.show()
    
    return 0
