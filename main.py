import bestconf
import os
conf = bestconf.config('test', os.getcwd())
print(conf.dat)