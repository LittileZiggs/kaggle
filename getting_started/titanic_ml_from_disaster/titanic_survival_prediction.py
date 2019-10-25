import pandas as pd
from sklearn.linear_model import LogisticRegressionCV
from sklearn import tree
from numpy import *

def load_dataset(file_name):
    raw_data_mat = pd.read_csv(file_name)
    return raw_data_mat

def get_label_and_data_mat(raw_data_mat):
    label = mat(raw_data_mat['Survived']).T
    data_mat = preprocess_data(raw_data_mat)
    return data_mat, label

def preprocess_data(raw_data_mat):
    m, n = shape(raw_data_mat)
    data_mat = zeros((m,11))

    age_mean = raw_data_mat['Age'].mean()
    raw_data_mat['Age'].fillna(age_mean, inplace=True)
    fare_mean = raw_data_mat['Fare'].mean()
    raw_data_mat['Fare'].fillna(fare_mean, inplace=True)

    age_min = raw_data_mat['Age'].min()
    age_max = raw_data_mat['Age'].max()
    sibsp_min = raw_data_mat['SibSp'].min()
    sibsp_max = raw_data_mat['SibSp'].max()
    parch_min = raw_data_mat['Parch'].min()
    parch_max = raw_data_mat['Parch'].max()
    fare_min = raw_data_mat['Fare'].min()
    fare_max = raw_data_mat['Fare'].max()
    for i in range(m):
        if raw_data_mat['Pclass'][i] == 1:
            raw_data_mat[i, 0] = 1
        if raw_data_mat['Pclass'][i] == 2:
            raw_data_mat[i, 1] = 1
        if raw_data_mat['Pclass'][i] == 3:
            raw_data_mat[i, 2] = 1
        if raw_data_mat['Sex'][i] == 'female':
            data_mat[i, 3] = 1
    #  process   age
        data_mat[i, 4] = (raw_data_mat['Age'][i] - age_min) / (age_max - age_min)

        data_mat[i, 5] = (raw_data_mat['SibSp'][i] - sibsp_min) / (sibsp_max - sibsp_min)
        data_mat[i, 6] = (raw_data_mat['Parch'][i] - parch_min) / (parch_max - parch_min)
        data_mat[i, 7] = (raw_data_mat['Fare'][i] - fare_min) / (fare_max - fare_min)

        if raw_data_mat['Embarked'][i] == 'C':
            data_mat[i, 8] = 1
        if raw_data_mat['Embarked'][i] == 'Q':
            data_mat[i, 9] = 1
        if raw_data_mat['Embarked'][i] == 'S':
            data_mat[i, 10] = 1

    # df = pd.DataFrame(dataMat)
    return data_mat

# def preprocess_training_set():
#     raw_data_mat = load_dataset('data/train.csv')
#     training_data_mat = preprocess_data(raw_data_mat[:700])
#     return training_data_mat

# def logistic_regression(data_mat, label):
#     return lrcv(cv = 5, random_state = 0).fit(data_mat, label)

def predictTestSetByLogisticRegression(data_mat, label):
    clf = LogisticRegressionCV(cv = 5).fit(data_mat, label)
    raw_test_mat = pd.read_csv('data/test.csv')
    test_mat = preprocess_data(raw_test_mat)
    return clf.predict(test_mat)

def predictTestSetByDecisionTree(data_mat, label):
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(data_mat, label)
    raw_test_mat = pd.read_csv('data/test.csv')
    test_mat = preprocess_data(raw_test_mat)
    return clf.predict(test_mat)

if __name__ == '__main__':
    data_mat, label = get_label_and_data_mat(load_dataset('data/train.csv'))
    test_label = predictTestSetByDecisionTree(data_mat, label)
    result = pd.DataFrame(columns = ['PassengerId', 'Survived'])
    result['PassengerId'] = load_dataset('data/test.csv')['PassengerId']
    result['Survived'] = test_label
    result.to_csv('data/submission_decision_tree.csv', index = False, encoding = 'utf-8')
    # count = 0
    # for i in range(shape(test_label)[0]):
    #     if test_label[i] != result['Survived'][i]:
    #         count = count + 1
    #
    # num = 0
    # gender_result = load_dataset('data/gender_submission.csv')
    # for j in range(shape(test_label)[0]):
    #     if test_label[j] != gender_result['Survived'][j]:
    #         num = num + 1