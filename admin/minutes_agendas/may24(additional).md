*After the advisory committee, Aditya and Levannia asked us if we could join an impromptu meeting as they had further suggestions for us. Saisree and Neethu were gone for lunch and could thus not join.*

- They feel we should try some sort of noise filtering algorithm, and instead of using clustering, try using moving/simple averages. 
- The analyte we are working with is very noisy, so if we can find an underlying signal and then use this signal to calculate some stats (i.e. the same predictors from the predictor file), they should then be able to use similar models that they currently use for other analytes to distinguish the pin contact errors.
- First step : Focus on just filtering (smoothening the curve) --> even if we loose some info
- Split them into different windows, filter out the noise and then find moving averages(or just the mean), then take unsuccessful readings and do the exact same thing and compare the averages.
- The reason why we are approaching it in this simpler way: biggest difference between our analyte and the other sensors is that it is noisier.
- For the pin contacts, the signal should go to 0 (because there is no current) in the calibration window as well as in the sample window whereas for the unsucessful readings, it will not go to 0 for the sample window.
- Provide them with a framework to filter our analyte so that it ressembles the other analytes
- Note differences between groups of the unsuccessful and the pincontacts could be useful (even if we are not clustering the pin contacts out)
- If smoothing get us somewhere - that would satisfy our client
- If we smooth, we might not have to cluster, we might be able to apply some sort of moving average method to pull out the pin contacts. By removing the noise, the pin contact should be close to 0 for the entire waveform. 
- Use another analyte (that is not noisy and that performs well in their models) to compare how smooth our waves should be.
- Once our waves are smooth, we can recalculate the predictors and use those to perform supervised learning (i.e. SVM) and identify the pin contact errors.
- Once the noise will be removed, it will be easier to identify the misclassification, if we choose to go in the supervised realm (identify the unsucessful that should have been pin contacts).
- The downside of doing supervised is we will not be able to identify other ways (other than pin) that our analyte fails.
- How to compare the smootheness of our analyte to the smoothness of the other 'target' analyte : calculate how similar the slope in target and the slope in smooth analyte are. 
- Will give us the formulas to recalculate the predictors
