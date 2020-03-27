import csv
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

today = datetime.today().strftime('%m-%d-%Y')
beginning = datetime(2020, 1, 22)
with open('output/regression/regression_history.csv', 'r') as file:
    reader = csv.reader(file)
    reader.__next__()
    ydata = []
    xdata = []
    for row in reader:
        ydata.append(int(row[5]))
        xdata.append(int(row[1]))
plt.scatter(xdata, ydata)
plt.xlabel('Days passed since 22. January')
plt.ylabel('Days from 22. January until the end of the pandemic')
# weighted mean for the last 5 days
ydata_mean = ydata[-5:]
w_sum = len(ydata_mean)*(len(ydata_mean)+1)/2
w_mean = 0
for index in range(len(ydata_mean)):
    w_mean += ydata_mean[index]*(index+1)/w_sum


end_date = (beginning + timedelta(days=int(w_mean))).strftime('%m-%d-%Y')
print(end_date)
plt.title('History of estimations')
plt.savefig('output/end_estimation/'+today+'.png', dpi=200)
plt.show()
