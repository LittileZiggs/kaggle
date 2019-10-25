from __future__ import absolute_import, division, print_function, unicode_literals

import tensorflow as tf
import pandas as pd
from numpy import *

train = pd.read_csv('data/train.csv')
test = pd.read_csv('data/test.csv')
train_label = train.pop('label')
label = zeros((42000, 1))
for i in range(42000):
    label[i][0] = train_label[i]

def convert2Dto3D(data_set):
    m,n = data_set.shape
    data_mat = zeros(((m, 28, 28)))

    for i in range(m):
        for j in range(28):
            for k in range(28):
                data_mat[i][j][k] = data_set['pixel' + str(j * 28 + k)][i]

    return data_mat

train_data = convert2Dto3D(train) / 255.0
test_data = convert2Dto3D(test) / 255.0

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_data, label, epochs=5)

test_label = model.predict(test_data)
result = pd.DataFrame(index=range(test_label.shape[0]), columns = ['ImageId', 'Label'])
for i in range(test_label.shape[0]):
    result['ImageId'][i] = i + 1
    result['Label'][i] = argmax(test_label[i])
result.to_csv('data/submission_simple.csv', index = False, encoding = 'utf-8')