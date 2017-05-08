# Disaster Detection Using Twitter Data

### How To Run
```python ./detect.py <file containing tweets>```

You can also type ```python ./detect.py -h``` for more help on running the program

### How To Test The Classifier

The classifier can be tested using the command:
```python classify.py --test```

This will test the classifier using a 90% training to 10% testing split and average the results over 10 interations.

### Data
- Hurricane Irene tweets are available at [http://apollo.cse.nd.edu/datasets/irene_hurricane.txt](http://apollo.cse.nd.edu/datasets/irene_hurricane.txt)
- Hurricane Sandy tweets are available at [http://apollo.cse.nd.edu/datasets/sandy_hurricane.txt](http://apollo.cse.nd.edu/datasets/sandy_hurricane.txt)
- The tweets collected from Twitter streaming api are available in the [data folder](https://github.com/lkgarrison/disaster-detection/tree/master/data)

### Plotting the Relevant Tweets Per Hour
A csv file containing the number of relevant tweets per hour chronologically can be generated using the following command:

``` python plot.py <data> ```

This will output the resulting csv file to the **distributions** directory.

### Requirements
- python 2.7
- scipy
- numpy
- sklearn
