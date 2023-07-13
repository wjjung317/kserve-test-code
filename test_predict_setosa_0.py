#Load libraries
from joblib import dump, load

# Load model
# It is a model that predicts the species of an iris flower given measurements about the length and width of its petals and stem
# The order of values in the X object are stem length, stem width, petal length, petal width in centimeters
# The mapping of numbers to species type in the prediction are the following: 0=Setosa, 1=Versicolur, 2=Virginica 
clf = load('model.joblib') 

# Test for 'computational integrity'
# Based on the model we built, we know that supplying values of [stem length, stem width, petal length, petal width] of [5.1, 3.5, 1.4, 0.2] respectively should result in the model predicting the 'setosa' species (coded as '0' in the model)
# We test for the above in the code below
def test_predict_setosa_0():
    # Given.
    X = [[5.1, 3.5, 1.4, 0.2]] # order of values: stem length, stem width, petal length, petal width 
    # When.
    predict_setosa_0 = clf.predict(X)
    # Then.
    assert predict_setosa_0 == [[0]] # '0' here maps to the 'setosa' species
