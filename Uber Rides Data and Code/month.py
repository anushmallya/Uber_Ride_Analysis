import main
from matplotlib.pyplot import *
from seaborn import *

# Count of rides in a months
rides_per_month = main.data.groupby('Start Month').size()
# print(rides_per_month)

# Reorder the months in the data
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
rides_per_month = rides_per_month.reindex(months)

# Create a plot to Analyze the rides per month
figure(figsize=(10,5))
barplot(x=rides_per_month.index,hue=rides_per_month.index,legend=False, y=rides_per_month.values, palette='viridis')
xlabel("Month")
ylabel("Number of Rides")
title("Uber Rides per Month")
savefig("rides_per_month.png", dpi=300, bbox_inches="tight")
show()
