import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
days = np.arange(1, 11)
avg_delivery = np.random.randint(30, 60, size=10)   # minutes
std_dev = np.random.uniform(2, 8, size=10)          # standard deviation

plt.figure(figsize=(9, 5))
plt.errorbar(days, avg_delivery, yerr=std_dev, fmt='-o', color='blue',
             ecolor='red', capsize=5, label='Avg delivery time ± SD')
plt.title('Flipkart Average Delivery Time (10 Days)')
plt.xlabel('Day')
plt.ylabel('Delivery Time (minutes)')
plt.xticks(days)
plt.legend()
plt.grid(True)
plt.show()