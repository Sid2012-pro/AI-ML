import matplotlib.pyplot as plt
import pandas as pd


min_percentage = 0.035

data = pd.read_csv('fifa_eda_stats.csv')


nationalities_count = data['Nationality'].value_counts()


total_players = len(data)


filtered_nationalities_count = nationalities_count[nationalities_count >= min_percentage * total_players]


other_count = total_players - filtered_nationalities_count.sum()
if other_count > 0:
  filtered_nationalities_count['Rest'] = other_count

plt.pie(filtered_nationalities_count, labels=filtered_nationalities_count.index, autopct='%1.1f%%', radius=3)

plt.show()
