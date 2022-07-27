import numpy as np
from scipy import stats
import skuskove as skus
import matplotlib.pyplot as plt


dates = skus.column_to_array("../data/final_data/Student1", 0)
times_s1 = skus.column_to_array("../data/final_data/Student1", 1)
times_s2 = skus.column_to_array("../data/final_data/Student2", 1)
times_s3 = skus.column_to_array("../data/final_data/Student3", 1)
times_s4 = skus.column_to_array("../data/final_data/Student4", 1)

total_times = []


intervals = skus.select_skuskove(dates)

mimo_s1 = list(map(float, skus.get_mimo(intervals, times_s1)))
skuskove_s1 = list(map(float, skus.get_skuskove(intervals, times_s1)))

mimo_s2 = list(map(float, skus.get_mimo(intervals, times_s2)))
skuskove_s2 = list(map(float, skus.get_skuskove(intervals, times_s2)))

mimo_s3 = list(map(float, skus.get_mimo(intervals, times_s3)))
skuskove_s3 = list(map(float, skus.get_skuskove(intervals, times_s3)))

mimo_s4 = list(map(float, skus.get_mimo(intervals, times_s4)))
skuskove_s4 = list(map(float, skus.get_skuskove(intervals, times_s4)))

mimo_all = mimo_s1 + mimo_s2 + mimo_s3 + mimo_s4
skuskove_all = skuskove_s1 + skuskove_s2 + skuskove_s3 + skuskove_s4

# rozptyl som nastavila, že nie je rovnaký, dunno why, nepríde mi, že by mal byť rovnaký
# print(np.var(skuskove_all))
# print(np.var(mimo_all))

# print(np.mean(mimo_all))
# print(np.mean(skuskove_all))

# dokopy: H_0 vs. H_1
print(stats.ttest_ind(skuskove_all, mimo_all, equal_var=False, alternative="less"))

# TODO: dokresliť pdf exponenciálnej fc so správnym parametrom

plt.hist(mimo_all, 30, (0,12.7), color="violet")

plt.xlabel("Time spent on Netflix")
plt.ylabel("Frequency")
plt.title("Histogram časov mimo skúškového")

plt.show()

