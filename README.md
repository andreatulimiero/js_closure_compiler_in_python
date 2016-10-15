# JS closure compiler in Python
Simple JS closure compiler written in Python that communicates with [Google Closure Compiler Service](https://closure-compiler.appspot.com/home). <br/>
Compile a JS file with closure not only reduce the size of the specified files, that is critical in the creation of a modern site, but also ensure
full compatibility with older sites that don't support the new ECMASCRIPT2016, giving you the possibility to use all of its sugar features.
All you need to do is specify a list of the files you want to be compiled

## Usage
Put the `closure_compiler.py` wherever you want and add all the files you want to compile in the `.to_closure_compile` file,
one line per file - relative paths are allowed as well. <br/>
Example: <br/>
#####Project's folder structure
```html
index.html
js/
 ├─closure_compiler.py
 ├─elements/
   ├─topbar.js
 ├─config.js
 ├─app.js
```

#####.to_closure_compile file structure
```html
elements/topbar.js
config.js 
app.js
```
##Configuration
###Configuration file
The compiler can be customized to suit your needs. <br/>
The configuration is a json dictionary file, it has to be called `.closure_compiler_congif.json`. <br/>
However, if no config file it's specified, the default values will be used instead <br/>
Configuration file structure (below are the default values):
```json
{
  "url" : "http://closure-compiler.appspot.com/compile",
  "compilation_level" : "WHITESPACE_ONLY",
  "output_format" : "text",
  "output_info" : "compiled_code",
  "output_file" : "app.min.js"
}
```
###Configuration options
<dl> 
  <dt>url</dt>
  <dd>This field shouldn't not be changed, but in case google will change the url, you can specify yours</dd>
  <dt>compilation_level</dt>
  <dd>
    This is the optimization level you want to use. Possible options are <em>WHITESPACE_ONLY</em>, <em>SIMPLE_OPTIMIZATIONS</em> and <em>ADVANCED_OPTIONS</em>
  </dd>
  <dt>output_format</dt>
  <dd>This is the format that the server will use to return the file. Possible formats are <em>text</em>, <em>xml</em> and <em>json</em></dd>
  <dt>output_info</dt>
  <dd>
    This parameter indicates what kind of information the server should return. Possible infos are <em>compiled_code</em>, <em>warnings</em>, 
    <em>errors</em> and <em>statistics</em></dd>
  <dt>output_file</dt>
  <dd>Specify the name of the file you want the compiled_code, or any other information, to be saved</dd>
</dl>
Other informations can be found directly in the Google's [site](https://developers.google.com/closure/compiler/docs/gettingstarted_api)

