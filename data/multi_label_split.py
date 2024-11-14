import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer
from skmultilearn.model_selection import iterative_train_test_split
from scipy.sparse import lil_matrix

def stratified_multi_label_split(df: pd.DataFrame, label_col: str, test_size: float = 0.2) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Performs a stratified train-test split for multi-label data while preserving label distributions.
    
    Args:
        df (pandas.DataFrame): Input dataframe containing the data
        label_col (str): Name of the column containing multi-label data (list of labels)
        test_size (float): Proportion of data to include in test split (default: 0.2)
        
    Returns:
        tuple: (df_train, df_test) containing the train and test splits as DataFrames
    """
    mlb = MultiLabelBinarizer()
    Y = mlb.fit_transform(df[label_col])
    Y = lil_matrix(Y)
    X = [[x] for x in df.index.tolist()]
    X = lil_matrix(X)
    
    
    X_train, _, X_test, _ = iterative_train_test_split(X, Y, test_size=test_size)
    train_idx = [x for sublist in X_train.toarray().tolist() for x in sublist]
    test_idx = [x for sublist in X_test.toarray().tolist() for x in sublist]

    df_train = df.loc[train_idx]
    df_test = df.loc[test_idx]

    return df_train, df_test