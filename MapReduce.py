import pandas as pd
from functools import reduce
from collections import Counter
Traffic_data = pd.read_csv("/Users/Neal/Python/BigDataProject/Automated_Traffic_Volume_Counts_20250427.csv",usecols=['Yr', 'M', 'D', 'HH','Boro','street','Vol' ])
Weather_data = pd.read_csv("/Users/Neal/Python/BigDataProject/final_cleaned_traffic_weather.csv", usecols=['date', 'conditions'])

Traffic_hours = Traffic_data['HH']
Traffic_hours.tolist()

hotspots = [0,0]

#Finding Peak Traffic Hours
a = Traffic_hours
count = Counter(a)
f = count.most_common(3)
print("The peak traffic hours are")
for i in range(3):
    print(f[i][0], "o'clock")

#Finding Congestion Hotspots

def map_function_Hotspot(List):
    s = List['street'].tolist()
    b = List['Boro'].tolist()
    v = List['Vol'].tolist()
    return [s,b,v]

def reduce_function_Hotspot(a):
    list = a
    idx = 0
    max_vol = list[2][0]
    print(max_vol)
    for i in range (1,len(Traffic_data)):
        if list[2][i] > max_vol:
            max_vol = list[2][i]
            idx = i
    hotspots[0] = list[0][i]
    hotspots[1] = list[1][i]
    #print(hotspots[0])
    h = str(hotspots[0]) + " " + str(hotspots[1])
    return h

temp = map_function_Hotspot(Traffic_data)
print("A Traffic hotspot is " , reduce_function_Hotspot(temp))






