#!/usr/bin/python 
"""
CommandLine Tool / Modul for Kimai 
"""
from urllib import urlencode
from urllib2 import Request, build_opener, HTTPCookieProcessor, HTTPHandler
from cookielib import CookieJar
from argparse import ArgumentParser
from ConfigParser import ConfigParser, Error as ConfigParserError
from datetime import datetime, timedelta

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

        cookiejar = CookieJar()
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

    def logWork(self, start, end, pid, aid, userid='134117316', comment='', description=''):
        """
        log work
        """ 
        param_start_date = start.strftime('%d.%m.%Y')
        param_start_time = start.strftime('%H:%M:%S')
        param_end_date = end.strftime('%d.%m.%Y')
        param_end_time = end.strftime('%H:%M:%S')
        time_delta = end - start
        hours, remainder = divmod(time_delta.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        param_duration = ':'.join([str(hours).zfill(2), str(minutes).zfill(2), str(seconds).zfill(2)]) 
        url = ''.join([self.baseurl, '/extensions/ki_timesheets/processor.php'])
        postdata = urlencode({  'id':'',
                                'axAction':'add_edit_timeSheetEntry',
                                'projectID':pid,
                                'filter':'',
                                'activityID':aid,
                                'description':'',
                                'start_day':param_start_date,
                                'end_day':param_end_date,
                                'start_time':param_start_time,
                                'end_time':param_end_time,
                                'duration':param_duration,
                                'location':'',
                                'trackingNumber':'',
                                'comment':'',
                                'commentType':0,
                                'userID[]':userid,
                                'budget':'',
                                'approved':'',
                                'statusID':1,
                                'billable':0,
                                'rate':'',
                                'fixedRate':''})
        request = Request(url, postdata)          
        self.session.open(request)

def main():
        
    cmd_parser = ArgumentParser(description='Log Work to a Kimai instance')
    cmd_parser.add_argument('--configFile', type=str, default='log2kimai.cfg')
    cmd_args = cmd_parser.parse_args()
    config_file = ConfigParser()

    try:
        config_file.readfp(open(cmd_args.configFile))
    except IOError:
        exit('Error: Specified config file was not found or not readable.')

    try:
        datetime_start = datetime.strptime('141201-0710', '%y%m%d-%H%M')
    except ValueError:
        exit('Error parsing start date (format is supposed to be YYYYmmdd-HHmm)')

    km = kimaiMessage(config_file.get('kimai','baseurl'), 
                      config_file.get('kimai', 'user'), 
                      config_file.get('kimai', 'pass'))
    datetime_end = datetime_start + timedelta(minutes=+5)
    km.logWork(datetime_start, datetime_end, 1, 1)


if __name__ == "__main__":
    main()
