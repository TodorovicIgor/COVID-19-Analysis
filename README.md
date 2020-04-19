# COVID-19 Data Analysis

## Intro

This repository contains simple python scripts used to fit gompertz curve to cumulative confirmed Coronavirus cases.

## Data

Data is fetched daily from [Johns Hopkins University Center for Systems Science and Engineering](https://github.com/CSSEGISandData/COVID-19),
ignoring data from China since their curve is skewed by a whole month, making it more difficult to fit curve for the rest of the world.


## Results
Current data looks like this:

<img src="/output/regression/img/04-19-2020.png" height="500" width="700px" />

Note: As more daily data arrives, the better estimation will be, since this is ongoing pandemic.\
That's why there is second graph, showing history of these estimations:

<img src="/output/end_estimation/04-19-2020.png" height="500" width="700px" />\
This plot should converge to specific value, marking the end of the pandemic.\
**As of 19. April 2020. estimated end of pandemic is 24. June 2020.**
 