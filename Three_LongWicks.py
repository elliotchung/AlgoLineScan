import One_OHLC_data
import Two_HighVolume

data = One_OHLC_data.ohlc_data
startingIndex = Two_HighVolume.MovingAvg-1
LongWickIndex = []
HighVolumeWithWicksIndex = []

for i in range(startingIndex, len(data['day'])):
    CandleLength = data['day'][i]['high'] - data['day'][i]['low']
    #Green Candle
    if data['day'][i]['close'] > data['day'][i]['open']:
        WickLength = data['day'][i]['open'] - data['day'][i]['low']
    #Red Candle
    if data['day'][i]['close'] < data['day'][i]['open']:
        WickLength = data['day'][i]['close'] - data['day'][i]['low']
    #doji
    if data['day'][i]['close'] == data['day'][i]['open']:
        WickLength = data['day'][i]['close'] - data['day'][i]['low']
    WickRatio = WickLength/CandleLength
    if WickRatio > 0.1:
        LongWickIndex.append(i)

set1 = set(Two_HighVolume.HighVolumeIndex)
set2 = set(LongWickIndex)
HighVolumeWithWicksIndex = list(set1.intersection(set2))

