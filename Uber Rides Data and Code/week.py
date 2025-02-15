from pandas import DataFrame
import main
from matplotlib.pyplot import *
from seaborn import *
from plotly.express import *

# Counts of Rides per Weekdays
rides_per_weekdays = main.data.groupby('Start Weekday').size()
# print(rides_per_weekdays)

# Create a plot to Analyze the rides per day
figure(figsize=(10,5))
barplot(x=rides_per_weekdays.index,hue=rides_per_weekdays.index,y=rides_per_weekdays.values,legend=False,order=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'], palette='coolwarm')
xlabel('Days')
ylabel('Number of Rides')
title("Uber Rides per Days")
savefig("rides_per_weekdays.png", dpi=300, bbox_inches="tight")
show()

# Store Weekend data
main.data["Weekend"] = main.data["Start Weekday"].isin(['Saturday','Sunday'])

# Count of rides per hour separately for weekdays and weekends
weekday_hours = main.data[main.data['Weekend'] == False]['Start Hour'].value_counts().sort_index()
# print(weekday_hours)
weekend_hours = main.data[main.data['Weekend'] == True]['Start Hour'].value_counts().sort_index()
# print(weekend_hours)

# Convert to DataFrame
hourly_data = DataFrame({
    'Hour': list(weekday_hours.index) + list(weekend_hours.index),
    'Number of Rides': list(weekday_hours.values) + list(weekend_hours.values),
    'Type': ['Weekday'] * len(weekday_hours) + ['Weekend'] * len(weekend_hours)
})

# Create interactive line chart
fig = line(hourly_data, x='Hour', y='Number of Rides', color='Type',
              title="Uber Rides: Weekdays vs. Weekends",
              markers=True, labels={'Hour': 'Hour of the Day', 'Number of Rides': 'Ride Count'},
              template='plotly_dark')
fig.write_image("weekday_hours.png")
fig.show(renderer="browser")