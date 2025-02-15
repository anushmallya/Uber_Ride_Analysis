import main
from matplotlib.pyplot import *
from seaborn import *

# Create a plot to analyze the count of purpose customers travel
figure(figsize=(15,10))
countplot(x='PURPOSE*', data=main.data, palette='Set2',hue='PURPOSE*',legend=False)
xlabel("Ride Category")
ylabel("Count")
title("Purpose")
show()