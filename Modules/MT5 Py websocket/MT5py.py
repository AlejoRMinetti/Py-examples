from datetime import datetime
from MetaTrader5 import * 
from pytz import timezone 
import matplotlib.pyplot as plt 
utc_tz = timezone('UTC') 


# connect to MetaTrader 5
MT5Initialize()
# wait till MetaTrader 5 establishes connection to the trade server and synchronizes the environment
MT5WaitForTerminal()

# request connection status and parameters
print(MT5TerminalInfo())
# get data on MetaTrader 5 version
print(MT5Version())

# request 1000 ticks from EURAUD 
euraud_ticks = MT5CopyTicksFrom("EURAUD", datetime(2019,4,1,0), 1000, MT5_COPY_TICKS_ALL)
# request ticks from AUDUSD within 2019.04.01 13:00 - 2019.04.02 13:00 
audusd_ticks = MT5CopyTicksRange("AUDUSD", datetime(2019,4,1,13), datetime(2019,4,2,13), MT5_COPY_TICKS_ALL)

# get bars from different symbols in a number of ways
eurusd_rates = MT5CopyRatesFrom("EURUSD", MT5_TIMEFRAME_M1, datetime(2019,4,5,15), 1000)
eurrub_rates = MT5CopyRatesFromPos("EURRUB", MT5_TIMEFRAME_M1, 0, 1000)
eurjpy_rates = MT5CopyRatesRange("EURJPY", MT5_TIMEFRAME_M1, datetime(2019,4,1,13), datetime(2019,4,2,13))
# shut down connection to MetaTrader 5
MT5Shutdown()

#DATA
print('euraud_ticks(', len(euraud_ticks), ')')
for val in euraud_ticks[:10]: print(val)
print('audusd_ticks(', len(audusd_ticks), ')')
for val in audusd_ticks[:10]: print(val)
print('eurusd_rates(', len(eurusd_rates), ')')
for val in eurusd_rates[:10]: print(val)
print('eurrub_rates(', len(eurrub_rates), ')')
for val in eurrub_rates[:10]: print(val)
print('eurjpy_rates(', len(eurjpy_rates), ')')
for val in eurjpy_rates[:10]: print(val)

#PLOTTING
x_time = [x.time.astimezone(utc_tz) for x in euraud_ticks]
# prepare Bid and Ask arrays
bid = [y.bid for y in euraud_ticks]
ask = [y.ask for y in euraud_ticks]

# draw ticks on the chart
plt.plot(x_time, ask,'r-', label='ask')
plt.plot(x_time, bid,'g-', label='bid')
# display legends 
plt.legend(loc='upper left')
# display header 
plt.title('EURAUD ticks')
# display the chart
plt.show()