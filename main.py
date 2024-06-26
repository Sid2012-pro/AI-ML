import matplotlib.pyplot as plt
import pandas as pd

# this variable uses pandas to read the fifa stats file
data = pd.read_csv('fifa_eda_stats.csv')

#this variable (named filtered variable for code readability conpares each line of the column 'Age' to 21 and if it is equal or larger than 21 it saves it in a list known as filtered data )
filtered_data = data[data['Age'] >= 21]
#this plots the 'filtered_data' list using matplotlib.pypylot's function 'hist' which plots a histogram
plt.hist(filtered_data['Age'] , edgecolor='black', color = 'skyblue')  

# for better readibility of the graph labels and titles are given to the y and x axis and he graph itself is labeled as well
plt.xlabel('Age')
plt.ylabel('Number of Players')
plt.title('Histogram of Player Ages (Over 21)')
plt.grid(True)

plt.show()
