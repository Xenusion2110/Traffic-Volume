import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

Traffic_data = pd.read_csv("/Users/Neal/Python/BigDataProject/Automated_Traffic_Volume_Counts_20250427.csv",usecols=['Yr', 'M', 'D', 'HH','Boro','street','Vol' ])
Weather_data = pd.read_csv("/Users/Neal/Python/BigDataProject/final_cleaned_traffic_weather.csv", usecols=['Vol', 'is_rain', 'is_snow'])

def NeededData(a, b):
    List = a
    List2 = b
    r = List['is_rain']
    s = List['is_snow']
    v = List['Vol']
    st = List2['street']
    return [r,s,v,st]

def MaxVolumes(a):
    List = a
    idx = 0
    idx2 = 0
    idx3 = 0
    idx4 = 0
    idx5 = 0
    idx6 = 0
    max_vol = List[2][0]
    for i in range (1, len(Weather_data)):
        if List[0][i] == True or List[1][i] == True:
            if List[2][i] > max_vol:
                max_vol = List[2][i]
                idx6 = idx5
                idx5 = idx4
                idx4 = idx3
                idx3 = idx2
                idx2 = idx
                idx = i
    return [List[2][idx], List[2][idx2], List[2][idx3],List[2][idx4],List[2][idx5],List[2][idx6]]

def StreetNames(a):
    List = a
    idx = 0
    idx2 = 0
    idx3 = 0
    idx4 = 0
    idx5 = 0
    idx6 = 0
    max_vol = List[2][0]
    for i in range (1, len(Weather_data)):
        if List[0][i] == True or List[1][i] == True:
            if List[2][i] > max_vol:
                max_vol = List[2][i]
                idx6 = idx5
                idx5 = idx4
                idx4 = idx3
                idx3 = idx2
                idx2 = idx
                idx = i
    l1 = List[3][idx]
    l2 = List[3][idx2]
    l3 = List[3][idx3]
    l4 = List[3][idx4]
    l5 = List[3][idx5]
    l6 = List[3][idx6]
    return [l1, l2, l3, l4, l5, l6]

a = NeededData(Weather_data, Traffic_data)
# plotting a bar chart
plt.bar(StreetNames(a), MaxVolumes(a))

# naming the x-axis
plt.xlabel('Streets')
# naming the y-axis
plt.ylabel('Traffic Volume')
# plot title
plt.title('Most Affected Streets During Rain Or Snow')

# function to show the plot
plt.show()

print('Lol')