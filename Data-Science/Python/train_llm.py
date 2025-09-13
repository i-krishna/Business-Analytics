# This code builds and trains a simple language model using TensorFlow and Keras. 
# It uses an embedding layer, two LSTM layers, and a dense output layer. 
# The model is trained on X_train and y_train, and its performance is validated on X_val and y_val after each epoch.
# Validation accuracies are printed at the end.

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense

# Example data (replace with your actual tokenized data)
X_train, y_train = ...  # Training data
X_val, y_val = ...      # Validation data

# Build a simple language model
model = Sequential([
    Embedding(input_dim=10000, output_dim=128),
    LSTM(256, return_sequences=True),
    LSTM(256),
    Dense(10000, activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model and validate after each epoch
history = model.fit(
    X_train, y_train,
    epochs=10,
    batch_size=64,
    validation_data=(X_val, y_val)  # Validation after each epoch
)

# Access validation accuracy after each epoch
val_accuracies = history.history['val_accuracy']
print("Validation accuracies after each epoch:", val_accuracies)

