from datetime import date
import pandas as pd


Traffic_data = pd.read_csv("/Users/Neal/Python/BigDataProject/Automated_Traffic_Volume_Counts_20250427.csv",usecols=['Yr', 'M', 'D'])
Year = Traffic_data['Yr']
Month = Traffic_data['M']
Day = Traffic_data['D']
dates = []
for i, value in Traffic_data['Yr'].items():
    dates[i] = date(Year[i], Month[i], Day[i])
