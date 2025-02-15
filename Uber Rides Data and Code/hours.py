import main
from matplotlib.pyplot import *
from seaborn import *

# Count of rides in an hour
rides_per_hour = main.data.groupby('Start Hour').size()
# print(rides_per_hour)

# Create a plot to Analyze the rides per hour in a Day
figure(figsize=(10, 5))
lineplot(x=rides_per_hour.index, y=rides_per_hour.values,hue=rides_per_hour.index,legend=False, marker="o", color="b")
xlabel("Hour of the Day")
ylabel("Number of Rides")
title("Uber Rides Per Hour of the Day")
savefig("rides_per_hour.png", dpi=300, bbox_inches="tight")
show()

# Create a table for rides per hour and weekday and fill the missing field with 0
max_ride_hour_in_day = main.data.pivot_table(index='Start Hour',columns="Start Weekday",values="START_DATE*",aggfunc='count')
max_ride_hour_in_day=max_ride_hour_in_day.fillna(0)

# Reorder the columns on weekday
max_ride_hour_in_day = max_ride_hour_in_day[['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']]
# print(max_ride_hour_in_day)

# Create a plot Heatmap to analyze the peak ride hours in weekday
figure(figsize=(10,6))
heatmap(max_ride_hour_in_day, cmap='coolwarm', linewidths=0.5, annot=True)
title("Uber Ride Frequency by Hour and Day of the Week")
xlabel("Day of the week")
ylabel("Hour of the Day")
show()