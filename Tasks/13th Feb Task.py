#Create numpy array with the following temperature(celcius)[28,32,30,37,36,38]  Requirements: convert the list into numpy array print maximum and minimum temp calculate average temp display last 3 days temp
import numpy as np

# Given temperature list
temps = [28, 32, 30, 37, 36, 38]

# Convert list to numpy array
temp_array = np.array(temps)

# Print maximum and minimum temperature
print("Maximum Temperature:", np.max(temp_array))
print("Minimum Temperature:", np.min(temp_array))

# Calculate average temperature
print("Average Temperature:", np.mean(temp_array))

# Display last 3 days temperature
print("Last 3 Days Temperature:", temp_array[-3:])

