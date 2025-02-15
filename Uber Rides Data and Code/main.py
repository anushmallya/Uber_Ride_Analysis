from pandas import *

# Storing "My Uber Drives - 2016.csv" as data
data = read_csv("My Uber Drives - 2016.csv")
# print(data.head(5))
# print(data.info())
# print(data.describe())

# Check for missing values in each column
# print(data.isnull().sum())

# Fill the missing values as "Unknown"
data['PURPOSE*']= data['PURPOSE*'].fillna("Unknown")
# print(data['PURPOSE*'])

# Convert "Start Date" and "End Date" column to datetime format
data['START_DATE*'] = to_datetime(data['START_DATE*'])
# print(data['START_DATE*'].head())
data['END_DATE*'] = to_datetime(data['END_DATE*'])
# print(data['END_DATE*'])

# Create a new Columns for "Start Hour", "Start Day", "Start Month", and "Start Weekday" from "Start Date"
data['Start Hour'] = data['START_DATE*'].dt.hour
# print(data['Start Hour'])
data['Start Day'] = data['START_DATE*'].dt.day
# print(data['Start Day'])
data['Start Month'] = data['START_DATE*'].dt.month_name()
# print(data['Start Month'])
data['Start Weekday'] = data['START_DATE*'].dt.day_name()
# print(data['Start Weekday'])

# Remove Duplicate rows
data.drop_duplicates(inplace=True)

# print(data.info())
# print(data.head())




