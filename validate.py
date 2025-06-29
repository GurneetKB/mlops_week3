import pandas as pd

def validate():
    df = pd.read_csv("data/iris.csv")
    assert df.shape[1] == 5, "Dataset should have 5 columns"
    assert df.isnull().sum().sum() == 0, "Dataset should not have nulls"

if __name__ == "__main__":
    validate()
