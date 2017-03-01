import json
import ast
import re

class Tweet(object):
	def __init__(self,text,time,geo):
		self.text=text
		self.time=time
		self.geo=geo

def load_dirty_json(dirty_json):
	regex_replace = [(r"([ \{,:\[])(u)?'([^']+)'", r'\1"\3"'), (r" False([, \}\]])", r' false\1'), (r" True([, \}\]])", r' true\1')]
	for r, s in regex_replace:
 		dirty_json = re.sub(r, s, dirty_json)
	clean_json = json.loads(dirty_json)
 	return clean_json

def keyword(dataset, words):
	tweets=[]
	for line in open(dataset,'r'):
		try:
			tweetdict=ast.literal_eval(line)
			tweets.append(tweetdict)
		except SyntaxError:
			print 'ERROR: tweet could not be loaded'
	for tweet in tweets:
		for w in words:
			if w in tweet['text']:
				print tweet['text'].encode("ascii","ignore")
				break

if __name__=="__main__":
	words=['flood','wind','power']
	keyword("irene_hurricane.txt",words)

