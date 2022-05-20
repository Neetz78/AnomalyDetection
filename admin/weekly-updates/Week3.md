Overall Progress at the end of Week 3 (May 16 - 22)

Since this project is mainly exploration based, we have clarified the expectations of the deliverables with our client. They have agreed that notebooks describing our attempts are sufficient. Scripts will be made for promising pipelines and preprocessing.

- Split the data into 3 windows according to the documentation provided: calibration window, post window, sample window.
  * This ensured that all of our timeseries were of the same length so that we dont run into issues when clustering
- Tried various modelling on the waveforms
  * Clustering windows with DTW
  * Clustering attempts on features extracted using the tsfresh package
  * Feature generation using an autoencoder - follwed by clustering on the features obtained
  * Clustering attempts with a self-organizing map


