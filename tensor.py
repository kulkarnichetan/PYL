import tensorflow as tf
import pandas as pd
import numpy as np

# 1. Create a constant tensor
tf.constant([[10, 20], [30, 40]])

# 2. Create a variable tensor
tf.Variable([[1.5, 2.5], [3.5, 4.5]])

# 3. Read CSV using pandas and convert to tensor
df = pd.read_csv('your_data.csv')  # Replace with your CSV file path
tf.convert_to_tensor(df.values, dtype=tf.float32)

# 4. Add two tensors
tf.add([1, 2], [3, 4])

# 5. Multiply tensors element-wise
tf.multiply([2, 3], [4, 5])

# 6. Matrix multiplication
a = tf.constant([[1, 2]])
b = tf.constant([[3], [4]])
tf.matmul(a, b)

# 7. Reshape a tensor
t = tf.constant([1, 2, 3, 4])
tf.reshape(t, (2, 2))

# 8. Create a tensor of zeros
tf.zeros([2, 3])

# 9. Create a tensor of ones
tf.ones([3, 2])

# 10. Create a tensor with normally distributed random values
tf.random.normal([3, 3], mean=0, stddev=1)

# 11. Reduce sum over all elements
tf.reduce_sum([[1, 2], [3, 4]])

# 12. Reduce mean of a tensor
tf.reduce_mean([1, 2, 3, 4, 5])

# 13. Apply softmax activation
tf.nn.softmax([2.0, 1.0, 0.1])

# 14. Apply sigmoid activation
tf.nn.sigmoid([-1.0, 0.0, 1.0])

# 15. Apply ReLU activation
tf.nn.relu([-3.0, 0.0, 2.0])

# 16. Create a dense layer and pass a tensor
dense = tf.keras.layers.Dense(3, activation='relu')
dense(tf.constant([[1.0, 2.0]]))  # Simulates 1 input sample with 2 features

# 17. Normalize a tensor (like min-max normalization on CSV values)
x = tf.constant([10, 20, 30, 40], dtype=tf.float32)
(x - tf.reduce_min(x)) / (tf.reduce_max(x) - tf.reduce_min(x))

# 18. One-hot encode integer labels
tf.one_hot([0, 1, 2], depth=3)

# 19. Create a small model with Keras Sequential
model = tf.keras.Sequential([
    tf.keras.layers.Dense(8, activation='relu', input_shape=(4,)),
    tf.keras.layers.Dense(3, activation='softmax')
])
model.summary()

# 20. Save and load a Keras model
model.save('my_simple_model')  # Saves model
loaded_model = tf.keras.models.load_model('my_simple_model')  # Loads it
