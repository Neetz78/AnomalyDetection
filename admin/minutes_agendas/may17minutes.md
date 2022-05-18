### Presentation

Team presented the overall progress, roadblocks and current weeks plan to Irene and Debangsha.

### Questions and Feedback

- Irene requested to walkthrough to understand time series better.
- Was questioned on wet-up period, Sara confirmed that we would be removing the wet-up period.

 ### How were these classified to begin with?
 
- Informed that a manual tenchnician would mark them as unsuccessful and pincontacts.
- Information was not provided on the important features of the waveforms, could have potentinal misclassifications.
- Was suggested to get confirmation from the client regarding this.

Was asked to reiterate the problem statement, finding pincontacts within the unsuccessful readings, explained other possible unsuccessful readings such as air bubble in sample.

### Why are we trying to find the pincontacts within unsuccessful readings?What is the necessity of this ? 

The clients needs to make sure that each batch has a limited number of pincontact errors in each batch before the cards are sent out.

### Include one slide as a quick recap of the problem statement in weekly update slides

- Considering looking into centering the waveforms to the peaks, as we have different lengths it might be useful.

### What makes the lengths different?
- we are not entirely sure.

### what is the plan going forward regarding different lengths?
- we are windowing first to see if it works, as the clients have mentioned that the calibration window is the most suitable for pincontacts.
- Later we would increase window or consider the entire waveform, and see the for the lengths.

### Once you consider the full length waveforms, what would you do with the shorter ones? 
- We are going to throw then out as we do not have any cases of these as of now.
- If time permits we might include them and see if we have a better way to do it.

### What is the frequency of the data?
- Informed them that the frequency is 5Hz.
- Was suggested to keep this is mind while using window

### Are you using overlaping windows or non- overlapping?
- Presently we are working with non-overlapping windows, later we might look into overlapping windows.
- Was suggested to overlapping, as overlapping windows helps in getting more data points and extract more features.

### Are you forbidden from using Deep neural netwrok?
- No we are not, was suggest to consider using them.
- Might help in extracting goof features for timeseries data.

### How are you formaulating this problem 
- We are trying to cluster pincontacts within the unsuccessful data.
- Time series clustering.

### Is it finding pincontacts wihtin unsuccessful or pincontacts among all of it?
- Explained that earlier we have considered the entire dataset, but since this process is supposed to improve the quality control process and manual technician do not even look at successful readings we have considered to drop it and only work with unsuccessful and pincontacts.

### You said some of the pincontacts look like a successful does it mean they have been misclassified?
- Informed them that the clients have confirmed that the labels are legit, and data has no errors.

- Looks like this a problem of unsupervised anomaly detection.
- Take advantage of all digital signal processing techniques, such as band-pass filtering , low pass filtering, spectral residual, fourier transform.\
    - Informed them that fourier transform essentail only gives frequency information, Hence we are considering DWT(Discrete wavelet transforms).
    - We have to extract some features from the time series , wothout that we wont be able to cluster raw time series data.
    - Look into dynamic time wrapping, looking forward to see your results in the next week.
 ### Units in the plot?
 - X-axis is the time and Y-axis is  the current , always include the units in the plots.


