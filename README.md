# Example Code
``` python
import pythconf
import os
conf = pyconf.config('test', os.getcwd())
# 'test' will be the filename and os.getcwd() will return the current directory so the .pyconf will be created in the current directory
print(conf.dat) # dict
```
# Using pyconf files
you can create a .pyconf file yourself, to use the data, you have to use the same filename (with or without .pyconf) in the file argument
## .pyconf files
### test.pyconf
```
USERNAME = None
PASSWORD = None
```
## Accesing data
``` python
import pythconf
import os
from getpass import getpass
conf = pyconf.config('test', os.getcwd())
if "USERNAME" not in conf.dat:
  user = input('Username: ')
  conf.dat["USERNAME"] = user
else:
  if conf.dat["USERNAME"] == None:
    user = input('Username: ')
    conf.dat["USERNAME"] = user
if "PASSWORD" not in conf.dat:
  password = getpass('Password: ')
  conf.dat["PASSWORD"] = password
else:
  if conf.dat["PASSWORD"] == None:
    password = getpass('Password: ')
    conf.dat["PASSWORD"] = password
```

