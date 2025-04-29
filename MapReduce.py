import pandas as pd
Traffic_data = pd.read_csv("/Users/Neal/Python/BigDataProject/Automated_Traffic_Volume_Counts_20250427.csv",usecols=['Yr', 'M', 'D', 'HH'])
Weather_data = pd.read_csv("/Users/Neal/Python/BigDataProject/New_York__NY__United_States.csv", usecols=['conditions'])

