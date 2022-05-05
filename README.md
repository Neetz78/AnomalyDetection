# Anomaly Detection in Biosensor Waveforms 

This project aims to compare various machine learning pipelines that perform clustering to identify pin contact errors from biosensor readings. 

## Team Members

- Justine Filion : one sentence about you!
- Saisree GR : one sentence about you!
- Neethu Gopalakrishna : one sentence about you!
- Sara Hall : one sentence about you!

## Describe your topic/interest in about 150-200 words

The compounding costs of healthcare services and shortages of healthcare facilities and of nurses and other skilled personnel have put pressure on the medical system to provide more care on producing user-friendly devices to the nurses in order to reduce training time and costs. As a result, there is an increasing demand in the range and complexity of medical devices. The devices range from a simple thermometer to complex devices, such as ventilators, infusion pumps, and dialysis machines. This demand escalates the need for more accurate devices. The robustness of a device could be ensured by handling the anomalies in the device’s usual performance. One such anomaly found in the epoc reader, a biomedical device that provides blood report, is error (no  reading ) on the epoc screen caused by the problem of lacking pin contact. The identification of the cause of this error is crucial in testing of these devices for quality assurance.

## About this Project

- Statistically show that the successful readings are similar enough to consider only a subset of them for our training dataset. This will alleviate issues resulting from having an imbalanced dataset. 
- Resample our data to obtain multiple training sets, each having more balanced classes.
- Leverage the aggregate predictors of the readings to find possible clusters.
- Remove the wet-up period from the waveforms as it provides no information on whether or not the reading is successful. 
- Split the waveforms into different time windows such as calibration window, sample window and post window. 
- Apply noise filters to the waveforms and feed them to machine learning algorithms for clustering.
- Compare whether or not the clusters obtained by the raw data and the waveform data match.


## Dataset

The dataset we are working with consists of several CSV files which describe sensor readings for a particular analyte from many different tests. The data generally consist of three broad categories - successful readings, unsuccessful readings, and readings lacking pin contact, which have been labeled manually by teams of people and separated out into different files. Overall there are 411076 successful readings,  9855 unsuccessful readings, and 84 readings lacking pin contact. This means that the data are heavily unbalanced and we will have to account for this in our machine learning pipelines. 

Each reading has two records associated with it: a raw signal time series, and a series of predictors which have been calculated from the raw data. These records can be linked together using their unique test identifiers. Within the predictors derived from the raw waveforms are metrics like slope, mean signal, and noise from several different windows including the calibration and sample periods. The timeseries for different tests are different lengths so that is another thing we will need to account for in our analyses. 

Both the predictor and time-series files will need some amount of preprocessing. With the time series data we will need to perform some sort of noise filtering. We will then need to plot and look at the waveforms to split them into windows that make sense for clustering unsuccessful readings into different groups. We may also want to look into ways to normalize the signals. For the predictors, we will need to make sure we are not missing too many missing values or outliers prior to proceeding with our analyses. Finally, it seems there might be some duplicated test records for the predictors as there are more records stored as summary statistics than as raw waveforms. As a result, we will need to filter out the tests that are present in both forms and get rid of any duplicates so that we are able to use them together should we choose to do so. 


## References 

[1] https://www.nhlbi.nih.gov/health/blood-tests

[2]https://www.siemens-healthineers.com/en-ca/blood-gas/blood-gas-systems/epoc-blood-analysis-system

[3]https://nacce.siemens-info.com/wp-content/uploads/2020/07/T20001.001-epoc-Blood-Analysis-System-Resource-Guide-v12-020521-eff-date-2-15-21.pdf

[4] Nawaz, Menaa, et al. "Signal Analysis and Anomaly Detection of IoT-Based Healthcare Framework." 2020 Global Conference on Wireless and Optical Technologies (GCWOT). IEEE, 2020.

[5] Dimitra Azariadi, Vasileios Tsoutsouras, “ECG Signal Analysis and Arrhythmia Detection on IoT wearable medical devices”, IEEE 5th International Conference on Modern Circuits and Systems Technologies (MOCAST), 2016.

[6] Md Anam Mahmud, Ahmed Abdelgawad, Kumar Yelamarthi, “Signal Processing Techniques for IoT-based Structural Health Monitoring” in IEEE 29th International Conference on Microelectronics (ICM), 2017.

D. Wulsin, J. Blanco, R. Mani and B. Litt, "Semi-Supervised Anomaly Detection for EEG Waveforms Using Deep Belief Nets," 2010 Ninth International Conference on Machine Learning and Applications, 2010, pp. 436-441, doi: 10.1109/ICMLA.2010.71.


