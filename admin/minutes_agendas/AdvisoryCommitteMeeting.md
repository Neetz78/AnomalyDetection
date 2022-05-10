Minutes, meeting 2022-05-09 (30 minutes)

**Agenda : Presenting the proposal of the capstone problem**

**Presentation:**

 - The initial 15 minutes was spent on presentation.

**Questions and comments from advisors and data scientists:**

**Questions**

 -  **Difference between supervised and unsupervised learning?**
    Mentioned about how supervised and unsupervised learning works and linked it to the problem statement 
      
 -  **How do we plan on accommodating the different lengths of different signals?**
    We decided to try dynamic time warping to align two signals
    
 -  **How does mixture model work?**
    Mixture model works by assigning probability of each data point being in a predicted cluster
    
 -  **Where does feature selection portion of the project fall into?**
    The feature selection and engineering portion falls into the modelling phase of the project
    
 -  **How do you plan to augment the data?**
    We plan to identify the time window which is important in time series data. This wimdow will be primarily focussed to generate similar waveforms.
    
 **Comments**
 
 -  Comment on client generating more pin contact error data
    The ratio of pin contact to successful readings (80:1 million) seemed very big and hence the client decided to generate more pin contact readings synthetically
 
