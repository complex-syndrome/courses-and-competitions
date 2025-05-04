import pandas as pd

from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import OrdinalEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_percentage_error

from xgboost import XGBRegressor


def categorical_columns(df: pd.DataFrame):
    categorical_cols = df.select_dtypes(include=['object', 'category'])
    # for col in categorical_cols:
    #     print(f"{col}: {df[col].unique()}")
    return categorical_cols.columns


def preprocess_data(data: pd.DataFrame, cols_to_encode: list):
    encoder = OrdinalEncoder()
    data_encoded = data.copy()
    data_encoded[cols_to_encode] = encoder.fit_transform(data[cols_to_encode])
    return data_encoded

def test_train(model, X, y):
    X_train, X_valid, y_train, y_valid = train_test_split(X, y, random_state=42, test_size=0.2)

    model.fit(X_train, y_train)
    print("Test Model fitted.")

    predictions = model.predict(X_valid)
    print("Test Model predicted.")

    mape = mean_absolute_percentage_error(y_valid, predictions)
    
    print(f"Test MAPE: {mape * 100:.2f}%\n")


def real_train(model, X, y, target):
    model.fit(X, y)
    print("Model fitted.")

    predictions = model.predict(target)
    print("Model predicted.")
    return predictions

    
def main():
    data = pd.read_csv("train.csv", index_col=0)
    TARGET = pd.read_csv("test.csv", index_col=0)
    data.dropna(axis=0, inplace=True)
    
    col_to_use = ["country", "store", "product"]
    
    print("CSV read.")
    
    X = data[col_to_use]
    y = data["num_sold"]

    to_encode = categorical_columns(X)
    labeled_X = preprocess_data(X, to_encode)
    labeled_target = preprocess_data(TARGET[col_to_use], to_encode)
    
    model = XGBRegressor(random_state=42)
    # model = RandomForestRegressor(random_state=42)
    # model = DecisionTreeRegressor(random_state=42)

    test_train(model, labeled_X, y)
    num_sold = real_train(model, labeled_X, y, labeled_target)
    
    # Check length
    # print(labeled_target.shape[0])
    # print(len(num_sold))
    
    df = pd.DataFrame(pd.DataFrame({
        "id": TARGET.index, 
        "num_sold": num_sold
    }))
    
    df.to_csv("submission.csv", index=False)
    print("Output created.\n")
    
    results = pd.read_csv("submission.csv")
    results.info()

if __name__ == "__main__":
    main()