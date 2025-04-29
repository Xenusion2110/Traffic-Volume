import pandas as pd
from datetime import datetime
from sklearn.preprocessing import MinMaxScaler

# Loading Traffic Data
traffic_df = pd.read_csv("/Users/mohdshoyeb/Desktop/Big data Analytics/Project/nyc-traffic-analytics/data/Automated_Traffic_Volume_Counts_20250429.csv",
    usecols=['Yr', 'M', 'D', 'HH', 'Vol']  # Make sure 'Vol' exists
)

traffic_df['date'] = pd.to_datetime(dict(year=traffic_df['Yr'], month=traffic_df['M'], day=traffic_df['D']))
traffic_df['hour'] = traffic_df['HH']

# Loading Weather Data
weather_df = pd.read_csv("/Users/mohdshoyeb/Desktop/Big data Analytics/Project/nyc-traffic-analytics/data/New_York__NY__United_States.csv",
    usecols=['datetime', 'conditions']
)

weather_df['datetime'] = pd.to_datetime(weather_df['datetime'])
weather_df['date'] = weather_df['datetime'].dt.date
weather_df['hour'] = weather_df['datetime'].dt.hour

traffic_df['date'] = pd.to_datetime(traffic_df['date']).dt.date

merged_df = pd.merge(traffic_df, weather_df, on=['date', 'hour'], how='left')

merged_df.dropna(subset=['conditions'], inplace=True)
merged_df.drop_duplicates(inplace=True)

merged_df['is_rain'] = merged_df['conditions'].str.contains('Rain', case=False, na=False)
merged_df['is_snow'] = merged_df['conditions'].str.contains('Snow', case=False, na=False)
merged_df['day_of_week'] = pd.to_datetime(merged_df['date']).dt.dayofweek
merged_df['is_weekend'] = merged_df['day_of_week'] >= 5

# Outlier Removal for Volume
Q1 = merged_df['Vol'].quantile(0.25)
Q3 = merged_df['Vol'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

merged_df = merged_df[(merged_df['Vol'] >= lower_bound) & (merged_df['Vol'] <= upper_bound)]

# Encoding Weather Conditions
merged_df['weather_main'] = merged_df['conditions'].str.extract(r'(\w+)', expand=False)
merged_df['weather_main'] = merged_df['weather_main'].astype('category')
merged_df['weather_main_code'] = merged_df['weather_main'].cat.codes

scaler = MinMaxScaler()
merged_df['Vol_scaled'] = scaler.fit_transform(merged_df[['Vol']])

# Saving Final Dataset
merged_df.to_csv("/Users/mohdshoyeb/Desktop/Big data Analytics/Project/nyc-traffic-analytics/data/final_cleaned_traffic_weather.csv",
    index=False
)
print("Final cleaned dataset saved as 'final_cleaned_traffic_weather.csv'")
