log2kimai
=========

a python module  / command line tool to log work to a standart Kimai instance via http(s)

supported versions
------------------
+ 0.9.3.1384
+ 0.9.2.1306

cmd usage
---------
```
log2kimai.py [-h] [--configFile CONFIGFILE] [-v] [-d]
                    action [action ...]

Log Work to a Kimai instance

positional arguments:
  action                add, info projects/activities

optional arguments:
  -h, --help            show this help message and exit
  --configFile CONFIGFILE
                        default: log2kimai.cfg
  -v, --verbose
  -d, --dry             dryrun; just validating input
  
example: echo "151021-1600|120|1|1|comment" | ./log2kimai.py add
example: cat input.psv | ./log2kimai.py add
example: ./log2kimai.py info activities
  
```

modul usage
-----------

```
from log2kimai import kimaiMessage

kimai = kimaiMessage('http://demo.kimai.org', 'admin', 'changeme', '0.9.3.1384')
kimai.logWork(<datetime_start>, <datetime_end>, <project_id>, <activitie_id>, <comment>)

```