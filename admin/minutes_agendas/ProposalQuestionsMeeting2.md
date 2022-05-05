Minutes, meeting 2022-05-05 (40 minutes)
**Unsupervised** :
* Do we use only the unsuccessful readings and try to identify the pin contact errors?
	- No, combine the entire dataset, including the successful readings. The wave forms for the successful readings should be easily distinguishable from unsuccessful readings.
	- When combining them though, there will be huge imbalances. We would need to prove that all the successful readings are similar so that we can just use a subset of them when building our training set. (i.e. take 10 000 unsuccessful readings , 10 000 successful readings and all the pin contact errors)

**Link between raw data and waveform** :
* We can start with waveform and see how they compare to the clusters obtained from the predictors. 
* Can combine them and use them together (i.e. find a certain time period that is important and use it with the predictors).
* For the analyte we are studying, they were previously not able to only use the predictors (as they were for other analytes)  have to use the waveform

**End user of the device** :
* Hospitals and ambulances, in patient rooms used by nurses

**How this project will help them** :
* There is a broader project (automation of the finished goods process).  The cards are printed and then a random sample of cards are tested. They need to meet certain criteria per lot so that they can be released to the customers. At present, it’s a very manual process where operators look at waveforms to identify causes of problems. There is a threshold on how many pin contact errors there can be if the lot is to be released. 
* Our work will help automate this process (find a way to automatically label these things – decrease the amount of time the operators have to spend trying to identify them)

**Time windows** :
* Wet-up period : 
	- When the card is inserted in the reader, the valve is broken, the plunger comes out and pushes on the calibration fluid and that pushes the fluid to the sensor. When the fluid touches the sensor, it’s called the wet-up period. 
	- The first noisy period is wet-up. 
	- When looking at the waveforms, we can remove that period because it will not tell us anything about success or failure (48-50 seconds-ish) and then use noise reduction for the remaining part of the timeseries

**How the labelling works** :
* When a card is run, it has all 14 analytes on it, we are only looking at one analyte
* Some of the analytes depend on other analytes (ex: pH depends on C02 – if something goes wrong with pH, C02 will also be an unsuccessful test (seen in the return code))
* If a Test ID has been attributed the ‘unsuccessful’ code, operators go in and look at the waveforms of these test. Operators focus mainly on identifying pin contact errors and sample bubbles. 
* Pin contacts have more consistent waveforms compared to sample bubbles so should be easier to identify.
* Our goal is not to identify clusters that match with return codes. In our case, a combination of errors corresponds to a pin contact error.

**Fields in the raw data (comes out of analytical tools)** : 
* TestID : unique identifier
* ReturnCode : Decide whether the test is successful or a failure (many of the return codes could mean pin contact). The return code that is assigned is determined by the software using the various metrics that are calculated. Then, the operator verifies all the ‘unsuccessful’ readings and checks whether a pin contact error was the cause.
* C_ : measures come from the calibration window
* S_ : measures come from the sample window
* For the analyte we are looking at, it can take a while to stabilize (might be too noisy in the sample window) so we have a post window (P_)
* Generally, the post window will be smoother than the sample window
* T_ : trans window (will probably not be very useful to us, largely used for sensors conductivity)
* A_ : additional window, on calibration side

**Advisory committee presentation** :
* Introduction of the project and us
* Motivation
* Don’t have to be very specific
* Flow chart
