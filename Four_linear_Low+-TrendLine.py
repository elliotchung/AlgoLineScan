import One_OHLC_data
import Three_LongWicks
import math

data = One_OHLC_data.ohlc_data
StartingCandleIndex = Three_LongWicks.HighVolumeWithWicksIndex
ConnectingCandleIndex = Three_LongWicks.LongWickIndex
startingIndex = Three_LongWicks.startingIndex

def create_line_dict(x1, y1, x2, y2, limit):
    slope = (y2 - y1) / (x2 - x1)
    x_values = list(range(x1, limit))
    #print(x_values)
    y_values = [y1 + slope * (x - x1) for x in x_values]
    #log_y_values = [math.log(y, 10) for y in y_values]  # calculate logarithmic y-values

    result = {}
    #print('hi',x_values)
    for i in range(len(x_values)):
        x = x_values[i]
        #y = log_y_values[i]  # use logarithmic y-value
        y = y_values[i] # use linear y-value
        result[x] = y
    return result
    

#create_line_dict(StartingCandleIndex[0], data['day'][StartingCandleIndex[0]]['low'], 
#ConnectingCandleIndex[20], data['day'][ConnectingCandleIndex[20]]['low'], len(data['day']))

#create a dicitonary of indexes that starting candle can connect to
PossibleConnectionsDict = {}
for i in range(0, len(StartingCandleIndex)):
    PossibleConnectionsDict[StartingCandleIndex[i]] = {}
    for j in range(0, len(ConnectingCandleIndex)):
        if ConnectingCandleIndex[j] > StartingCandleIndex[i]:
            PossibleConnectionsDict[StartingCandleIndex[i]][ConnectingCandleIndex[j]] = {}

#inner most index: all xy values for the line
#middle index: all possible connecting candles
#outer most index: all starting candles

for i in range(0, len(StartingCandleIndex)):
    PossibleConnectingCandles = list(PossibleConnectionsDict[StartingCandleIndex[i]].keys())
    for j in range(0, len(PossibleConnectingCandles)):
        LineDict = create_line_dict(StartingCandleIndex[i], data['day'][StartingCandleIndex[i]]['low'], 
        PossibleConnectingCandles[j], data['day'][PossibleConnectingCandles[j]]['low'], len(data['day']))
        PossibleConnectionsDict[StartingCandleIndex[i]][PossibleConnectingCandles[j]].update(LineDict)

#remove dictionaries containing negative y values
for i in range(0, len(StartingCandleIndex)):
    keys_to_remove = []
    for key, inner_dict in PossibleConnectionsDict[StartingCandleIndex[i]].items():
        if any(value < 0 for value in inner_dict.values()):
            keys_to_remove.append(key)

    for key in keys_to_remove:
        del PossibleConnectionsDict[StartingCandleIndex[i]][key]

#remove dictionaries where trendline has been breached
for i in range(0, len(StartingCandleIndex)):
    keys_list = list(PossibleConnectionsDict[StartingCandleIndex[i]].keys())
    for j in range(0, len(keys_list)):
        inner_keys_list = list(PossibleConnectionsDict[StartingCandleIndex[i]][keys_list[j]].keys())
        for k in range(0, len(inner_keys_list)):
            if data['day'][inner_keys_list[k]]['close'] < PossibleConnectionsDict[StartingCandleIndex[i]][keys_list[j]][inner_keys_list[k]]:
                del PossibleConnectionsDict[StartingCandleIndex[i]][keys_list[j]]
                break

#filter to only include trendlines that are near to the latest candle
latest_candle_price = data['day'][len(data['day'])-1]['close']
upper_limit = latest_candle_price + (latest_candle_price * 0.05)
lower_limit = latest_candle_price - (latest_candle_price * 0.05)
for i in range(0, len(StartingCandleIndex)):
    keys_list = list(PossibleConnectionsDict[StartingCandleIndex[i]].keys())
    for j in range(0, len(keys_list)):
        if PossibleConnectionsDict[StartingCandleIndex[i]][keys_list[j]][len(data['day'])-1] > upper_limit or PossibleConnectionsDict[StartingCandleIndex[i]][keys_list[j]][len(data['day'])-1] < lower_limit:
            del PossibleConnectionsDict[StartingCandleIndex[i]][keys_list[j]]


#list out the dates
for i in range(0, len(StartingCandleIndex)):
    keys_list = list(PossibleConnectionsDict[StartingCandleIndex[i]].keys())
    for j in range(0, len(keys_list)):
        print(StartingCandleIndex[i],data['day'][StartingCandleIndex[i]]['date'], 
        keys_list[j],data['day'][keys_list[j]]['date'],PossibleConnectionsDict[StartingCandleIndex[i]][keys_list[j]][len(data['day'])-1])
print(latest_candle_price)