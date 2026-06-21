# 1. Why visualize?
# Looking at hundreds of rows in an excel sheet or a Pandas DataFrame makes it very difficult 
# to spot trends. A visual chart instantly highlights patterns (e.g., sales are going up every 
# summer) and outliers (e.g., one person paid $500 for a ticket while everyone else paid $10).

# 2. The Basic Workflow
# To draw anything in Matplotlib, you follow a 3-step pattern:
# - Import the library: `import matplotlib.pyplot as plt` (using `plt` is the industry standard).
# - Build the chart: Call a function like `plt.plot(x_data, y_data)` which draws the graphic in memory.
# - Display it: Call `plt.show()` to actually render the window and show the chart on your screen.

# 3. The Four Core Chart Types
# The hardest part of data visualization is picking the right chart:
# - Line plot (plt.plot): Best for tracking changes over a continuous sequence. 
#   Example: Tracking a company's stock price over a year.
# - Scatter plot (plt.scatter): Best for finding correlations between two numbers. 
#   Example: Plotting age on the X-axis and salary on the Y-axis to see if older people earn more.
# - Bar chart (plt.bar): Best for comparing distinct categories against a single number. 
#   Example: Average survival rate (number) by Passenger Class (category: First, Second, Third).
# - Histogram (plt.hist): Best for seeing the "spread" or "distribution" of ONE number. 
#   Example: Spreading ages into buckets (e.g., 0-10, 10-20) to see how many people fall into each.

# 4. Making Charts Readable
# A chart without labels is useless. Matplotlib provides tools to add context:
# - plt.title("My Chart"): Adds a title at the top.
# - plt.xlabel("Age") & plt.ylabel("Fare"): Labels what the X and Y axes represent.
# - plt.legend(): If you have two lines on one chart, a legend creates a key explaining colors.
# - figsize: An argument you can pass to make the chart window larger or smaller.

# 5. Multiple Plots
# Sometimes you want to show charts side-by-side (like a dashboard). 
# - plt.subplots(): An advanced tool that allows you to create a grid (like a 2x2 square) 
#   and place different charts into specific slots.