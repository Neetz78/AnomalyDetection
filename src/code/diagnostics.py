import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pandas.api.types import is_numeric_dtype
import altair as alt

""" Gets the data into the proper format for the other diagnostic functions. 
    Args:
        ts_df has columns for all the time points and a TestId column so it can be joined with the predictors data. 
        pred_df has the aggregate predictors, and a TestId column so it can be joined with the time series data. 
        clusters - optional - has the labels for the clusters formed from a clusterig algorithm
        labels - optional - has the pre-defined labels for the reading (eg. un/pc/etc). 
    Returns:
        A data frame containing the time series data and predictors. If clusters and labels are provided, they are added
        as columns in the data frame. 
"""
def prepare_data(ts_df, pred_df, clusters = None, labels = None):
    ts_pred = pd.merge(ts_df, pred_df, how = 'left', on = 'TestId')
    
    # If clusters and labels are not empty, add them as columns to the data frame. 
    if clusters is not None:
        ts_pred['Cluster'] = clusters
    if labels is not None:
        ts_pred['Label'] = labels.reset_index(drop = True)
        
    return ts_pred

""" Retrieves the testids in a given cluster and stores them in a dataframe. The user has the option of extracting the ids for a specific type(s) of reading(s)
 (i.e. unsuccessful, ecd).
        data: Pandas dataframe that contains minimally: 
                - a column for the testids, 
                - a column for the label of the reading (i.e. unsuccessful, ecd, con, syn)
                - a column with the cluster number
        cluster_num (int): The number of the cluster that the user wants to extract the TestIds from
        clust_col (str): The name of the column containing the clusters of the readings
        label_col (str): The name of the column containing the labels of the readings
        id_col (str): The name of the column containing the test ids of the readings
        labels (list) - optional: A list of the labels for which we want to extract the TestIds. If none is given, all the testids in the cluster are returned.
    
    Returns:
        A dataframe with the TestIds for the readings in a specific cluster
        
    Example:
        To extract the testids for the contaminated ('con') and synthetic ('syn') ecd contact readings in cluster 3 we would have:
        extract_testid(data, cluster_num = 3, label = ['con', 'syn'])
"""
def extract_testid(data, cluster_num, clust_col = 'Clusters', label_col = 'Label', id_col = 'TestId', labels = None):
    if label is not None:
        testids = data[(data[clust_col] == cluster_num) & (data[label_col].isin(label))][id_col]
    else:
        testids = data[(data[clust_col] == cluster_num)][[id_col, label_col]]
    
    df = pd.DataFrame(testids).reset_index(drop = True)
    return df



""" Retrieve the number of readings from different categories in each cluster (eg. number of unsuccessful, number of wild ecd errors, etc)
    and store them in a dataframe. 
    Args:
        ts_pred can have columns for any predictors but must also have and a label column with the predefined labels (un'/'pc'/etc'), 
                and a cluster column with the cluster labels. 
    Returns:
        A dataframe with the counts of readings in each category for each cluster. 
        This dataframe has columns for each of the following: cluster label, a column for the count of reading in each non 'un' categories,  
        the sum of reading in non 'un' categories (assumed to be the total number of ecd contact errors), and the number of unssuccessful 
        readings. Rows are sorted in descending order based on the number of total ecd contact errors so that the information for the cluster 
        with the most ecd contacts is at the top of the dataframe. 
"""
def get_label_counts(ts_pred, clust_col = 'Cluster', label_col = 'Label'):

    #Group by label and cluster to get
    counts = ts_pred[[clust_col, label_col]].value_counts().reset_index(name='counts').sort_values([clust_col, 'counts'], ascending = [1, 0]).reset_index(drop = True)
    
    #Pivot so each column is a label and the values are the counts. Replace nans with 0s. 
    counts = counts.set_index(clust_col).pivot(columns = label_col, values = 'counts').fillna(0)
    counts = counts.apply(pd.to_numeric, downcast='integer')
    
    #Count the total number of ecd error (all but un)
    counts['tot_ecds'] = counts[list(counts.columns[counts.columns != 'un'])].sum(axis = 1)
    
    un = counts.pop('un')
    counts['un'] = un
    
    #Sort descending by non - 'un' labels, so first clusters contain the most ecds. 
    return counts.sort_values('tot_ecds', ascending = False)

