#!/usr/bin/env python
from log2kimai import kimaiMessage
from datetime import datetime, timedelta

def test_list_activity():
    kimai = kimaiMessage('http://demo.kimai.org', 'admin', 'changeme', '0.9.3.1384')
    assert len(kimai.activity) > 0

def test_list_projects():
    kimai = kimaiMessage('http://demo.kimai.org', 'admin', 'changeme', '0.9.3.1384')
    assert len(kimai.projects) > 0
