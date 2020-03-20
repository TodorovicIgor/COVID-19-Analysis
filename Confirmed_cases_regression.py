import matplotlib.pyplot as plt
import csv
import numpy as np
from scipy.optimize import curve_fit
from datetime import datetime, timedelta
import os


def model(x, brzina_zaraze, dan_sa_najvecim_porastom, ukupno_zarazenih):
    return ukupno_zarazenih/(1+np.exp(-(x-dan_sa_najvecim_porastom)/brzina_zaraze))


today = datetime.today().strftime('%d-%m-%Y')
matrix = []

# xdata = np.linspace(0, 57, 1)
# TODO pandas for reading .csv
with open('data_confirmed.csv', 'r') as file:
    reader = csv.reader(file)
    header = reader.__next__()
    ydata = [0 for _ in range(len(header)-4)]
    xdata = [i for i in range(len(header)-4)]
    for row in reader:
        if row[1] == 'China':
            continue
        # TODO slicing
        for index in range(4, len(row)):
            ydata[index-4] += int(row[index])

popt, pcov = curve_fit(model, xdata, ydata)
xdata_prediction = [i for i in range(int(2*popt[1]))]

plt.plot(model(xdata_prediction, *popt), 'r--')
plt.plot(ydata, 'b')
plt.legend(['Predikcija', 'Stvarni slucajevi'], loc='upper left')
plt.xlabel('Dana od 22. Januara')
plt.ylabel('Ukupno slucajeva')
begin = datetime(2020, 1, 22)
inflection = (begin + timedelta(days=int(popt[1]))).strftime('%d-%m-%Y')
end = (begin + timedelta(days=int(2*popt[1]))).strftime('%d-%m-%Y')
plt.title('Trenutni dan: '+today+'\nPromena nagiba: '+inflection+'\nKraj: '+end)

# saving plot
if not os.path.exists(today+'.png'):
    plt.savefig(today+'.png', dpi=150)

# appending data to .csv if not already appended
with open('regression.csv', 'r', newline='') as file:
    reader = csv.reader(file)
    new_day = True
    for row in reader:
        if row[1] == today:
            new_day = False
            break
with open('regression.csv', 'a', newline='') as file:
    if new_day:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(['date: ', today])
        writer.writerow(['expected end: ', end, int(2*popt[1])])
        writer.writerow(['inflection point: ', inflection, int(popt[1])])
        writer.writerow(['total cases: ', popt[2]])
        writer.writerow(['data: ']+ydata)

plt.show()
