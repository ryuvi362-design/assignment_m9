import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

dates = pd.date_range(end=pd.Timestamp.today().normalize(), periods=14)
balance = [1500, 1420, 1350, 1800, 1750, 1600, 1550,
           1480, 1900, 1850, 1700, 1650, 1580, 1520]

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(dates, balance, marker='o', color='teal')
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d %b'))
ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))
plt.xticks(rotation=45)
ax.set_title('Paytm Wallet Balance (Last 14 Days)')
ax.set_xlabel('Date')
ax.set_ylabel('Balance (₹)')
plt.tight_layout()
plt.show()