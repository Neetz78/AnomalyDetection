# **Archive Glossary**

Here is a glossary for the original bits of code used in the first iteration of our project where the results were unsatisfactory. 

## Preprocessing (Iteration 1)

Preprocessing steps taken in the first iteration. The notebooks are listed in the order that they were used. 


|Notebook/Script| Description |
|--------|--------------------------------------|
|[SeparateLabels](Preprocessing/SeparateLabels.ipynb) | This notebook was used in the first iteration to separate out the unsuccessful and successful predictors into different files.|
|[CheckMissingRecords](Preprocessing/CheckMissingRecords.ipynb) |  Used in the first iteration to make sure there were no duplicate test IDs or test IDs that were present in predictor files but not the time series files or vice versa.          |
|[Standardize](Preprocessing/standardize.py)| This script was used in the first iteration to remove the wet-up period and standardize the waveforms to have mean 0 and stdev 1. The code was janky though so in our final pre-processing notebook an improved function is included for future use. |
| [window](Preprocessing/window.ipynb)| This notebook was used in the first iteration to separate the files into widows relative to sample detect time. It wasn't great though because the indexing was highly dependent on the amount of wet-up removed. A much better function for this (window_after_zeroed()) is included in the final preprocessing notebook. |
| [Filtering](Preprocessing/Data-filtering.ipynb)| This notebook was used in the first iteration to try various filtering techniques such as low pass and band pass filters on the waveforms. |

## Clustering (Iteration 1)
|Notebook/Script| Description |
|--------|--------------------------------------|
|[CalWindowPCA](Clustering/PCA_CAL.ipynb)|This notebook tries to cluster frequency domain of the calibration window of the readings into 2 groups using agglomerative clustering with 3 clusters and with euclidean distance as a distance measure. This process was also repeated after trying to extract features from the frequency domain with TSFresh. ECDs were not separated from unsuccessful in either case. Plotting the first two components of a PCA further demonstrated the lack of separation between these two groups.  We also tried this on the post ad sample windows with similar results. |
|[CalWindowKMeans](Clustering/CLUSTER_CAL.ipynb) | This notebook tries to cluster the calibration window of the readings into 2 groups using kmeans with dynamic time warping as a distance measure. The results were bad with an equal proportion of unsuccessful and ECD errors in both clusters. We also tried this on the post ad sample windows with similar results.|
|[CalWindowFFTKMeans](Clustering/CAL_FFT.ipynb) | This notebook tries to cluster frequency domain of the calibration window of the readings into 2 groups using agglomerative clustering with 3 clusters and with euclidean distance as a distance measure. This process was also repeated after trying to extract features from the frequency domain with TSFresh. ECDs were not separated from unsuccessful in either case. Plotting the first two components of a PCA further demonstrated the lack of separation between these two groups.  We also tried this on the post ad sample windows with similar results. |
|[CalWindowSOM](Clustering/CAL_SOM.ipynb) | This notebook tries to cluster the normalized calibration window and the raw calibration window waveforms using SOM (self organizing maps). The results were not promising as the clusters always included a major portion of unsuccessful waveforms but this window seemed to perform the best out of all windows. |
|[PostWindowSOM](Clustering/POST_SOM.ipynb) | This notebook tries to cluster the normalized post window and the raw post window waveforms using SOM (self organizing maps). The results were worse than those obtained in calibration window. |
|[SampleWindowSOM](Clustering/SAMPLE_SOM.ipynb) | This notebook tries to cluster the normalized sample window and the raw sample window waveforms using SOM (self organizing maps). The results were worse than those obtained in the calibration window. |
|[TSFresh](Clustering/FeatureExtractionTSFRESH.ipynb) | This notebook provides a template pipeline for clustering using the features extracted from the TSFRESH python package. For demonstration purposes, we have used the time-series data for the calibration period ([-15, -3] from sample detect time) without standardizing and without noise filtering. This process was also repeated for data that was pre-processed in various different ways. The list of attempts is detailed at the beginning of this notebook. |
|[AutoencoderIteration1](Clustering/AutoencoderIteration1)|This notebook contains the intital run of the autoencoder to extract features from raw time series data after preprocessing and clustering performed using various techniques such as Agglomerative clustering,KMeans and Gaussian Mixture Model.These steps were performed on all windows separately i.e calibration,post and sample window.  |
|[Calwindow_clustering](Clustering/Calwindow_clustering) | This notebook contains different dimensionality reductions techniques tried such as Singular Value Decomposition, Discrete fourier transforms and Discrete Wavelet transforms on only calibration window of the time series data. Clustering methods such as Kmeans, DBSCAN and Birch.|
|[DWT&model](Clustering/DWT&model) | This notebook contains DWT(discrete wavelet transform) filtering technique and clustering perfomred over the filtered waveform.|


## Noise Reduction (Iteration 1.5)

A slight miscellaneous notebook is an example of the attempts we made to compare the noise levels of our analyte with a less noisy one. 

|Notebook/Script| Description |
|--------|--------------------------------------|
| [Noise Exploration](Preprocessing/NoiseExploration.ipynb)| This notebook is an example of the process we used to compare our analyte of interest (A) with a less noisy analyte (B) to try and determine the optimal way to reduce noise. Future work could definitely benefit from trying other attempts. In the final preprocessing notebook, three forms of noise reduction are included, along with a function for diagnostic plots which only considers analyte A.  |
| [Moving Average Feature Extraction](Preprocessing/MovingAverageFeatures.ipynb)| This notebook includes a function to window a dataframe that contains the moving average of each time series. When using a centered moving average with a window of length 'w', the first and last 'w/2' time points are NaN, thus a new function that considers this new indexing was created to window w.r.t sample detect time. Then, the difference in mean between the calibration window, the post window and the sample window were calculated for each timeseries in the hopes of using these differences as new predictors. We found that whether or not the data had been normalized prior to smoothened affected the distribution of these differences greatly.    |
| [Differences in Mean between Windows](Preprocessing/DifferencesMeanRF.ipynb)| This notebook includes various plots to visualize the raw waveforms compared to that of the moving average. Also, boxplots for the distributions of the differences in mean between windows [(see Moving Average Feature Extraction notebook)](Preprocessing/MovingAverageFeatures.ipynb) for the smoothed waveforms (smoothed using moving average) are included to see if they differ for the ECD readings and the unsuccessful readings. In order to see how much predictive power these new features (difference in mean) held, a random forest classifier was used. |


## Anomaly Detection (Iteration 1)

A slight miscellaneous notebook is an example of the attempts we made to detect ECDs as anomalies with respect to unsuccessful readings.

|Notebook/Script| Description |
|--------|--------------------------------------|
| [LSTM](AnomalyDetection/LSTM)| This notebook cotains the LSTM model used along with autoencoder to detect anomalies in this case being ECDs from other unsuccessful readings.|
