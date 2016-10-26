import os, requests, json
from functools import reduce
from termcolor import colored
import colorama

# Default settings
config = {
  'url' : 'http://closure-compiler.appspot.com/compile',
  'compilation_level' : 'WHITESPACE_ONLY',
  'output_format' : 'text',
  'output_info' : 'compiled_code',
  'output_file' : 'app.min.js'
}

files_names = []

def print_info(info):
  print( colored(info, 'white') )

def print_success(success):
  print( colored(success, 'green'))

def print_warning(warning):
  print( colored(warning, 'yellow') )

def print_error(error):
  print( colored(error, 'red') )
  
def print_filename(filename):
  print( colored(filename, 'grey') )

def print_stat(stat):
  print( colored(stat, 'cyan') )

def switch_to_current_dir():
  abspath = os.path.abspath(__file__)
  dname = os.path.dirname(abspath)
  os.chdir(dname)

def load_configs():
  print_info('Loading configurations ...')
  try:
    f = open('.closure_compiler_config.json')
    try:
      loaded_config = json.loads(f.read().strip())
    except json.JSONDecodeError:
      print_warning('#Malformed config file, using defaults ...')
      return
    for key in loaded_config:
      if key not in config:
        print_warning('#' + key + ' is not a valid configuration')
      else:
        config[key] = loaded_config[key]
  except FileNotFoundError:
    print_warning('#No .closure_compile_config.json file found. Using default values')

def get_js_code():
  print('\nReading files specified in .to_closure_compile ...')
  joined_js = ''
  try:
    to_closure_compile = open('.to_closure_compile')
    for filename in to_closure_compile.read().split('\n'):
      try:
        f = open(filename.strip())
        joined_js += f.read()
        files_names.append(filename.strip())
        print_filename('|-' + filename)
      except FileNotFoundError:
        print_error('|-No ' + filename + ' file found')
  except FileNotFoundError:
    print_warning('#No .to_closure_compile file found')
  return joined_js

if __name__ == '__main__':
  colorama.init()
  switch_to_current_dir()
  load_configs()
  data = {
    'js_code' : get_js_code(),
    'compilation_level' : config['compilation_level'],
    'output_format' : config['output_format'] ,
    'output_info' : config['output_info']
  }

  print_info('\nRequesting compilation ...')
  if not len(data['js_code']):
    print_error('#No file specified, aborting compilation\n')
    exit(2)
    
  try:
    r = requests.post(config['url'], data=data)    
  except:
    print_error('Impossible to communicate with the server, check your internet connection')
    exit(1)
  with open(config['output_file'], mode='w+') as output_file:
    print(r.text, file=output_file)
    print_success('Compilation saved in ' + config['output_file'] + '\n')
    current_size = os.path.getsize(config['output_file'])//1024
    previous_size = reduce(lambda x,y: x + y, [os.path.getsize(x) for x in files_names])//1024
    print_info('Previous size: ' + str(previous_size) + ' Kb')
    print_info('Current size: ' + str(current_size) + ' Kb')
    saved_percentage = int((previous_size - current_size)/previous_size*100)
    print_stat('Saved: ~' + str(saved_percentage if saved_percentage > 0 else '100') + '% (' + str(previous_size - current_size) + ' Kb) of room')
    exit(0)