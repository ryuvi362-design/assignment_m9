import matplotlib.pyplot as plt

days = ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5', 'Day 6', 'Day 7']
spotify = [12000, 13500, 12800, 15000, 16200, 18000, 17500]
youtube = [20000, 21000, 22500, 21500, 24000, 26000, 25000]

fig, ax = plt.subplots(figsize=(10, 5))

ax.fill_between(days, youtube, color='red', alpha=0.5, label='YouTube')
ax.fill_between(days, spotify, color='green', alpha=0.6, label='Spotify')

ax.set_title('Daily Active Users Analytics', fontsize=14, fontweight='bold')
ax.set_xlabel('Day of the Week')
ax.set_ylabel('Number of Active Users')
ax.grid(True, linestyle='--', alpha=0.6)
ax.legend()

plt.tight_layout()
plt.show()