import matplotlib.pyplot as plt

days = ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5', 'Day 6', 'Day 7']
spotify = [12000, 13500, 12800, 15000, 16200, 18000, 17500]
youtube = [20000, 21000, 22500, 21500, 24000, 26000, 25000]

plt.figure(figsize=(9, 5))
plt.fill_between(days, youtube, color='red', alpha=0.5, label='YouTube')
plt.fill_between(days, spotify, color='green', alpha=0.6, label='Spotify')
plt.title('Daily Active Users: Spotify vs YouTube')
plt.xlabel('Days')
plt.ylabel('Active Users')
plt.legend()
plt.show()