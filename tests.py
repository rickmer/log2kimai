#!/usr/bin/env python
from log2kimai import KimaiMessage
from datetime import datetime, timedelta

def test_list_activity():
    kimai = KimaiMessage('http://demo.kimai.org', 'admin', 'changeme', '0.9.3.1384')
    assert len(kimai.activity) > 0

def test_list_projects():
    kimai = KimaiMessage('http://demo.kimai.org', 'admin', 'changeme', '0.9.3.1384')
    assert len(kimai.projects) > 0
