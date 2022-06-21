# This script was used in the first iteration to remove the wet-up period and standardize the waveforms to have mean 0 and stdev 1. The code was janky though so in our final pre-processing notebook an improved function is included for future use. 

# Reads in the time series data and creates new files with the standardized time series, with wet-up period (user defined) removed.
import pandas as pd

# Read in the time series data
ECDts = pd.read_csv('../Data/Time Series/ECDTS/PC_TS.csv')
synth_ts = pd.read_csv('../Data/Time Series/ECDTS/PC_TS_Synthetic.csv')
un_ts = pd.read_csv('../Data/Time Series/unsuccesful time series/US_TS.csv')
direct = '../Data/Time Series/successful time series/S_TS_'
# succ_ts = pd.concat(map(pd.read_csv, [direct+'1(1).csv', direct+'2(1).csv', 
#                                  direct+'3(1).csv', direct+'4(1).csv', direct+'5(1).csv', direct+'6(1).csv', 
#                                  direct+'7(1).csv', direct+'8(1).csv']))



def standardize(ts_df, wet_up_length = 150):
    """Gets rid of wet-up period and z-normalizes time series stored in a dataframe. 

    Args:
        ts_df (pandas data frame): Time series stored in rows of dataframe, with first column being the test ID. 
        wet_up_length (int, optional): Length of the wet-up period in seconds (default = 150).

    Returns:
        A new pandas data frame with z-normalized time series stored in the rows. 
    """
    samples = int(wet_up_length/0.2) #Length of the wet-up period in samples. 
    subset = ts_df.iloc[:, samples:1501] #Time series with wet-up period removed. 
    ids = ts_df['TestId']
    s = subset.std(axis = 1) #New data frame with standard deviation for each time series. 
    # Change 0's to 1*10^-50 to avoid errors when dividing by 0. 
    s = [10e-50 if a == 0 else a for a in s]
    m = subset.mean(axis = 1) #New data frame with the mean for each time series. 

    #Subtract the mean of the time series from each time point. 
    st1 = subset.sub(m, axis = 0) 
    #Divide each time point by the standard deviation of the time series. 
    norm = st1.div(s, axis = 0)

    #Return the standardized time series with test ids back in the first column. 
    return pd.concat([ids, norm], axis = 1)


# Save the new standardized files. 
pin = standardize(ECDts)
un = standardize(un_ts)
synth = standardize(synth_ts)
# succ = standardize(succ_ts)

pin.to_csv('../Data/Time Series/ECDTS/PC_TS_STAND.csv', index = False)
un.to_csv('../Data/Time Series/unsuccesful time series/US_TS_STAND.csv', index = False)
synth.to_csv('../Data/Time Series/ECDTS/PC_TS_SYNTH_STAND.csv', index = False)
#succ.to_csv('Data/Time Series/successful time series/S_TS_STAND.csv', index = False)