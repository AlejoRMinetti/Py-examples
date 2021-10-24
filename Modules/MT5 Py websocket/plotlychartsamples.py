# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 16:13:03 2019

@author: dmitrievsky
"""
from MetaTrader5 import *
from datetime import datetime

# Initializing MT5 connection 
MT5Initialize()
MT5WaitForTerminal()

print(MT5TerminalInfo())
print(MT5Version())

# Copying data to list
rates = MT5CopyTicksFrom("EURUSD", datetime(2019,3,14,13), 1000, MT5_COPY_TICKS_ALL)
bid = [x.bid for x in rates]
ask = [x.ask for x in rates]
time = [x.time for x in rates]

# Deinitializing MT5 connection
MT5Shutdown()

import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
data = [go.Scatter(x=time, y=bid), go.Scatter(x=time, y=ask)]

plot(data)
