
# May 20: Check-in meeting with Siemens Healthineers

**Presented findings:**
- Splitting based on windows
- Problem with the peaks and sample detect time not matching
- Application of PCA of cal, sample and post window
- Auto encoding waveforms to obtain 200 features
- Applying LSTM on the resultant features to cluster
- Application of SOM on the waveforms of different windows
- Applied SOM on standardized waveforms after windowing 
- Gaussian mixture model to cluster 
- Checking subclusters of a cluster

We also presented the agenda that would be used in meeting with advisor on May 24th

# Suggestions and questions asked:

Q1: Is standardizing reducing information? <br>
    Maybe. Would have to explore with raw data for the next week.

Q2: How do technology analysts typically label a pin contact? <br>
    When the calibration mean is 0, they usually classify it as pin contact

S1: Three types of pin contact error : <br>
	  Glue on card, glue on connector, scratch on the card

S2: Number of clusters: <br>
	  Deciding based on the return codes for unsuccessful and the 3 types of producing pin contact error

S3: Try separating the PCA clusters by height

S4: Trying applying clustering on filtered data

Decided to present to the data review meeting of Siemens Healthineers to practice for the mid-term presentation

Siemens Healthineers to provide the kind of synthetic data produced (glue on card, glue on connector or scratch on the card)




