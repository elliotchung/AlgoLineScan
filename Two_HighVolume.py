import One_OHLC_data

data = One_OHLC_data.ohlc_data
VolumeDict = {index: volume['volume'] for index, volume in enumerate(data['day'])}
MovingAvg = 50
VolumeList = list(VolumeDict.values())
fiftyDayAvgdict = {}
HighVolumeIndex = []

for i in range(0, len(VolumeList) - MovingAvg+1):
    window = VolumeList[i:i+MovingAvg]
    fiftyDayAvg = sum(window)/MovingAvg
    fiftyDayAvgdict[i+MovingAvg-1] = fiftyDayAvg

for i in range(MovingAvg-1, len(VolumeList)):
    if VolumeDict[i] > fiftyDayAvgdict[i]:
        HighVolumeIndex.append(i)
print(HighVolumeIndex)
