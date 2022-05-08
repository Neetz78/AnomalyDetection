# Anomaly Detection in Biosensor Waveforms 

This project aims to compare various machine learning pipelines that perform clustering to identify pin contact errors from biosensor readings. 

## Team Members

- Justine Filion : one sentence about you!
- Saisree GR : one sentence about you!
- Neethu Gopalakrishna : one sentence about you!
- Sara Hall : one sentence about you!

## Describe your topic/interest in about 150-200 words

As the healthcare sector evolves to incorporate more technology for faster and more accurate diagnostics, there is an increasing demand for commercially produced biomedical devices. For these instruments to help improve patient care, they must be accurate and reliable and thus undergo many tests for quality control. With the development of machine learning techniques in recent years, we are uniquely positioned to automate certain aspects of the quality control process.
One area of development is for systems that perform blood analysis, as it is one of the most common tests run by health professionals and is involved in the diagnosis of many different conditions [1]. Being able to get fast and accurate live test results has the potential to improve patient outcomes by enabling treatment to be modified based on results [2]. The epoc system fulfills these needs as a handheld wireless system that enables comprehensive blood analysis testing at the patient’s side within minutes on a single room temperature test card [2].

The epoc system has three components: a test card which contains the components necessary to perform the testing for various different analytes, a reader which has a card slot for the test card and records the test results, and a host that interfaces with the reader to provide information to the healthcare professional [3] As a device that is used in patient care, the test cards must undergo comprehensive quality control testing before being sent out for use. This testing involves making sure a low number of cards yield unsuccessful readings. A reading may be unsuccessful for different reasons such as inadequate pin contact between the test card and the reader or air bubbles in the sample. Operators spend a significant amount of time trying to diagnose these problems with unsuccessful tests by analyzing their waveforms, but manual identification is cumbersome and notalways accurate because of:

- Human bias in the identification of causes.
- Overlap between the characteristics of different problems that underlie unsuccessful readings.

As a result, the goal of this project is to use unsupervised machine learning techniques on the data from the readings for a particular analyte to see if they can be automatically clustered into different types of errors. Of particular interest is whether unsupervised methods will yield a cluster that corresponds well to a lack of pin contact between the test card and the reader.

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

## References 

[1] https://www.nhlbi.nih.gov/health/blood-tests

[2]https://www.siemens-healthineers.com/en-ca/blood-gas/blood-gas-systems/epoc-blood-analysis-system

[3]https://nacce.siemens-info.com/wp-content/uploads/2020/07/T20001.001-epoc-Blood-Analysis-System-Resource-Guide-v12-020521-eff-date-2-15-21.pdf

[4] Nawaz, Menaa, et al. "Signal Analysis and Anomaly Detection of IoT-Based Healthcare Framework." 2020 Global Conference on Wireless and Optical Technologies (GCWOT). IEEE, 2020.

[5] Dimitra Azariadi, Vasileios Tsoutsouras, “ECG Signal Analysis and Arrhythmia Detection on IoT wearable medical devices”, IEEE 5th International Conference on Modern Circuits and Systems Technologies (MOCAST), 2016.

[6] Md Anam Mahmud, Ahmed Abdelgawad, Kumar Yelamarthi, “Signal Processing Techniques for IoT-based Structural Health Monitoring” in IEEE 29th International Conference on Microelectronics (ICM), 2017.

D. Wulsin, J. Blanco, R. Mani and B. Litt, "Semi-Supervised Anomaly Detection for EEG Waveforms Using Deep Belief Nets," 2010 Ninth International Conference on Machine Learning and Applications, 2010, pp. 436-441, doi: 10.1109/ICMLA.2010.71.


