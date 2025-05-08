import pandas as pd
from functools import reduce
from collections import Counter
Traffic_data = pd.read_csv("/Users/Neal/Python/BigDataProject/Automated_Traffic_Volume_Counts_20250427.csv",usecols=['Yr', 'M', 'D', 'HH','Boro','street','Vol' ])
Weather_data = pd.read_csv("/Users/Neal/Python/BigDataProject/final_cleaned_traffic_weather.csv", usecols=['Vol', 'is_rain', 'is_snow'])

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
    for i in range (1,len(Traffic_data)):
        if list[2][i] > max_vol:
            max_vol = list[2][i]
            idx = i
    hotspots[0] = list[0][idx]
    hotspots[1] = list[1][idx]
    h = str(hotspots[0]) + " " + str(hotspots[1])
    return h

temp = map_function_Hotspot(Traffic_data)
print("A Traffic hotspot is " , reduce_function_Hotspot(temp))

#Traffic Volume Trend 

def map_function_Trend(a):
    List = a
    y = List['Yr']
    v = List['Vol'].tolist()
    return [y,v]


def reduce_function_Trend2(v1, v2):
    
    voldiff = v2 - v1
    trend = (voldiff/v1) * 100
    return trend
    

def reduce_function_Trend1(list, year):
    list = list
    idx = 0
    max_vol = 0
    year = year
    for i in range(1, len(Traffic_data)):
        if list[0][i] == year:
            if list[1][i] > max_vol:
                max_vol = list[1][i]
                idx = i
    return list[1][idx]

temp = map_function_Trend(Traffic_data)
l = reduce_function_Trend1(temp, 2015)
l2 = reduce_function_Trend1(temp, 2024)
print("The volume for rain has changed by ", reduce_function_Trend2(l,l2), "%")


#Most Affected during Hazardous weather

def map_function_Weather(a, b):
    List = a
    List2 = b
    r = List['is_rain']
    s = List['is_snow']
    v = List['Vol']
    st = List2['street']
    return [r,s,v,st]

def reduce_function_Weather(a):
    List = a
    idx = 0
    idx2 = 0
    max_vol = List[2][0]
    for i in range (1, len(Weather_data)):
        if List[0][i] == True or List[1][i] == True:
            if List[2][i] > max_vol:
                max_vol = List[2][i]
                idx2 = idx
                idx = i
    l1 = List[3][idx]
    l2 = List[3][idx2]
    return [l1, l2]

temp = map_function_Weather(Weather_data, Traffic_data)
w = reduce_function_Weather(temp)
print("The areas most affected by weather are ", w[0], " and ", w[1])
                



    




    
    







