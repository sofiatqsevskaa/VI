import math
import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'
from submission_script import *
from dataset_script import dataset
from sklearn.naive_bayes import GaussianNB

# Ova e primerok od podatochnoto mnozestvo, za treniranje/evaluacija koristete ja
# importiranata promenliva dataset
dataset_sample = [['1', '35', '12', '5', '1', '100', '0'],
                  ['1', '29', '7', '5', '1', '96', '1'],
                  ['1', '50', '8', '1', '3', '132', '0'],
                  ['1', '32', '11.75', '7', '3', '750', '0'],
                  ['1', '67', '9.25', '1', '1', '42', '0']]

if __name__ == '__main__':
    dataset = [[int(num) if num.isdigit() else float(num) for num in row] for row in dataset]

    train_set = dataset[:int(0.85 * len(dataset))]
    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]

    test_set = dataset[int(0.85 * len(dataset)):]
    testX = [row[:-1] for row in test_set]
    testY = [row[-1] for row in test_set]

    classifier = GaussianNB()
    classifier.fit(train_x, train_y)
    ct = 0
    for i in range(len(test_set)):
        pred = classifier.predict([testX[i]])[0]
        if pred == testY[i]:
            ct += 1
    test = [int(num) if num.isdigit() else float(num) for num in input().split(' ')]

    print(ct / len(test_set))
    print(classifier.predict([test])[0])
    print(classifier.predict_proba([test]))
    submit_train_data(train_x, train_y)
    submit_test_data(test_x, test_y)
    submit_classifier(classifier)
    # povtoren import na kraj / ne ja otstranuvajte ovaa linija
    # from submission_script import *
