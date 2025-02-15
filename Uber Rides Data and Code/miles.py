from pandas import Categorical
import main
from plotly.express import *
import kaleido

# Store sum of miles driven per month
monthly_miles = main.data.groupby("Start Month")["MILES*"].sum().reset_index()

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
monthly_miles['Start Month'] = Categorical(monthly_miles['Start Month'], categories=months,ordered=True)

# Sort by calendar order
monthly_miles = monthly_miles.sort_values('Start Month')
# print(monthly_miles)

# Create an interactive Plotly bar chart
fig = bar(
    monthly_miles,
    x="Start Month",
    y="MILES*",
    text="MILES*",
    title="Total Miles Covered Per Month",
    labels={"MILES*": "Miles Driven", "Start Month": "Month"},
    color="MILES*",
    color_continuous_scale="blues"
)

fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
fig.update_layout(xaxis_title="Month", yaxis_title="Total Miles", plot_bgcolor="white")
fig.write_image("monthly_miles.png")
fig.show(renderer="browser")