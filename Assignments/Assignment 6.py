#Assignment (20/02/2026)

#Assignment Name : NumPy Speed Test
#Description : Compare Python lists vs NumPy arrays with 1M numbers, measure execution time, write 3 observations.

import time
import numpy as np

# Create 1 million numbers
size = 1_000_000

# Python List Test
start = time.time()

python_list = list(range(size))
squared_list = [x * 2 for x in python_list]

end = time.time()
list_time = end - start

print("Python List Time:", list_time, "seconds")


# NumPy Array Test
start = time.time()

numpy_array = np.arange(size)
squared_array = numpy_array * 2

end = time.time()
numpy_time = end - start

print("NumPy Array Time:", numpy_time, "seconds")


# Comparison
print("\nDifference:", list_time - numpy_time, "seconds")

