import urllib2
import json
import datetime
cur_date = datetime.datetime.now()
list = []
for j in range (10):
	stoixeio = input('dwse aritmo:')
	list.append(stoixeio)
def check(x,y):
	s=0
	for i in x:
		if i in y:
			s+=1
	return s
list_epituxia = []
hmeres = []
today = datetime.datetime.today().day
for i in range (int(today)):
	cur_date= cur_date - datetime.timedelta(days=1)
	date_str= cur_date.strftime("%d-%m-%Y")
	hmeres.append(date_str)
	url='http://applications.opap.gr/DrawsRestServices/kino/drawDate/%s.json'%date_str
	req= urllib2.Request(url)
	response= urllib2.urlopen(req)
	data=response.read()
	data=json.loads(data)
	klhrwseis=data['draws'] ['draw']
	r=[]
	for k in klhrwseis:
		tmp=k['results']
		r.append(check(list,tmp))
	m = 0
	for i in range (180):
		if r[i] > 4:
			m += 1
	list_epituxia.append(m)
	print ('apotelesmata',date_str)
	print (r[:])
	print ('\n')
max_list = max(list_epituxia)
b = list_epituxia.index(max(list_epituxia))
print ('oi perissoteres epituxies sas einai',max_list,'thn hmera',hmeres[b])