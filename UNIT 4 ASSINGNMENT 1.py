import numpy as np

heart_rate = np.random.randint(80, 151, 10)

print("\nHeart rates for 10 minutes:")
print(heart_rate)

first_5_minutes = np.average(heart_rate[:5])
print("\nAverage of first 5 minutes:")
print(first_5_minutes)

maximum = np.max(heart_rate)
print("\nMaximum heart rate:")
print(maximum)

minimum = np.min(heart_rate)
print("\nMinimum heart rate:")
print(minimum)

average = np.average(heart_rate)
print("\nOverall average heart rate:")
print(average)

high_rate = heart_rate > 120
print("\nHeart rate exceeding 120 BPM:")
print(heart_rate[high_rate])

minutes = np.where(heart_rate > 120)[0] + 1
print("\nMinutes exceeding 120 BPM:")
print(minutes)
