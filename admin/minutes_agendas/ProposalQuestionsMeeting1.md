# Chat with Aditya Minutes
## May 3, 2022

In this meeting we had a list of questions to clarify what they want out of this project so that we can write our proposal. 

What kind of license do we need for our git repo (permissive vs copyrighted)
- Probably MIT but they will get back to us. 

Is it fair to say that our main goal with this project is to perform unsupervised clustering on the unsuccessful time series data? In this case, are we mainly ignoring the successful data?
- Sort of. We are focussed on clustering the unsuccessful readings but there aren't that many of them. As a result, we will likely use the successful readings to do some weight inititialization. 

What are the priorities in terms of using the time series vs the raw predictors?
- We are going to use both. For instance, we might run a random forest on the predictors to get an idea of variable importance and use them for an SVM. Then we could do somethin like a CNN or dynamic time warping on the raw time series. 
- We are going to need to perform some sort of noise filtering on the time series before feeding them into the CNN. 
- We also probably want to look at plots and split the time series into windows before feeding into a model. 

Am I correct in thinking the time series are the raw sensor readings over time whereas raw data predictors are summary data that have been derived from the  time series? Or are they separate? In either case how are they collected?
- Yes, so they are not unrelated. 

We haven't actually learned how to deal with time series data in the program. Do you have any good resources you would suggest?
- The Keras documentation is very good. 

How do some TestId end up in the PinContact file, how do they detect that there is an error there.
- PinContact is a subset of the unsseccsful data file where the reading have been manually identified as having pin contact issues. 

What does the column returncode signify?
- It's not important for now. They are indicators that might be usefull for identifying pin contact?

What are the expected deliverables?
- Code for various attempted pipelines and a copy of our final report. 
