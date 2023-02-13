#Load libraries
from joblib import dump, load

# Load model
clf = load('model.joblib') 

def test_predict_versicolor_1():
    # Given.
    X = [[5. , 2. , 3.5, 1. ]]
    # When.
    predict_versicolor_1 = clf.predict(X)
    # Then.
    assert predict_versicolor_1 == [[1]]