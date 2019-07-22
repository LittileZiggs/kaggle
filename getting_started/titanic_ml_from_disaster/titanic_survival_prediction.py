import pandas as pd
from sklearn.linear_model import LogisticRegressionCV as lrcv
from numpy import *

def load_dataset(fileName):
    raw_datamat = pd.read_csv(fileName)
    return raw_datamat

def preprocess_data(raw_dataMat):
    m,n = shape(raw_dataMat)
    label = mat(raw_dataMat['Survived']).T

    dataMat = zeros((m,11))
    age_mean = raw_dataMat['Age'].mean()
    raw_dataMat['Age'].fillna(age_mean, inplace=True)
    age_min = raw_dataMat['Age'].min()
    age_max = raw_dataMat['Age'].max()
    sibsp_min = raw_dataMat['SibSp'].min()
    sibsp_max = raw_dataMat['SibSp'].max()
    parch_min = raw_dataMat['Parch'].min()
    parch_max = raw_dataMat['Parch'].max()
    fare_min = raw_dataMat['Fare'].min()
    fare_max = raw_dataMat['Fare'].max()
    for i in range(m):
        if raw_dataMat['Pclass'][i] == 1:
            dataMat[i, 0] = 1
        if raw_dataMat['Pclass'][i] == 2:
            dataMat[i, 1] = 1
        if raw_dataMat['Pclass'][i] == 3:
            dataMat[i, 2] = 1
        if raw_dataMat['Sex'][i] == 'female':
            dataMat[i, 3] = 1
    #  process   age
        dataMat[i, 4] = (raw_dataMat['Age'][i] - age_min) / (age_max - age_min)

        dataMat[i, 5] = (raw_dataMat['SibSp'][i] - sibsp_min) / (sibsp_max - sibsp_min)
        dataMat[i, 6] = (raw_dataMat['Parch'][i] - parch_min) / (parch_max - parch_min)
        dataMat[i, 7] = (raw_dataMat['Fare'][i] - fare_min) / (fare_max - fare_min)

        if raw_dataMat['Embarked'][i] == 'C':
            dataMat[i, 8] = 1
        if raw_dataMat['Embarked'][i] == 'Q':
            dataMat[i, 9] = 1
        if raw_dataMat['Embarked'][i] == 'S':
            dataMat[i, 10] = 1

    # df = pd.DataFrame(dataMat)
    return dataMat, label

def preprocess_training_set():
    raw_datamat = load_dataset('data/train.csv')
    training_datamat = preprocess_data(raw_datamat[:700])
    return training_datamat

def logisticRegression(dataMat, label):
    return lrcv()