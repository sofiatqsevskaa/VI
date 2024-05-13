import os
from submission_script import *
from dataset_script import dataset
from sklearn.preprocessing import OrdinalEncoder
from sklearn.tree import DecisionTreeClassifier

os.environ['OPENBLAS_NUM_THREADS'] = '1'

data = [['C', 'S', 'O', '1', '2', '1', '1', '2', '1', '2', '0'],
        ['D', 'S', 'O', '1', '3', '1', '1', '2', '1', '2', '0'],
        ['C', 'S', 'O', '1', '3', '1', '1', '2', '1', '1', '0'],
        ['D', 'S', 'O', '1', '3', '1', '1', '2', '1', '2', '0'],
        ['D', 'A', 'O', '1', '3', '1', '1', '2', '1', '2', '0']]

if __name__ == '__main__':
    a = int(input())
    crit = input()
    value = 1 - float(a / 100)

    enc = OrdinalEncoder()
    enc.fit([r[:-1] for r in dataset])
    clf = DecisionTreeClassifier(criterion=crit, random_state=0)

    train = [r for r in dataset[int(value * len(dataset)):]]
    train_X = [r[:-1] for r in train]
    train_Y = [r[-1] for r in train]
    train_X = enc.transform(train_X)

    test = [r for r in dataset[:int(value* len(dataset))]]
    test_X = [r[:-1] for r in test]
    test_Y = [r[-1] for r in test]
    test_X = enc.transform(test_X)

    clf.fit(train_X, train_Y)

    acc = 0
    for pred, true_val in zip(test_X, test_Y):
        pred_cls = clf.predict([pred])[0]
        if pred_cls == true_val:
            acc += 1
            
    acc = float(acc / len(test))
    f_imp = list(clf.feature_importances_)

    print("Depth: " + str(clf.get_depth()))
    print("Number of leaves: " + str(clf.get_n_leaves()))
    print("Accuracy: " + str(acc))
    print("Most important feature: " + str(f_imp.index(max(f_imp))))
    print("Least important feature: " + str(f_imp.index(min(f_imp))))

    submit_train_data(train_X, train_Y)
    submit_test_data(test_X, test_Y)
    submit_classifier(clf)
    submit_encoder(enc)
