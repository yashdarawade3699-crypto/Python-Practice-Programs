import numpy as np
heart_rate=np.random.randit(80,151,10)
print(\Heart rates for 10 minutes:)
print(heart_rate)

first_5_minutes=np.average(heart_rate[:5])
print(first_5_minutes)

maximum=np.max(heart_rate)
print(maximum)
minimum=np.min(heart_rate)
print(minimum)
average=np.average(heart_rate)
print(average)

