import pandas as pd

def replace_value(dataframe, column, old_value, new_value):
    """
    Replaces a value in a column with a new value in a pandas DataFrame.
    Returns a pandas DataFrame.

    Parameters:
    ----------
    dataframe : pandas.DataFrame
    column : str
    old_value : str, int, or float
    new_value : str, int, or float

    Returns:
    -------
    pandas.DataFrame
        A DataFrame with a new specified value, that replaced the old specified value,
        in the specified column

    Examples:
    --------
    >>> import pandas as pd
    >>> df = pd.read_csv('filename.csv') # Replace 'filename.csv' with your desired dataset filename
    >>> result = replace_value(df, column_name, "old value", "new value")
    >>> print(result)

    """
    new_dataframe = (dataframe.loc[dataframe[column] == old_value, column] = new_value)
    return new_dataframe