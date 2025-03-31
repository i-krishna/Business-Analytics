# Python code

import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Sample data (replace this with actual process data from Steelcase)
process_data = np.array([28, 32, 30, 35, 33, 31, 29, 34, 32, 33])

# Step 1: Analyze the current process
# Calculate mean and standard deviation
mean = np.mean(process_data)
std_dev = np.std(process_data)

# Create a histogram
plt.hist(process_data, bins=range(25, 40), edgecolor='black')
plt.title('Current Process Histogram')
plt.xlabel('Process Value')
plt.ylabel('Frequency')
plt.show()

# Step 2: Implement Lean/Six Sigma principles
# Perform a process capability analysis using statsmodels
process_capability = sm.stats.ProcessCapability(process_data, lsl=25, usl=35)

# Display process capability analysis results
print(process_capability.summary())

# Step 3: Make improvements (if necessary)
# Implement changes to the process based on the analysis

# Step 4: Verify improvements
# Repeat the capability analysis after implementing changes

# Display updated process capability analysis results
print(process_capability.summary())
