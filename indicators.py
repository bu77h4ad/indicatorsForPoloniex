def Highest(nPriod, chart, iBar=-1):	
	"""
	Return (float) the maximum for nPriod period
	"""
	Highest= float(chart[iBar]['high'])
	for j in range(1,nPriod +1 ):         
		if Highest < float(chart[iBar-j ]['high']) :  Highest = float(chart[iBar-j]['high'])  
	return(Highest)


def Lowest(nPriod, chart, iBar=-1):
	"""
	Return (float) the minimum for nPriod period
	"""
	Lowest= float(chart[iBar]['low'])
	for j in range(1,nPriod +1 ):         
		if Lowest > float(chart[iBar-j]['low']) :  Lowest = float(chart[iBar-j]['low'])
	return(Lowest)


def SMA(nPriod, chart, iBar=-1):
	"""
	Return (float) simple moving average SMA = SUM(Close, N)/N,
	"""
	SMA = 0.0   
	for j in range(nPriod):
		SMA = SMA + float(chart[iBar-j]['close'] )    
	SMA=SMA/nPriod  
	return (SMA)


def PiceChannel( nPriod, chart, iBar=-1):
	"""
	Return (dict) Price Channel

	highPrice = Highest(nPriod, chart, iBar)
	lowPrice = Lowest(nPriod, chart, iBar)
	centerLine = (highPrice +  lowPrice) / 2
	"""  
	highPrice = Highest(nPriod, chart, iBar)
	lowPrice = Lowest(nPriod, chart, iBar)
	centerLine = (highPrice +  lowPrice) / 2
	  
	PriceChannel = {
		'highPrice'	: 	highPrice,
		'centerLine': 	centerLine,
		'lowPrice'	:	lowPrice
	}  
	return (PriceChannel)


def RSI(nPeriod, chart, iBar=-1):
	"""
	RSI (Relative Strength Index) или индекс относительной силы
	RSI = 100 - (100 / (1 + U / D))
	RS = nPeriod( bulls bar / bears bar)
	"""
	bull = 0
	bear = 0

	for i in range(nPeriod):
		#Если бычья свечка
		if chart[iBar - i]['close'] > chart[iBar - i - 1]['close'] : 
			bull +=  chart[iBar - i]['close']  - chart[iBar - i -1]['close'] 
		#Если медвежья свечка
		if chart[iBar - i]['close'] < chart[iBar - i - 1]['close'] :
			bear += chart[iBar - i -1]['close'] - chart[iBar - i]['close'] 
	if bear==0:
		RSI = 100
	else:
		RS= bull / bear
		RSI = 100 - (100 / (1 + RS))
	return RSI
