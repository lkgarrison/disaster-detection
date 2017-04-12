import filter
from datetime import datetime

def plot(data):
	tweets=filter.filter(data)
	counts_per_day=dict()
	for tweet in tweets:
		time_info=tweet.time.split()
		key=' '.join(time_info[1:4])
		time_hms=time_info[4].split(':')
		hour=int(time_hms[0])
		if hour<12:
			key+=" 00"
		else:
			key+=" 12"
		if key in counts_per_day:
			counts_per_day[key]+=1
		else:
			counts_per_day[key]=1
	dates=sorted(counts_per_day.keys(),key=getDateFromKey)
	for key in dates:
		print key, counts_per_day[key]

def getDateFromKey(key):
	#return datetime.strptime(key, "%d %b %Y %p")
	return datetime.strptime(key, "%d %b %Y %H")

if __name__=="__main__":
	plot("irene_hurricane.txt")
