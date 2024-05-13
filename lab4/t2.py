import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'
# from submission_script import *
# from dataset_script import dataset
from test_dataset import dataset
from sklearn.ensemble import RandomForestClassifier

# Ova e primerok od podatochnoto mnozestvo, za treniranje/evaluacija koristete ja
# importiranata promenliva dataset
dataset_sample = [[180.0, 23.6, 25.2, 27.9, 25.4, 14.0, 'Roach'],
                  [12.2, 11.5, 12.2, 13.4, 15.6, 10.4, 'Smelt'],
                  [135.0, 20.0, 22.0, 23.5, 25.0, 15.0, 'Perch'],
                  [1600.0, 56.0, 60.0, 64.0, 15.0, 9.6, 'Pike'],
                  [120.0, 20.0, 22.0, 23.5, 26.0, 14.5, 'Perch']]

if __name__ == '__main__':
    col_index = int(input())
    num_trees = int(input())
    criterion = input()

    train_set = [row[:col_index] + row[col_index + 1:] for row in dataset[:int(0.85 * len(dataset))]]
    test_set = [row[:col_index] + row[col_index + 1:] for row in dataset[int(0.85 * len(dataset)):]]

    train_X = [row[:-1] for row in train_set]
    train_Y = [row[-1] for row in train_set]

    test_X = [row[:-1] for row in test_set]
    test_Y = [row[-1] for row in test_set]

    classifier = RandomForestClassifier(criterion=criterion, n_estimators=num_trees, random_state=0)
    classifier.fit(train_X, train_Y)

    ct = 0
    for i in range(0, len(test_set)):
        pred = classifier.predict([test_X[i]])[0]
        if pred == test_Y[i]:
            ct += 1

    accuracy = float(ct) / len(test_set)

    new_input = list(int(num) for num in input().split())
    del new_input[col_index]

    print("Accuracy: " + str(accuracy))
    print(classifier.predict([new_input])[0])
    print(classifier.predict_proba([new_input])[0])

    # submit_train_data(train_X, train_Y)
    # submit_test_data(test_X, test_Y)
    # submit_classifier(classifier)
