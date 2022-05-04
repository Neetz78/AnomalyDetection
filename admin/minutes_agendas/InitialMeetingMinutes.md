# Initial Client Meeting Minutes
## May 3, 2022

- Started with introductions and icebreaker activity. 
- Learned about the system we are developing machine learning models for anomaly detection. It's a blood analysis system that measure the concentrations of different analytes. 
- The system has three components - a card, a reader, and a host. The card is where the chemical reactions occur that measure concentrations, the reader reads the signal over time, and the host processes information and displays it to the user. 
- After card inserted into reader - mechanical clamp pierces valve and squeezes out calibration fluid - passes over the sensor module. Get an initial measurement in amps/mamps/ohms. After some time (160-180 seconds), calibraion completes. Then specimen gets injected (blood for clinical use, quality control fluids for testing). Calibration fluid pushed out of the sensor into waste channel, and blood moves over the sensor so that the reader provides readings for the sensors.
- We are looking at anomaly detection for one of the analytes. Good tests have characteristic waveforms during calibration and injection. 
- One thing that can go wrong with with the readings is that the pins might not make adequate contact, in which case the electrical circuit is incomplete. 
- Ideally they would like us to create an unsupervised machine learning model to identify kinds of error, specifically they would like us to pull out pin contact errors as they tend to be hard to identify.
- For deliverales, they want us to come up with several potential machine pipelines and give them the code as well as our final report. They want to know what works, what doesn't work, what sort of works. They are looking for prototypes rather than polished code. 
- There are files for both successful and unsuccessful readings. Some files contain the raw waveforms while others contain summary information calculated from the waveforms. Both types are in csv files. Information can be joined based on test ID. 
- Ideally they want an unsupervised model because they don't trust their labels, but if we can't manage it, they would be happy with supervised models as well. 
- For the first week we are meeting with Aditya on a daily basis to dicuss our progress on the proposal. 
-  Throught the Capstone we will meet with Aditya, Mike, and Levannia on Mondays and Fridays to discuss progress. 
-  We also have additional committee meetings every second week starting from May 9. The first one we will present our proposal, the last we will present our final product. The intermediate ones we will present out progress and we are expected to send an agenda of what we wish to discuss prior to the meeting. 
-  We were also given a team charter to fill out. 
