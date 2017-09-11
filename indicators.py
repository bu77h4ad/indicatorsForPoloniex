def Highest(nPriod, Chart, iBar=-1):	
	"""
	Return (float) the maximum for nPriod period
	"""
	Highest= float(Chart[iBar]['high'])
	for j in range(1,nPriod +1 ):         
		if Highest < float(Chart[iBar-j ]['high']) :  Highest = float(Chart[iBar-j]['high'])  
	return(Highest)


def Lowest(nPriod, Chart, iBar=-1):
	"""
	Return (float) the minimum for nPriod period
	"""
	Lowest= float(Chart[iBar]['low'])
	for j in range(1,nPriod +1 ):         
		if Lowest > float(Chart[iBar-j]['low']) :  Lowest = float(Chart[iBar-j]['low'])
	return(Lowest)


def SMA(nPriod, Chart, iBar=-1):
	"""
	Return (float) simple moving average SMA = SUM(Close, N)/N,
	"""
	SMA = 0.0   
	for j in range(nPriod):
		SMA = SMA + float(Chart[iBar-j]['close'] )    
	SMA=SMA/nPriod  
	return (SMA)


def PiceChannel( nPriod, Chart, iBar=-1):
	"""
	Return (dict) Price Channel

	highPrice = Highest(nPriod, Chart, iBar)
	lowPrice = Lowest(nPriod, Chart, iBar)
	centerLine = (highPrice +  lowPrice) / 2
	"""  
	highPrice = Highest(nPriod, Chart, iBar)
	lowPrice = Lowest(nPriod, Chart, iBar)
	centerLine = (highPrice +  lowPrice) / 2
	  
	PriceChannel = {
		'highPrice'	: 	highPrice,
		'centerLine': 	centerLine,
		'lowPrice'	:	lowPrice
	}  
	return (PriceChannel)
