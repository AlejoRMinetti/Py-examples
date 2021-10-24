import os
import pandas as pd

# Write to CSV

df = pd.DataFrame({'name': ['Raphael', 'Donatello'],
                    'mask': ['red', 'purple'],
                    'weapon': ['sai', 'bo staff']})
df.to_csv(index=False)

# Read from csv

def symbol_to_path(symbol, base_dir="data"):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))

def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols:  # add SPY for reference, if absent
        symbols.insert(0, 'SPY')
    print(df)
    for symbol in symbols:
        # TODO: Read and join data for each symbol
        df_temp = pd.read_csv(symbol_to_path(symbol), index_col='Date',
                    parse_dates=True, usecols=['Date','Adj Close'], na_values=['nan'] )
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        print(df_temp)
        df = df.join(df_temp, how='inner') 
        print(df)
        if symbol == 'SPY': # drop
            df = df.dropna(subset=['SPY'])
    # no sale en orden cronologico :(
    return df