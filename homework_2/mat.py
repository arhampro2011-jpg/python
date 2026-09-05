# ================================
#  INTRODUCTION TO MATPLOTLIB
#  ACP - MY SAVINGS PROGRESS CHART
# ================================

# ================================================
#  ACTIVITY - MY SAVINGS PROGRESS CHART
# ================================================

# PART 1 - IMPORT MATPLOTLIB
# matplotlib.pyplot is the drawing tool.
# We use "plt" as its short nickname.
import matplotlib.pyplot as plt

# PART 2 - YOUR DATA
# weeks holds the x-axis labels.
# savings holds the amount saved each week.
weeks = ['Week 1', 'Week 2', 'Week 3', 'Week 4', 'Week 5']
savings = [20, 45, 70, 110, 150]

# PART 3 - PLOT A LINE GRAPH
# plt.plot(x, y) joins the savings amounts with a line.
plt.plot(weeks, savings)
plt.show()

# PART 4 - ADD LABELS AND A TITLE
# plt.title() adds a heading to the chart.
# plt.xlabel() labels the x-axis.
# plt.ylabel() labels the y-axis.
plt.plot(weeks, savings)
plt.title('My Savings Progress Chart')
plt.xlabel('Week')
plt.ylabel('Savings Amount')
plt.grid(True)
plt.ylim(0, 180)
plt.show()

# PART 5 - CUSTOMISE THE LINE CHART
# color changes the line colour.
# marker adds a dot at every data point.
# linestyle changes the line style.
# linewidth makes the line thicker.
plt.plot(weeks, savings, color='blue', marker='o',
         linestyle='dashed', linewidth=2)

plt.title('My Savings Progress Chart')
plt.xlabel('Week')
plt.ylabel('Savings Amount')
plt.grid(True)
plt.ylim(0, 180)
plt.show()

# PART 6 - DRAW A BAR CHART
# plt.bar(x, y) draws a bar for each week.
plt.bar(weeks, savings, color='orange')

plt.title('My Savings Bar Chart')
plt.xlabel('Week')
plt.ylabel('Savings Amount')
plt.ylim(0, 180)
plt.show()
