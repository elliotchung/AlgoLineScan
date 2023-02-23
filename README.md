# AlgoLineScan
Uses Tradier API's historical data to find trendlines
## Steps
1. Download all files into the same folder
2. Input your access token from tradier in One_OHLC_data.py
3. Choose your start_date and end_date
4. run Four_linear_Low+-TrendLine.py
5. Draw the trendlines using your favourite charting software
### What this code is doing:
1. One_OHLC_data.py gets the historical data from tradier into a JSON file
2. Two_HighVolume.py calculates the 50 day simple moving average of the volume each day. It then compares the 50 day average volume to the actual volume, and records it in a list if the actual volume is higher
3. Three_LongWicks.py finds the candles with long wicks, i.e. WickLength/CandleLength > 0.1. It then creates 2 lists, one to record the candles with long wicks and another to record the candles with high volume AND long wicks
4. Four_linear_Low+-TrendLine.py draws many trendlines. The trendlines start from a high volume long wick candle, and connect to any other long wick candle. It then filters out any trenlines which extend to a negative price region. It then filters out trendlines whereby the close price of any candle is below the trendline i.e. the trendline has been breached.  It then filters out any trendlines which are too far from the latest price. It then lists out the dates of the remaining trendlines.
### Problems
1. Not for Log Scale trendlines
2. Have not filtered out earnings dates
