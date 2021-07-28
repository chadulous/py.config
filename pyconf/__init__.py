import ast
import os
from pathlib import Path
class Error(Exception):
    """Base class for other exceptions"""
    pass
class config:
  def __init__(self, file: str, path: str):
    '''adds new file to config list
    NOTE: if you want the conf file to be in the same place as the current file, you can use os.getcwd()'''
    path = path.split('/')
    path.append(f'{file.split(".")[0]}.pyconf')
    check = Path(f'/{os.path.join(*path)}')
    if not check.is_file():
      del path[-1]
      os.system('cd')
      os.system(f'cd /{os.path.join(*path)}')
      os.system(f'> {file.split(".")[0]}.pyconf')
    del path[-1]
    path.append(f'{file.split(".")[0]}.pyconf')
    path = os.path.join(*path)
    self.rawdat = open(f'/{path}', 'r').read()
    self.dat = {}
    self.path = path
    for line in self.rawdat.splitlines():
      if line.count(' = ') >= 1:
        line = line.split(' = ')
        if line[1] != 'None':
          self.dat[line[0]] = line[1]
        else:
          self.dat[line[0]] = None
    self.convert()
  def add(self, key, defaultval=None):
    self.dat[key] = defaultval
    self.convert()
  def convert(self):
    open(f'/{self.path}', 'w').write(f'')
    file = open(f'/{self.path}', 'a')
    for data in self.dat:
      file.write(f'\n{data} = {self.dat[data]}')
