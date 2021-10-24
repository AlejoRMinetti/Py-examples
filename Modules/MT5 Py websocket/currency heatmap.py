from MetaTrader5 import *
from datetime import date
import pandas as pd 
import matplotlib.pyplot as plt 

# Initializing MT5 connection 
MT5Initialize()
MT5WaitForTerminal()

print(MT5TerminalInfo())
print(MT5Version())

# Create currency watchlist for which correlation matrix is to be plotted
sym = ['EURUSD','GBPUSD','USDJPY','USDCHF','AUDUSD','GBPJPY']

# Copying data to dataframe
d = pd.DataFrame()
for i in sym:
     rates = MT5CopyRatesFromPos(i, MT5_TIMEFRAME_M1, 0, 1000)
     d[i] = [y.close for y in rates]

# Deinitializing MT5 connection
MT5Shutdown()

# Compute Percentage Change
rets = d.pct_change()

# Compute Correlation
corr = rets.corr()

# Plot correlation matrix
plt.figure(figsize=(10, 10))
plt.imshow(corr, cmap='RdYlGn', interpolation='none', aspect='auto')
plt.colorbar()
plt.xticks(range(len(corr)), corr.columns, rotation='vertical')
plt.yticks(range(len(corr)), corr.columns);
plt.suptitle('FOREX Correlations Heat Map', fontsize=15, fontweight='bold')
plt.show()

# Importing statmodels for cointegration test
import statsmodels
from statsmodels.tsa.stattools import coint

x = d['GBPUSD']
y = d['GBPJPY']
x = (x-min(x))/(max(x)-min(x))
y = (y-min(y))/(max(y)-min(y))

score = coint(x, y)
print('t-statistic: ', score[0], ' p-value: ', score[1])

# Plotting z-score transormation
diff_series = (x - y)
zscore = (diff_series - diff_series.mean()) / diff_series.std()

plt.plot(zscore)
plt.axhline(2.0, color='red', linestyle='--')
plt.axhline(-2.0, color='green', linestyle='--')

plt.show()