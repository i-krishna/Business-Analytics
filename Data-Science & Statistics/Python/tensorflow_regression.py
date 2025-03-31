# Python code

# Import necessary libraries
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# Sample data (replace this with actual process data from Steelcase)
process_data = np.array([28, 32, 30, 35, 33, 31, 29, 34, 32, 33], dtype=float)
target_values = np.arange(25, 35, 1)

# Normalize data
process_data_normalized = (process_data - np.mean(process_data)) / np.std(process_data)

# Build a simple linear regression model using TensorFlow
model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=1, input_shape=[1])
])

model.compile(optimizer='sgd', loss='mean_squared_error')

# Train the model
model.fit(process_data_normalized, target_values, epochs=1000, verbose=0)

# Make predictions
predictions = model.predict(process_data_normalized)

# Denormalize predictions
predictions_denormalized = predictions * np.std(process_data) + np.mean(process_data)

# Plot the results
plt.scatter(process_data, target_values, label='Actual Data')
plt.plot(process_data, predictions_denormalized, color='red', label='Regression Line')
plt.xlabel('Process Data')
plt.ylabel('Target Values')
plt.title(' Forecast model with TensorFlow')
plt.legend()
plt.show()
