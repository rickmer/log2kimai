#!/usr/bin/python 
"""
CommandLine Tool / Modul for Kimai 
"""
from urllib import urlencode
from urllib2 import Request, build_opener, HTTPCookieProcessor, HTTPHandler
import cookielib

class kimaiMessage(object):
	"""
	The Message Object
	"""
	def __init__(self, baseurl, user, passwd):
		"""
		message constructor
		"""
		self.baseurl = baseurl
		self.user = user
		self.passwd = passwd

		cookiejar = cookielib.CookieJar()
		opener = build_opener(HTTPCookieProcessor(cookiejar), HTTPHandler())
		url = ''.join([self.baseurl, '/index.php?a=checklogin'])
		postdata = urlencode({'name':self.user, 'password':self.passwd})
		request = Request(url, postdata)	      
		opener.open(request)
		self.session = opener

	def __del__(self):
		"""
		deconstruct Message
		"""
		url = ''.join([self.baseurl, '/index.php?a=logout'])	      
		self.session.open(Request(url))

	def logWork(self):
		"""
		submit time
		"""
		url = ''.join([self.baseurl,'/extensions/ki_timesheets/processor.php'])
		postdata = urlencode({  'id':'',
								'axAction':'add_edit_timeSheetEntry',
								'projectID':1,
								'filter':'',
								'activityID':1,
								'description':'',
								'start_day':'27.11.2014',
								'end_day':'27.11.2014',
								'start_time':'15:45:00',
								'end_time':'17:45:00',
								'duration':'02:00:00',
								'location':'',
								'trackingNumber':'',
								'comment':'',
								'commentType':0,
								'userID[]':'936661847',
								'budget':'',
								'approved':'',
								'statusID':1,
								'billable':0,
								'rate':'',
								'fixedRate':''})
		request = Request(url, postdata)	      
		self.session.open(request)

def main():

	km = kimaiMessage('http://demo.kimai.org', 'admin', 'changeme')
	km.logWork()


if __name__ == "__main__":
	main()