""" Prints the number of readings from different categories in each cluster 
    (eg. number of unsuccessful, number of wild ecd errors, etc). 
    Displays histograms for the desired aggregate predictors in each cluster. 
    If show_traces = True, plots the waveforms in each cluster, with one plot for unsuccessful, 
    and one for the various kinds of ECD errors. 
    Args:
        ts_pred has columns for all the predictors (time points and other features), TestId, Cluster (result of the clustering algorithm), and Label ('un'/'wild'/'syn'/'etc'). Can be generated with prepare_data(). 
        feature_list is a list of the aggregat predictors you wish to describe for the clusters.
        start is the time that the time series data begins with respect to sample detect time (eg. -30 means a start of 30 seconds before sample detect time). 
        clust_col is the name of the column containing cluster labels. 
        label_col is that name of the column cotaining the data labels ('un'/'syn'/'cont'/etc) 
        show_traces is a boolean variable indicating whether you wish to see the plotted weaveforms for the different clusters. 
    Returns:
        Nothing.
"""
def describe_clusters(ts_pred, feature_list, start = -30, end = 39.8, clust_col = 'Cluster', label_col = 'Label', show_traces = True):
    # Make sure there's only one decimal place in start and ed time, and get the string representations for column name indexing. 
    start = str(round(float(start), 1))
    end = str(round(float(end), 1))
    
    #Get the counts for number of readings in each cluster
    counts = get_label_counts(ts_pred, clust_col = clust_col, label_col = label_col)

    
    #Add plotting the raw traces to the loop when show_traces is true. 
    if show_traces == True:
        feature_list.append('un')
        feature_list.append('ecd')
    
    #Make sure font is visible in all subsequent plots
    plt.rcParams['font.size'] = '15'
    #Compute some summary information for each cluster.
    for cluster in counts.index:
        # Print the cluster number: 
        print('\nCluster', cluster, '\n------------------------------------')
        # Subset the data frame with just the cluster.
        clust_subset = ts_pred[ts_pred[clust_col] == cluster]
        # Print some summary information
        for label in counts.columns:
            print("Number of", label, ":", counts[label][cluster])
        
        # Arange the descriptive plots into a row for each cluster. 
        fig, axes = plt.subplots(1, len(feature_list), figsize = (200/len(feature_list), 5))
        # Make a plot for each of the features in the list. 
        for feat, ax in zip(feature_list, axes):
            
            # Plot the unsuccessful waveforms (only happens when show_traces is true). 
            if feat == 'un':
                 if (len(ts_pred[(ts_pred[clust_col] == cluster) & (ts_pred[label_col] == 'un')]) > 0):
                    ax.plot(ts_pred[(ts_pred[clust_col] == cluster) & (ts_pred[label_col] == 'un')].loc[:, start:end].transpose())
                    ax.xaxis.set_ticks([start, '-0.0', end])
                    ax.set_ylabel('signal')
                    ax.set_xlabel('time (secs w.r.t sample detect')
                    
            # Plot the ECD error waveforms (only happens when show_traces is true). 
            elif feat == 'ecd':
                 if (len(ts_pred[(ts_pred[clust_col] == cluster) & (ts_pred[label_col] != 'un')]) > 0):
                    ax.plot(ts_pred[(ts_pred[clust_col] == cluster) & (ts_pred[label_col] != 'un')].loc[:, start:end].transpose())
                    ax.set_ylabel('signal')
                    ax.set_xlabel('time (secs w.r.t sample detect')
                    ax.xaxis.set_ticks([start, '-0.0', end])
            
            # When a feature is categorical, make sure the histogram has the same number of bins as categories to get the count for each one. 
            elif is_numeric_dtype(ts_pred[feat]) == False:
                ts_pred[feat] = ts_pred[feat].astype(str)
                ax.hist(ts_pred[ts_pred[clust_col] == cluster][feat], bins = len((ts_pred[ts_pred[clust_col] == cluster][feat]).unique()))
                ax.tick_params(labelrotation=90)
                ax.set_ylabel('count')
                ax.set_xlabel('category')
            
            # Use the default number of bins when the feature is numerical. 
            else:
                ax.hist(ts_pred[ts_pred[clust_col] == cluster][feat])
                ax.set_ylabel('count')
                ax.set_xlabel('value')
            ax.set_title(feat)
            
        # Show all of the plots. 
        plt.show()
        
""" Compare the probability density estimations for selected predictors for two clusters. This will tell us the proportion of reading having different value of the predictors in different clusters. 
    Args:
        ts_pred has columns for all the predictors (time points and other features), TestId, Cluster (result of the clustering algorithm), and Label ('un'/'wild'/'syn'/'etc'). Can be generated with prepare_data(). 
        clust1 is the label for the first cluster you want to look at. 
        clust2 is the label for the seconf cluster you want to look at. 
        feature_list is a list of the aggregat predictors you wish to describe for the clusters. These must be numerical features. 
        start is the time that the time series data begins with respect to sample detect time (eg. -30 means a start of 30 seconds before sample detect time). 
        clust_col is the name of the column containing cluster labels. 
        label_col is that name of the column cotaining the data labels ('un'/'syn'/'cont'/etc) 
        show_traces is a boolean variable indicating whether you wish to see the plotted weaveforms for the different clusters. 
    Returns:
        Nothing.
"""       
def compare_cluster_densities(ts_pred, clust1, clust2, feature_list, clust_col = 'Cluster'):
    # Select the rows with the clusters of interest
    subset = ts_pred[ts_pred[clust_col].isin([clust1, clust2])].copy()
    subset['Cluster'] = subset['Cluster'].astype(str)

    # For each feature in the lsit, make a plot that compares the densitities of that feature for the two clusters.
    # This will estimate the relative proportions of readings in the clusters at different values of the 
    return alt.hconcat(*(
        alt.Chart(subset).encode(
            x= col,
            y=col,
            color=clust_col
        ).transform_density(
            density=col,
            groupby = [clust_col],
            steps=200,
            as_=[col, 'density'],
            extent=[subset[col].min(), subset[col].max()]
        ).mark_area(orient='vertical', opacity=0.5).encode(
            y='density:Q'
        ).properties(
            height=200,
            width=200
        )
        for col in feature_list
    ))