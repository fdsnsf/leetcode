#coding=utf-8
from random import randint, choice
from string import lowercase
from sys import maxint
from time import ctime

import re

doms  = ('com', 'edu', 'net', 'org', 'gov')

result = []

for i in range(randint(5, 10)):
	dtint = randint(0, 456456465) #maxint-1
	dtstr = ctime(dtint)
	shorter = randint(4, 7)
	em = ''
	for j in range(shorter):
		em += choice(lowercase)

	longer = randint(shorter, 12)
	dn = ''
	for j in range(longer):
		dn += choice(lowercase)

	r = '%s::%s@%s.%s::%d-%d-%d' % (dtstr, em, dn, choice(doms), dtint, shorter, longer)
	result.append(r)

#Thu Jan 27 20:35:38 1983::sqtjr@pcfmat.net::412518938-5-6
for i in result:
	#print re.search(r'::(\d+)', i).group(1)
	#print re.search(r'\w+@\w+.\w{3}', i).group()
	#print re.search(r'\b\d{4}', i).group()
	#result = re.search(r'::(\w+)@(\w+.\w{3})', i)
	#print result.group(1), result.group(2)
	#result = re.search(r'::(\w+)@(\w+).(\w{3})', i)
	#print result.group(1), result.group(2), result.group(3)
	#print re.search(r'\b\d+(:\d+){2}\b', i).group()
	print re.sub(r'\w+@\w+.\w{3}','sun_fan0825@sina.com', i)
