- We discussed our plan of the week which includes
  * Our concerns on DTW - the assumption that "one vector is a non-linear time-stretched series of the other"[ref](https://stats.stackexchange.com/questions/22209/can-someone-please-explain-dynamic-time-warping-for-determining-time-series-simi)
  * We think longest common subsequence could be a better measure
  * We want to do 2 types of clustering - shape based and feature based (fourier transforms/pca) (kmeans/kmedoids)
  * Because of the very different lengths of the time series and the limitations of of DTW, one option would be to only consider the calibration period (that is common to all series)

- Feedback
  * Levannia talked to someone with lots of knowledge on the analyte we are using and said there has been no experience or treshold to distinguish noise from the signal
  * Noise reduction: would be interesting to do some kind of grid search to see which frequency works best - would be good for them to classify noise
  * Reserve some time in Friday's meeting to talk about what will be discussed in Tuesday's advisory committee
  * The fabricated pin contacts that they are doing will be available to us on Thursday.
  * If the very short wavelengths are causing us issues (return code: cannotcalculate), we can discard them.
