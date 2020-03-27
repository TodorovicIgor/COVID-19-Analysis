import matplotlib.pyplot as plt
import csv
import numpy as np
from scipy.optimize import curve_fit
from datetime import datetime, timedelta
import os


def logistic_model(x, a, b, c):
    return c/(1+np.exp(-(x-b)/a))


today = datetime.today().strftime('%m-%d-%Y')
matrix = []

# TODO pandas for reading .csv
with open('time_series_covid19_confirmed_global.csv', 'r') as file:
    reader = csv.reader(file)
    header = reader.__next__()
    days_since_beginning = len(header)-4
    ydata = np.zeros(shape=len(header)-4, dtype='float64')
    xdata = np.arange(start=0, stop=len(header)-4, dtype='float64')
    for row in reader:
        if row[1] == 'China':
            continue
        # TODO slicing
        for index in range(4, len(row)):
            ydata[index-4] += int(row[index])

popt, pcov = curve_fit(logistic_model, xdata, ydata, maxfev=5000)
xdata_prediction = [i for i in range(int(2*popt[1]))]

plt.plot(logistic_model(xdata_prediction, *popt), 'r--')
plt.plot(ydata, 'b')
plt.legend(['Forecast', 'Actual'], loc='upper left')
plt.xlabel('Days since 22. January')
plt.ylabel('Total cases')
begin = datetime(2020, 1, 22)
inflection = (begin + timedelta(days=int(popt[1]))).strftime('%m-%d-%Y')
end = (begin + timedelta(days=int(2*popt[1]))).strftime('%m-%d-%Y')
plt.title('Today\'s date: '+today+'\nInflection point: '+inflection+'\nEstimated end: '+end)

# saving plot
if not os.path.exists('output/regression/img/'+today+'.png'):
    plt.savefig('output/regression/img/'+today+'.png', dpi=1000)

# appending data to .csv if not already appended
with open('output/regression/regression_history.csv', 'r', newline='') as file:
    reader = csv.reader(file)
    new_day = True
    for row in reader:
        if row[0] == today:
            new_day = False
            break
if new_day:
    with open('output/regression/regression_history.csv', 'a', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        row = [today, days_since_beginning, inflection, int(popt[1]), end, int(2*popt[1]), int(popt[2])]
        # scientific notation messes everything up, solution is to traverse ydata array, apparently astype doesn't work
        for item in ydata:
            row.append(int(item))
        writer.writerow(row)

# plt.clf()
plt.show()
