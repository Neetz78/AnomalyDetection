## Advisory committee meeting

### May 24, 2022

#### Presentation

- The first 20 minutes was spent on presenting the committe with our progress,
- The presentation includes the following:
  - Agenda
  - Problem statement
  - Preprocessing
  - Schedule
  - Preprocessing aggregate predictors
  - Preprocessing raw time series
  - Preprocessing -windowing
  - Modelling whole windows
  - Visualizing readings
  - Modelling- Autoencoder
  - Modelling- Self Organizing Map
  - Modelling- TSFresh predictors
  - Modelling-Dimensionality Reduction
  - Modelling-Clustering
  - Next-steps
  - Questions and feedback,
 
 
**Questions and comments from advisors and data scientists:**

**Questions**

**Did the loadings from the PCA signify the imporatant features?**
- Didnt look at it, will try to find some insights, Also loadings from TSFresh library nothing stood out in this method all loadings were at 0.

**Are the pincontacts and unsuccessful distinguishable when viewed in your PCA?**
- They look the similar.

**How did you set up the components for PCA?**
- We gave the percenatge of variation to obtain the PCA as around 0.95.

**Did we include succcessful as well?**
- No we are using only unsuccessful and pincontacts.
- Maybe use successful test as a baseline for extracting features.

**Explain how we have normalized the data?**
- We have subtracted the mean and divided by standard deviation for each data point.
- Possibly the standarization is causing all the waveforms to look the same.
  
 **How are you going to find the metric before or after the noise filtering?**
 - We have not yet given much thought to it.
 - Shift the focus to noise filtering and later a simple moving average could work.

**Can we use a larger range of data? like the whole waveforms say 30s to 190s?**
- Yes, we are planning on expanding the windows to look for more information going forward.

**How did you decide on the autocorrelation? how did you decide the lag?**
- the package extracts by default a whole bunch of numbers.

**Was a optimal or a range of values?**

- We had a range of lags, we can go back and check the range of values to better understand the data points chosen.


**Feedback**

- Maybe because they are standard, it might have caused all of the waveforms to look the same. Try without standardizing in calibration window.Just standard sample window combination of the two might result in better outcome.
- look at the windows as a whole and not separate windows.
- If we cannot pull out pincontacts our main goal is to understand the characteristics of the data points by charactering the clusters which are forming now.
- Try training the model with the successful data, and feedin only pincontacts and later feed the model with unsuccessful to see how it fairs.


