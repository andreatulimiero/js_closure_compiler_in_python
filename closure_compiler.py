import os, requests, json

# Default settings
config = {
  'url' : 'http://closure-compiler.appspot.com/compile',
  'compilation_level' : 'WHITESPACE_ONLY',
  'output_format' : 'text',
  'output_info' : 'compiled_code',
  'output_file' : 'app.min.js'
}
files_names = []

def switch_to_current_dir():
  abspath = os.path.abspath(__file__)
  dname = os.path.dirname(abspath)
  os.chdir(dname)

def load_configs():
  print('Loading configurations ...')
  try:
    f = open('.closure_compiler_config.json')
    try:
      loaded_config = json.loads(f.read().strip())
    except json.JSONDecodeError:
      print('#Malformed config file, using defaults ...')
      return
    for key in loaded_config:
      if key not in config:
        print('#' + key + ' is not a valid configuration')
      else:
        config[key] = loaded_config[key]
  except FileNotFoundError:
    print('#No .closure_compile_config.json file found. Using default values')

def get_js_code():
  print('\nReading files specified in .to_closure_compile ...')
  joined_js = ''
  try:
    to_closure_compile = open('.to_closure_compile')
    for filename in to_closure_compile.read().split('\n'):
      try:
        f = open(filename)
        joined_js += f.read()
        print('|-' + filename)
      except FileNotFoundError:
        print('|-No ' + filename + ' file found')
  except FileNotFoundError:
    print('#No .to_closure_compile file found')
  return joined_js

if __name__ == '__main__':
  switch_to_current_dir()
  load_configs()
  data = {
    'js_code' : get_js_code(),
    'compilation_level' : config['compilation_level'],
    'output_format' : config['output_format'] ,
    'output_info' : config['output_info']
  }
  print('\nRequesting compilation ...')
  if not len(data['js_code']):
    print('#No file specified, aborting compilation\n')
    exit(1)
  r = requests.post(config['url'], data=data)
  with open(config['output_file'], mode='w+') as output_file:
    print(r.text, file=output_file)
    print('Compilation saved in ' + config['output_file'] + '\n')
    exit(0)