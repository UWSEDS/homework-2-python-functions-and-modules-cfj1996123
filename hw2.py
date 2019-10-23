import pandas as pd

def reads(url):
    df = pd.read_csv(url)
    return df

def test_create_dataframe(df, colnames):
    '''
    :param df:        pandas data frame
    :param colnames:  list[str]
    :return:          bool
    '''
    # test whether all columns are specified in colnames
    colnames_set = set(colnames)
    for col in df.columns:
        if col not in colnames_set:
            return False
    # test whether all elements in the same column have the same type
    for col in df.columns:
        for i in range(len(df[col])):
            elem = df[col][i]
            if type(elem) != type(df[col][0]):
                return False

    # test whether there is at least 10 rows
    if df.shape[0] < 10:
        return False

    return True


if __name__ == '__main__':
    url = "https://data.seattle.gov/api/views/tw7j-dfaw/rows.csv?accessType=DOWNLOAD"
    df = reads(url)
    res = test_create_dataframe(df, list(df.columns))
    print(res)

    d = {'col1': [1, 2], 'col2': [3, '3']}
    df = pd.DataFrame(data=d)
    print(test_create_dataframe(df, list(df.columns)))

