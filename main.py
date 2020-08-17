import matplotlib.pyplot as mt
from matplotlib.ticker import MultipleLocator
import numpy as np
from setpy import spmean


directory_str = "datasets/"
spm = spmean(directory_str)
covidArr = spm.dataMean("03/01/2019", "04/31/2019", "03/01/2020", "04/31/2020")


dateArray = spm.returnDates()
print(dateArray)
numArry = spm.returnNum()
print(numArry)
# Graphing Data

def maxAvg(arr1, arr2):
    if max(arr1) > max(arr2):
        return max(arr1)
    else:
        return max(arr2)

width = 10
y_pos = np.arange(len(spm.names))
# c2016 = mt.bar(y_pos - width/4, covidArr[0], width, label='2016')
# c2017 = mt.bar(y_pos - width/5, covidArr[1], width, label='2017')
# c2018 = mt.bar(y_pos, covidArr[2], width, label='2018')
c2019 = mt.bar(y_pos - width/2, covidArr[0], width, label='2019')
c2020 = mt.bar(y_pos + width/2, covidArr[1], width, label='2020')

# mt.bar(y_pos, avgarr)

mt.xticks(y_pos, spm.names)
mt.yticks(np.arange(0, maxAvg(covidArr[0], covidArr[1])+1, 1.0))
mt.axes().yaxis.set_minor_locator(MultipleLocator(0.5))
mt.xlabel("Counties")
mt.ylabel("NO2 Levels (ppb)")
mt.title('New York Counties NO2 Daily Levels')
mt.legend()

def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    # autolabel() Code by MatPlotLib.
    for rect in rects:
        height = round(rect.get_height(), 2)
        mt.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(c2019)
autolabel(c2020)
mt.show()
