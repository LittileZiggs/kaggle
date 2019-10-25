from __future__ import absolute_import, division, print_function, unicode_literals

import tensorflow as tf
import pandas as pd
from numpy import *
from tensorflow.keras import datasets, layers, models

train = pd.read_csv('data/train.csv')
test = pd.read_csv('data/test.csv')
label = train.pop('label')
train_label = zeros((29400, 1))
val_label = zeros((12600, 1))
for i in range(29400):
    train_label[i][0] = label[i]

for j in range(12600):
    val_label[j][0] = label[j + 29400]

def convert2Dto3D(data_set):
    m,n = data_set.shape
    data_mat = zeros((((m, 28, 28, 1))))

    for i in range(m):
        for j in range(28):
            for k in range(28):
                data_mat[i][j][k][0] = data_set['pixel' + str(j * 28 + k)][i]

    return data_mat

train_mat = convert2Dto3D(train) / 255.0
test_data = convert2Dto3D(test) / 255.0

train_data = zeros((((29400, 28, 28, 1))))
val_data = zeros((((12600, 28, 28, 1))))
for i in range(29400):
    train_data[i, :, :, :] = train_mat[i, :, :, :]

for j in range(12600):
    val_data[j, :, :, :] = train_mat[j + 29400, :, :, :]

class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
               'dog', 'frog', 'horse', 'ship', 'truck']

model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))

model.summary()

model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))

model.summary()

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
model.fit(train_data, train_label, epochs=10,
                    validation_data=(val_data, val_label))

test_label = model.predict(test_data)
result = pd.DataFrame(index=range(test_label.shape[0]), columns = ['ImageId', 'Label'])
for i in range(test_label.shape[0]):
    result['ImageId'][i] = i + 1
    result['Label'][i] = argmax(test_label[i])
result.to_csv('data/submission_cnn.csv', index = False, encoding = 'utf-8')