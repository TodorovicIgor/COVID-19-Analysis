# COVID-19 Data Analysis

## Intro

This is repository containing simple python scripts used to fit logistic curve to cumulative confirmed Coronavirus cases.

## Data

Data is fetched daily from [Johns Hopkins University Center for Systems Science and Engineering](https://github.com/CSSEGISandData/COVID-19),
ignoring data from China since their curve is skewed by a whole month, making it more difficult to fit curve for the rest of the world.


## Results
Current data looks like this:

<img src="/output/regression/img/03-27-2020.png" height="500" width="700px" />

Note: As more daily data arrives, the better estimation will be, since this is ongoing pandemic.\
That's why there is second graph, showing history of these estimations:

<img src="/output/end_estimation/03-27-2020.png" height="500" width="700px" />\
This plot should converge to specific value, marking the end of the pandemic.\
**DISCLAIMER:\
Results shown here are for entertainment purpose and are not intended to represent real events.\
Existing data is by no mean accurate, thus results are also NOT accurate.\
Having said that, as of 27. March 2020. estimated end of pandemic (which is probably not very accurate) is 12. June 2020.**
 