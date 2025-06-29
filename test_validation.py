import pandas as pd

def test_data_shape():
    df = pd.read_csv("data/iris.csv")
    assert df.shape[1] == 5

def test_no_nulls():
    df = pd.read_csv("data/iris.csv")
    assert df.isnull().sum().sum() == 0
