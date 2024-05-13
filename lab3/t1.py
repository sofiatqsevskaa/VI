import os
import math
os.environ['OPENBLAS_NUM_THREADS'] = '1'
from submission_script import *
from dataset_script import dataset
from sklearn.preprocessing import OrdinalEncoder
from sklearn.naive_bayes import CategoricalNB

# Ova e primerok od podatochnoto mnozestvo, za treniranje/evaluacija koristete ja
# importiranata promenliva dataset
dataset_sample = [['C', 'S', 'O', '1', '2', '1', '1', '2', '1', '2', '0'],
                  ['D', 'S', 'O', '1', '3', '1', '1', '2', '1', '2', '0'],
                  ['C', 'S', 'O', '1', '3', '1', '1', '2', '1', '1', '0'],
                  ['D', 'S', 'O', '1', '3', '1', '1', '2', '1', '2', '0'],
                  ['D', 'A', 'O', '1', '3', '1', '1', '2', '1', '2', '0']]

if __name__ == '__main__':
    encoder = OrdinalEncoder()
    encoder.fit([row[:-1] for row in dataset])
    train_set = dataset[:int(0.75 * len(dataset))]
    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]

    train_x = encoder.transform(train_x)

    test_set = dataset[int(0.75 * len(dataset)):]
    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]

    test_x = encoder.transform(test_x)

    classifier = CategoricalNB()
    classifier.fit(train_x, train_y)
    ct = 0

    for i in range(0, len(test_set)):
        predicted_classes = classifier.predict([test_set[i]])[0]
        true_class = test_y[i]
        if predicted_classes == true_class:
            ct += 1

    entry = [a for a in input().split(' ')]
    entry = encoder.transform([entry])
    print(ct/len(test_x))
    print(classifier.predict(entry)[0])
    print(classifier.predict_proba(entry))
    submit_test_data(test_x, test_y)
    submit_train_data(train_x, train_y)
    submit_classifier(classifier)
    submit_encoder(encoder)

