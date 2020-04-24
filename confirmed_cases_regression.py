import matplotlib.pyplot as plt
import csv
import numpy as np
from scipy.optimize import curve_fit
from datetime import datetime, timedelta


def gompertz_model(x, a, b, c):
    return np.multiply(a, np.exp(-np.multiply(b, np.exp(-np.multiply(c, x)))))


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
xdata_prediction = [i for i in range(int(2*popt[1])+20)]  # logistic

begin = datetime(2020, 1, 22)

popt2, pcov2 = curve_fit(gompertz_model, xdata, ydata, maxfev=5000)
plt.xlabel('Days since 22. January')
plt.ylabel('Total cases')
gompertz_xdata = []
for i in range(80, 1000):
    if (gompertz_model(i, *popt2) - gompertz_model(i-1, *popt2))/gompertz_model(i, *popt2) < 0.001:
        gompertz_xdata = [j for j in range(i)]
        end = (begin + timedelta(days=i)).strftime('%m-%d-%Y')
        break
# plt.plot(logistic_model(gompertz_xdata, *popt), 'r--')
plt.plot(gompertz_model(gompertz_xdata, *popt2), 'g--')
plt.title('Today\'s date: '+today+'\nEstimated end: '+end)
plt.plot(ydata, 'b')
plt.legend(['Gompertz Forecast', 'Actual'], loc='upper left')

# saving plot
plt.savefig('output/regression/img/'+today+'.png', dpi=200)
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

        row = [today, days_since_beginning, '-', '-', end, i, int(popt2[0])]
        # scientific notation messes everything up, solution is to traverse ydata array, apparently astype doesn't work
        for item in ydata:
            row.append(int(item))
        writer.writerow(row)
plt.show()
