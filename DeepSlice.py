from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical

import numpy
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
from tensorflow.keras.utils import plot_model
from tensorflow.keras.callbacks import EarlyStopping

seed = 9
numpy.random.seed(seed)

# load datasets
#csv files were filtered based on the data.
input_file = "large_dataset.txt"

dataset = pd.read_csv(input_file, header=None).values

# split into input (X) and output (Y) variables
X = dataset[:,0:8].astype("int32")
Y = dataset[:,8]

# preprocess data
# Standardize features by centering around 0 and scaling to unit variance
X_mean = X.mean(axis=0)
X_std = X.std(axis=0)
X = (X - X_mean) / X_std

encoder = LabelEncoder()
encoder.fit(Y)
encoded_Y = encoder.transform(Y)

# convert integers to dummy variables (i.e. one hot encoded)
y_one_hot = to_categorical(encoded_Y)

(X_train, X_val, Y_train, Y_val) = train_test_split(X, y_one_hot, test_size=0.2, random_state=seed)
(X_train, X_test, Y_train, Y_test) = train_test_split(X_train, Y_train, test_size=0.125, random_state=seed)

# create model
model = Sequential()
model.add(Dense(8, input_dim=8, kernel_initializer='normal', activation='relu'))
model.add(Dense(4, kernel_initializer='normal', activation='relu'))
model.add(Dense(3, kernel_initializer='normal', activation='tanh'))
model.add(Dense(3, kernel_initializer='normal', activation='softmax'))
print(model.summary())
# Compile model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Fit the model
early_stopping = EarlyStopping(monitor='val_loss', patience=3, min_delta=0.001, restore_best_weights=True)
history = model.fit(X_train, Y_train, validation_data=(X_val, Y_val), epochs=16, batch_size=128, callbacks=[early_stopping])

score = model.evaluate(X_test, Y_test, verbose=0)
print("Accuracy: %.2f%%" % (score[1]*100))
print("Loss: %.2f" % (score[0]*100))

# Plot training & validation accuracy values
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Model Accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()

# Plot training & validation loss values
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model Loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper right')
plt.show()
