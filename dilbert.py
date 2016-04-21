from bs4 import BeautifulSoup
import datetime
import requests
import sys
import os
from redis import Redis
from rq import Queue
from worker import download_image

base = datetime.datetime(2013, 10, 8, 0, 0)
#end = datetime.datetime(1993, 1, 1, 0, 0)
end = datetime.datetime.today()

date_list = [base + datetime.timedelta(days=x) for x in range(0, (end - base).days)]

redis_conn = Redis()
q = Queue(connection=redis_conn)  # no args implies the default queue

for date in date_list:
	date_string = str(date.strftime('%Y-%m-%d'))
	year = str(date.strftime('%Y'))
	month = str(date.strftime('%m'))

	path = str(year) + '/' + str(month).zfill(2)
	if not os.path.isdir(path):
		os.makedirs(str(year) + '/' + str(month).zfill(2))
	response = requests.get('http://dilbert.com/strip/' + date_string)
	soup = BeautifulSoup(response.text, 'html.parser')

	body = soup.find("img", class_="img-comic")['src']
	job = q.enqueue(download_image, year + '/' + month + '/' + date_string + '.gif', body)

	print 'gotten ' + date_string

