#Load libraries
from joblib import dump, load

# Load model
clf = load('model.joblib') 

def test_predict_setosa_0():
    # Given.
    X = [[5.1, 3.5, 1.4, 0.2]]
    # When.
    predict_setosa_0 = clf.predict(X)
    # Then.
    assert predict_setosa_0 == [[0]]